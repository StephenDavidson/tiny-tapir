"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tiny_tapir',
    version='1.0.0',
    description='Async selenium wrapper',
    long_description=long_description,
    url='https://github.com/StephenDavidson/tiny-tapir',
    author='Stephen Davidson',
    author_email='shdavidson90@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: UI Test Automation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='selenium aysnc aysnchronous angular react',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['selenium'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)