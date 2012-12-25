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

We recommend using virtualenv to use the latest packages of this packages
without interfering with the locally installed packages.

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

create translations:

    1. Use _ from the pyproject.i18n module for the strings
    2. Create a pot file for translations (make pot)
    3. Create a new translation language:
           cd i18n
           ./create_translations.sh de
    4. Translate the strings within de.po
    5. Add de.po to the SCM

update translations:

    1. Create a new pot file for translations (make pot)
    2. Update all translations files
           cd i18n
           ./update_translations.sh
    3. Update the missing translation strings within the \*.po files.

run tests with coverage

    1. nosetests --with-coverage

create distribution (source dist)

    1. create documentation (see above)
    2. create translations (see above)
    2. ./setup.py sdist

test translations:

    After the distribution was created the mo files for translation where
    built. Now it is possible to run the application with the translation 
    files. Just set the LANG env variable:

        LANG=de ./bin/pyproject
