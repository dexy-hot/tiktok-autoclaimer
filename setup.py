#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup for tiky."""

from setuptools import setup, find_packages


INSTALL_REQUIRES = [
   'requests',
   'colorama',
   'halo',
]

setup(
    name='tiky',
    version='1.0.2',
    description='TikTok AutoClaimer.',
    long_description='Automatically and periodically tries to claim multiple TikTok usernames using private API.',
    license='Dexy License',
    author='Dexy',
    author_email='dexy@flamelo.com',
    url='https://tiktokapi.xyz/',
    keywords='tiktok, autoclaimer, turbo, dexy,api,',
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    zip_safe=False,
	packages=find_packages(),
    py_modules=['tiky'],
    entry_points={'console_scripts': ['tiky = tiky:main']},
)