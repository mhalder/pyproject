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


"""This is a very simple module.

    :module: simplemodule
    :moduleauthor: Martin Halder <martin.halder@gmail.com>

"""


class SimpleClass:

    """Demonstrate class docstrings."""

    def __init__(self, one=1, two=2):

        """Set default attribute values only.

        This class does nothing except setting the
        default attributes.

        :param one: first useless parameter
        :param two: second one

        :returns: nothing

        :raises: nothing

        """

        self.one = one
        self.two = two

    def do_something(self, thing=1):

        """simple useless function.

        :param thing: some thing
        :returns: never
        :raises: your salary

        """

        pass
