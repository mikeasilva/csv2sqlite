========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/csv2sqlite/badge/?style=flat
    :target: https://readthedocs.org/projects/csv2sqlite
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/csv2sqlite/csv2sqlite.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/csv2sqlite/csv2sqlite

.. |codecov| image:: https://codecov.io/github/csv2sqlite/csv2sqlite/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/csv2sqlite/csv2sqlite

.. |version| image:: https://img.shields.io/pypi/v/csv2sqlite.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/csv2sqlite

.. |commits-since| image:: https://img.shields.io/github/commits-since/csv2sqlite/csv2sqlite/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/csv2sqlite/csv2sqlite/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/csv2sqlite.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/csv2sqlite

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/csv2sqlite.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/csv2sqlite

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/csv2sqlite.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/csv2sqlite


.. end-badges

Python package to load a CSV into a SQLite database

* Free software: MIT license

Installation
============

::

    pip install csv2sqlite

Documentation
=============

https://csv2sqlite.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
