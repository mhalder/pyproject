#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (C) 2012 Mathias Weber <mathew.weber@gmail.com>
# Copyright (C) 2012 Martin Halder <martin.halder@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
#


######## DO NOT TOUCH THIS (HEAD TO THE SECOND PART) ########################

import os
import shutil

from distutils.core import setup
from distutils.command.build import build
from distutils.spawn import find_executable, spawn


def find_packages(path='.'):
    ''' Find all python packages to install them. This searches recursively
        for all subpackages.

        :path: The path to start search for the packages. (or a list with
                paths to search through)
        :returns: A list with all the packages
    '''
    result = []
    if type(path) is list:
        for p in path:
            result += find_packages(p)
        return result

    walker = os.walk(path)
    result = []
    for path, directories, filenames in walker:
        if '__init__.py' in filenames:
            result.append(path)

    return result


def find_data(data_info):
    ''' find all data files and create a list with the install targets.

        :data_info: A tuple with the search path and the install path or a
                list with tuples to search for.
        :returns: A a list with all the tupples for the data files

        TODO: add support for other platforms than Linux (or maybe it
        already works, so we need to test it)
    '''
    result = []
    if type(data_info) is list:
        for data in data_info:
            result += find_data(data)
        return result

    walker = os.walk(data_info[0], topdown=True)
    for path, directories, filenames in walker:
        resultfiles = []
        for name in filenames:
            resultfiles.append(os.path.join(path, name))
        pathname = path[len(data_info[0]):]
        while pathname.startswith('/'):
            pathname = pathname[1:]
        result.append((os.path.join(data_info[1], pathname), resultfiles))

    return result


class InstallAndUpdateDataDirectory(build):
    def run(self):
        self.build_mo()
        build.run(self)

    def build_mo(self):
        if not find_executable('msgfmt'):
            self.warn("msgfmt executable could not be found -> no "
                      'translations will be built')
        domain = self.distribution.metadata.name
        podir = 'i18n'
        if not os.path.isdir(podir):
            self.warn('could not find %s directory' % podir)
            return

        for po in os.listdir(podir):
            if not po.endswith('.po'):
                continue
            pofile = os.path.join(podir, po)
            modir = os.path.join('locale', po[:-3], 'LC_MESSAGES')
            mofile = os.path.join(modir, '{0}.mo'.format(domain))
            mobuildfile = os.path.join(domain, mofile)
            cmd = ['msgfmt', '-v', '-o', mobuildfile, pofile, '-c']

            self.mkpath(os.path.join(domain, modir))
            self.make_file([pofile], mobuildfile, spawn, (cmd,))
        if os.path.isdir('locale'):
            shutil.rmtree('locale')
        shutil.move(os.path.join(domain, 'locale'), 'locale')


######## ONLY MODIFY WHAT IS BELOW ##########################################


setup(name='pyproject',
      version='0.2.0',
      description='Python Project Skeleton',
      author='Martin Halder',
      author_email='martin.halder@gmail.com',
      url='https://github.com/mhalder/pyproject',
      cmdclass={'build': InstallAndUpdateDataDirectory},
      packages=find_packages('pyproject'),
      scripts=[os.path.join('bin', 'pyproject')],
      data_files=(find_data([('locale', 'locale'),
          ('doc/gen', 'share/doc/pyproject')])),
      )
