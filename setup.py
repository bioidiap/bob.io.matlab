#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Mon 16 Apr 08:18:08 2012 CEST

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['xbob.blitz', 'xbob.io.base']))
from xbob.blitz.extension import Extension
import xbob.io.base

include_dirs = [xbob.io.base.get_include()]

packages = ['boost', 'bob-io >= 2.0.0a2', 'matio >= 1.3.0']
version = '2.0.0a0'

setup(

    name='xbob.io.matlab',
    version=version,
    description='Enable xbob.io.base to handle Matlab(R) files',
    url='http://github.com/bioidiap/xbob.io.matlab',
    license='BSD',
    author='Andre Anjos',
    author_email='andre.anjos@idiap.ch',

    long_description=open('README.rst').read(),

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
      'setuptools',
      'xbob.blitz',
      'xbob.io.base',
    ],

    namespace_packages=[
      "xbob",
      "xbob.io",
      ],

    ext_modules = [
      Extension("xbob.io.matlab.version",
        [
          "xbob/io/matlab/version.cpp",
          ],
        packages = packages,
        include_dirs = include_dirs,
        version = version,
        ),
      Extension("xbob.io.matlab._library",
        [
          "xbob/io/matlab/bobskin.cpp",
          "xbob/io/matlab/utils.cpp",
          "xbob/io/matlab/file.cpp",
          "xbob/io/matlab/main.cpp",
          ],
        packages = packages,
        boost_modules = ['system'],
        include_dirs = include_dirs,
        version = version,
        ),
      ],

    classifiers = [
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Environment :: Plugins',
      ],

    )
