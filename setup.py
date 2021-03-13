from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='optlab',
    version='0.0',
    description='OptReg laboratory scripts',
    url='https://github.com/VemundRogne/OptReg',
    install_requires=required
)