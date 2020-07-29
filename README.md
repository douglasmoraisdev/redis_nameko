# Redis Nameko

Lib para utilizar Redis no framework Nameko.


## Instalação
Adicionar ao `requirements.txt` do projeto:

```
git+https://github.com/douglasmoraisdev/redis_nameko.git#egg=redis_nameko
```

OU manualmente com PIP:
```bash
$ pip install git+https://github.com/douglasmoraisdev/redis_nameko.git#egg=redis_nameko
```



## Configuração
A Lib utiliza `o arquivo config.yml` para sua configuração. As mesmas podem ser encontradas no arquivo 'sample.config.yml'.

```yml
REDIS_HOST: 'localhost' # Host Redis
REDIS_PORT: 6379 # Porta
REDIS_DB: 0 # DB
REDIS_PASS : '123456123456ddx123' # Senha(opcional)

```

## Importação e uso
Para utilizar o log basta importar o objeto `redis_nameko` da package e utilizar como uma dependencia no serviço.

## Métodos

### zrank(zkey: str, payload: dict)
Realiza um ZRANK na chave especificada com o payload.
Retorna None caso não encontre correspendencia

### zrank(zkey: str, payload: dict)
Realiza um ZADD na chave especificada com o payload

### zrem(zkey: str, payload: dict)
Realiza um ZREM na chave especificada com o payload
