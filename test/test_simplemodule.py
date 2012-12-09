# -*- coding: utf-8 -*-
#
# Copyright 2012 Martin Halder <martin.halder@gmail.com>
#
# This file is part of PyProject.
#
# PyProject is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# PyProject is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyProject. If not, see <http://www.gnu.org/licenses/>.


"""This is a test for the simplemodule

    :module: test_simplemodule
    :moduleauthor: Martin Halder <martin.halder@gmail.com>

"""

from unittest import TestCase
from simplemodule import SimpleClass


class test_SimpleClass(TestCase):

    """Test SimpleClass constructor."""

    def test_constructor(self):

        """Call constructor and check members."""

        simple = SimpleClass()
        self.assertEqual(simple.one, 1)
        self.assertEqual(simple.two, 2)

    def test_constructor_with_values(self):

        """Call constructor and check members."""

        simple = SimpleClass(3, 4)
        self.assertEqual(simple.one, 3)
        self.assertEqual(simple.two, 4)

    def test_do_something(self):

        """Call constructor and check members."""

        simple = SimpleClass(3, 4)
        self.assertEqual(simple.do_something(), 'test')
