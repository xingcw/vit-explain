import setuptools
from pip._internal.req import parse_requirements

__version__ = '0.0.1'

setuptools.setup(
    name='vit_explain',
    version=__version__,
    packages=setuptools.find_packages()
)