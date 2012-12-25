# Makefile for the python project
#

PACKAGE_DIR=pyproject
PROJECT_DIR := $(shell pwd)
PYFILES:=$(shell find ${PACKAGE_DIR} -name '*.py')
BINFILES:=$(ls bin/)

DOMAIN_NAME=pyproject
MAINTAINER_EMAIL=Martin Halder <martin.halder@gmail.com>

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"
	@echo "  pot        to create the pot file for translations

clean:
	-$(MAKE) -C doc clean
	-rm -rf i18n/*.pot

html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man texinfo info gettext changes linkcheck doctest:
	PYTHONPATH=$(PROJECT_DIR) $(MAKE) -C doc $@

pot:
	echo $(PYFILES) $(BINARY_FILES) | xargs \
		xgettext --package-name "$(DOMAIN_NAME)" \
		--msgid-bugs-address "$(MAINTAINER_EMAIL)" \
		--copyright-holder "$(MAINTAINER_EMAIL)" \
		--from-code UTF-8 --sort-by-file --add-comments=i18n: \
		-d $(DOMAIN_NAME) -p i18n -o ${DOMAIN_NAME}.pot
	$(PYHTON) i18n/posplit i18n/${DOMAIN_NAME}.pot
