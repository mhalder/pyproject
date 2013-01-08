=========
PyProject
=========

PyProject provides a basic skeleton for new python projects including
distutils, sphinx documentation, unittest and coverage using the BSD license.


Prerequisites
=============

you need the following packages installed:

    1. python-sphinx
    2. python-coverage
    3. python-nose
    4. gettext

We recommend using virtualenv to use the latest versions of these packages
without interfering with the locally installed packages.


Installation
============

you can install this package with easy_install using::

    easy_install PyProject-0.2.0.tar.gz

or without easy_install::

    tar xzf PyProject-0.2.0.tar.gz
    cd PyProject-0.2.0
    python setup.py install


Usage
=====

create documentation::

    make html
    open doc/gen/html/index.html

create translations:

    1. use _ from the pyproject.i18n module for the strings
    2. create a pot file for translations (make pot)
    3. create a new translation language::

           cd i18n
           ./create_translations.sh de

    4. translate the strings within de.po
    5. add and commit de.po

update translations:

    1. create a new pot file for translations (make pot)
    2. update all translations files::

           cd i18n
           ./update_translations.sh

    3. update the missing translation strings within the \*.po files.

run tests with coverage::

    nosetests --with-coverage

create distribution (source dist):

    1. create documentation (see above)
    2. create translations (see above)
    3. run build::

        ./setup.py build

    4. run sdist::

        ./setup.py sdist

test translations:

    `setup.py build` creates the mo files for the translation. Now it is 
    possible to run the application with the translation files. Just set the 
    `LANG` environment variable::

        LANG=de ./bin/pyproject
