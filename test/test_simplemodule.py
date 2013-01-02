# -*- coding: utf-8 -*-
#
# Copyright 2013 Martin Halder <martin.halder@gmail.com>
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
"""This is a test for the simplemodule

    :module: test_simplemodule
    :moduleauthor: Martin Halder <martin.halder@gmail.com>

"""

from unittest import TestCase
from pyproject.simplemodule import SimpleClass


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
