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


class SimpleClass:

    """Demonstrate class docstrings."""

    def __init__(self, spam=1, eggs=2):

        """Set default attribute values only.

        Keyword arguments:
        spam -- a processed meat product
        eggs -- a fine breakfast for lumberjacks

        """

        self.spam = spam
        self.eggs = eggs
