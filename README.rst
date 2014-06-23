.. vim: set fileencoding=utf-8 :
.. Andre Anjos <andre.anjos@idiap.ch>
.. Thu 29 Aug 2013 16:07:57 CEST

.. image:: https://travis-ci.org/bioidiap/bob.io.matlab.svg?branch=master
   :target: https://travis-ci.org/bioidiap/bob.io.matlab
.. image:: http://img.shields.io/badge/docs-latest-orange.png
   :target: https://www.idiap.ch/software/bob/docs/latest/bioidiap/bob.io.matlab/master/index.html
.. image:: https://coveralls.io/repos/bioidiap/bob.io.matlab/badge.png
   :target: https://coveralls.io/r/bioidiap/bob.io.matlab
.. image:: http://img.shields.io/github/tag/bioidiap/bob.io.matlab.png
   :target: https://github.com/bioidiap/bob.io.matlab
.. image:: http://img.shields.io/pypi/v/bob.io.matlab.png
   :target: https://pypi.python.org/pypi/bob.io.matlab
.. image:: http://img.shields.io/pypi/dm/bob.io.matlab.png
   :target: https://pypi.python.org/pypi/bob.io.matlab

===================================
 Support for Matlab I/O in bob::io
===================================

This package contains no bindings. By importing it, you activate a transparent
plugin that makes possible to read and write to Matlab(R) files using
``bob.io.base`` functions.

Installation
------------

Install it through normal means, via PyPI or use ``zc.buildout`` to bootstrap
the package and run test units.

External Library Requirements
=============================

To properly install this package, you will need the following C/C++ components
pre-installed:

1. ``bob-io >= 2.0.0a2``
2. ``matio >= 1.3.0`` (`matio`_ is a C library for handling ``.mat`` files)

To test for the availability of the libraries listed above, use the command
``pkg-config``::

  $ pkg-config --modversion matio
  1.3.3
  $ pkg-config --modversion bob-io
  2.0.0a3

If any of the components is not installed on paths accessible by
``pkg-config``, you have two options:

1. Set the environment variable ``PKG_CONFIG_PATH`` so that ``.pc`` files for
   each of those distributions can be properly located (see ``man pkg-config``
   for details);

2. If you are using ``zc.buildout`` to setup your working environment, you can
   use the buildout variable ``prefixes`` to define the path to the
   installation area for your external packages.

Documentation
-------------

The latest version of the documentation can be found `here <https://www.idiap.ch/software/bob/docs/latest/bioidiap/bob.io.matlab/master/index.html>`_.

Otherwise, you can generate the documentation for this package yourself, after installation, using Sphinx::

  $ sphinx-build -b html doc sphinx

This shall place in the directory ``sphinx``, the current version for the
documentation of the package.

Usage
-----

In order to enable support for Matlab(R) file reading and writing in your
application, make sure to import this module, before calling
``bob.io.base.load`` or similar::

    >>> import bob.io.base
    >>> import bob.io.matlab
    >>> bob.io.base.load('myfile.mat')
    [...]

Testing
-------

You can run a set of tests using the nose test runner::

  $ nosetests -sv

.. warning::

   If Bob <= 1.2.1 is installed on your python path, nose will automatically
   load the old version of the insulate plugin available in Bob, which will
   trigger the loading of incompatible shared libraries (from Bob itself), in
   to your working binary. This will cause a stack corruption. Either remove
   the centrally installed version of Bob, or build your own version of Python
   in which Bob <= 1.2.1 is not installed.

You can run our documentation tests using sphinx itself::

  $ sphinx-build -b doctest doc sphinx

You can test overall test coverage with::

  $ nosetests --with-coverage --cover-package=bob.io.matlab

The ``coverage`` egg must be installed for this to work properly.

Development
-----------

To develop this package, install using ``zc.buildout``, using the buildout
configuration found on the root of the package::

  $ python bootstrap.py
  ...
  $ ./bin/buildout

Tweak the options in ``buildout.cfg`` to disable/enable verbosity and debug
builds.

.. Place here references to all citations in lower case
.. _matio: http://matio.sourceforge.net
