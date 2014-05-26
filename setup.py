#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Mon 16 Apr 08:18:08 2012 CEST

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['bob.blitz', 'bob.io.base']))
from bob.blitz.extension import Extension
import bob.io.base

include_dirs = [bob.io.base.get_include()]

packages = ['boost', 'bob-io >= 2.0.0a2', 'matio >= 1.3.0']
version = '2.0.0a0'

setup(

    name='bob.io.matlab',
    version=version,
    description='Enable bob.io.base to handle Matlab(R) files',
    url='http://github.com/bioidiap/bob.io.matlab',
    license='BSD',
    author='Andre Anjos',
    author_email='andre.anjos@idiap.ch',

    long_description=open('README.rst').read(),

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
      'setuptools',
      'bob.blitz',
      'bob.io.base',
    ],

    namespace_packages=[
      "bob",
      "bob.io",
      ],

    ext_modules = [
      Extension("bob.io.matlab.version",
        [
          "bob/io/matlab/version.cpp",
          ],
        packages = packages,
        boost_modules = ['system'],
        include_dirs = include_dirs,
        version = version,
        ),
      Extension("bob.io.matlab._library",
        [
          "bob/io/matlab/bobskin.cpp",
          "bob/io/matlab/utils.cpp",
          "bob/io/matlab/file.cpp",
          "bob/io/matlab/main.cpp",
          ],
        packages = packages,
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
