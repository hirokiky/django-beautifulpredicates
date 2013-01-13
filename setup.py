#!/usr/bin/env python

from setuptools import setup, find_packages
 
setup (
    name='django-beautifulpredicates',
    version='0.0.1',
    description="Library to provide a predicate dispatch for Django's generic views.",
    long_description="""\
Library to provide a predicate dispatch for Django's generic views.

Requirements
-------------
* Python 2.7 or later (not support 3.x)
* Django 1.4 or later

Features
---------
Using this, You can create views call method in considering of value returned by predicate.
For example folloing view calls method in considering of request parameter::

    class PonyView(PredicateProcessView):
        dispatch_config = (
                              ('get_corn_1', (RequestParamPredicate('corn=1'),)),
                              ('get_corn', (RequestParamPredicate('corn'),)),
                          )
        def get_corn(self, request, *args, **kwargs):
            return HttpResponse('pony with some corn')
    
        def get_corn_1(self, request, *args, **kwargs):
            return HttpResponse('pony with unicorn')
    
        def get_default(self, request, *args, **kwargs):
            return HttpResponse('pony')

In this case, It used:

* beautifulpredicates.views.PredicateProcessView
* beautifulpredicates.predicates.RequestParamPredicate

History
--------
0.0.1 (2012-01-13)
~~~~~~~~~~~~~~~~~~~
* first release 

""",
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    url='https://github.com/hirokiky/django-beautifulpredicates/',
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
