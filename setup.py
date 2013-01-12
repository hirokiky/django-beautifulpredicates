#!/usr/bin/env python

from setuptools import setup, find_packages
 
setup (
    name='django-beautifulpredicates',
    version='0.0',
    description="Library to provide a predicate dispatch for Django's generic views",
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    url='http://bitbucket.org/hirokiky/django-beautifulpredicaties',
    license='MIT License',
    classifiers=[
      'Development Status :: 1 - Planning',
      'Environment :: Plugins',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'Django>=1.4',
    ],
    packages=find_packages(),
    test_suite='runtests.main',
)
