import os
from datetime import datetime

import redis
from backoff_retry.retry import Retry

from nameko.extensions import DependencyProvider
from nameko import config

retry = Retry(Exception)

class RedisWrapper:

    op = None

    def __init__(self, host, port, db, password):

        self.redis = redis.Redis(host=host, port=port, db=db, password=password)
        self.op = self.redis_obj()

    def redis_obj(self):
        return self.redis

    @retry.backoff_strategy()
    def zrank(self, zkey, payload):
        return self.redis.zrank(zkey, payload)

    @retry.backoff_strategy()
    def zadd(self, zkey, payload):
        self.redis.zadd(zkey, payload)

    @retry.backoff_strategy()
    def zrem(self, zkey, payload):
        self.redis.zrem(zkey, payload)

class Redis(DependencyProvider):

    def setup(self):

        self.host = config.get('REDIS_HOST')
        self.port = config.get('REDIS_PORT')
        self.db = config.get('REDIS_DB')
        self.password = config.get('REDIS_PASS')

    def get_dependency(self, worker_ctx):
        return RedisWrapper(self.host, self.port, self.db, self. password)
