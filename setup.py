# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='elasticache-auto-discovery',
    version='1.0.0',
    description='AWS ElastiCache Auto Discovery Client for Python',
    author='Studio Ousia',
    author_email='admin@ousia.jp',
    url='https://github.com/studio-ousia/elasticache-auto-discovery',
    packages=find_packages(),
    license=open('LICENSE').read(),
    include_package_data=True,
    keywords=['memcached', 'elasticache', 'aws'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ),
    tests_require=['nose'],
    test_suite = 'nose.collector'
)
