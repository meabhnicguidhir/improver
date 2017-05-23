# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# (C) British Crown Copyright 2017 Met Office.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
"""Unit tests for the generate_ancillary.GenerateLandAncil plugin."""


import unittest
from iris.cube import Cube
from iris.tests import IrisTest
import numpy as np

from improver.generate_ancillary import GenerateLandAncil as GenLandAncil


class TestGenAncil(IrisTest):
    """Test the land mask ancillary generation plugin."""
    def setUp(self):
        """setting up paths to test ancillary files"""
        landmask_data = np.array([[0.2, 0., 0.],
                                  [0.7, 0.4, 0.05],
                                  [1, 0.95, 0.7]])
        self.landmask = Cube(landmask_data, long_name='test land')
        self.expected_mask = np.array([[0.25, 0., 0.],
                                       [0.75, 0.25, 0.],
                                       [1., 1., 0.75]])

    def test_landmask(self):
        """Test landmask generation"""
        result = GenLandAncil().process(self.landmask)
        self.assertEqual(result.name(), 'test land')
        self.assertArrayEqual(result.data, self.expected_mask)
