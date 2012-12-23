=========
PyProject
=========

PyProject provides a basic skeleton for new python projects including
distutils, sphinx documentation, unittest and coverage using GPLv3.


Prerequisites
=============

you need the following packages installed:

    1. sphinx
    2. coverage
    3. nose


Installation
============

you can install this package with easy_install using:

    1. easy_install PyProject-0.1.0.tar.gz

or without easy_install:

    1. tar xzf PyProject-0.1.0.tar.gz
    2. cd PyProject-0.1.0
    3. python setup.py install


Usage
=====

create documentation:

    1. make html
    2. open doc/gen/html/index.html

run tests with coverage

    1. nosetests --with-coverage

create distribution (source dist)

    1. create documentation (see above)
    2. ./setup.py sdist
