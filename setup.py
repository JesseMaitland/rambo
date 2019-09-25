from os import linesep
from setuptools import setup, find_packages


def get_requirements():
    with open('requirements.txt') as file:
        return [line.rstrip(linesep) for line in file.readlines()]


def get_long_description():
    with open('README.md') as file:
        return file.read()


setup(
    name='rambo-py',
    version='1.0.0',
    author='jesse maitland',
    discription='collection of handy methods for terminal applications',
    include_package_data=True,
    long_description=get_long_description(),
    install_requires=get_requirements(),
    packages=find_packages(exclude=('tests', 'venv', 'logs')),
    scripts=["bin/rambo"],
    download_url="https://github.com/JesseMaitland/rambo/archive/1.0.0.tar.gz"
)
