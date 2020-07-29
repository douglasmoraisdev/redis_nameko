import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redis_nameko",
    version="0.0.1",
    author="Douglas Morais",
    author_email="msantos.douglas@gmail.com",
    description="Redis dependency for Nameko",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/douglasmoraisdev/redis_nameko.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
        'nameko==3.0.0-rc8',
        'redis'
    ],
    dependency_links=['https://github.com/douglasmoraisdev/backoff_retry/tarball/master#egg=backoff_retry']
)