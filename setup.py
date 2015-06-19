from setuptools import setup

setup(
    name             = 'iris_sdk',
    version          = '0.1',
    description      = 'Python client library for IRIS / BBS API',
    author           = 'Bandwidth',
    maintainer       = 'Bandwidth',
    url              = 'https://github.com/scottbarstow/iris-python',
    packages         = ["iris_sdk"],
    long_description = "IRIS / BBS Python API",
    classifiers = [
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)