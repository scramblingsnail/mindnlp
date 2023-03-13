# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Test T5"""
import unittest
import numpy as np

import mindspore

from mindspore import Tensor

from mindnlp.models.t5 import T5Config, T5LayerNorm, T5DenseActDense, T5DenseGatedActDense
from mindnlp.models.t5 import T5LayerFF, T5Attention, T5LayerSelfAttention, T5LayerCrossAttention, T5Block
class TestModelingT5(unittest.TestCase):
    r"""
    Test T5
    """
    def setUp(self):
        """
        Set up.
        """
        self.input = None

    def test_t5_layer_norm(self):
        r"""
        Test T5LayerNorm
        """
        hidden_size = 512
        model = T5LayerNorm((hidden_size,), eps = 1e-6)

        input_ids = Tensor(np.random.randn(hidden_size), mindspore.float32)

        outputs = model(input_ids)
        assert outputs.shape == (hidden_size, )

    def test_t5_dense_act_dense(self):
        r"""
        Test T5DenseActDense
        """
        config = T5Config()
        model = T5DenseActDense(config)

        input_ids = Tensor(np.random.randn(2, config.d_model), mindspore.float32)

        outputs = model(input_ids)
        assert outputs.shape == (2, config.d_model)

    def test_t5_dense_gated_act_dense(self):
        r"""
        Test T5DenseGatedActDense
        """
        config = T5Config()
        model = T5DenseGatedActDense(config)

        input_ids = Tensor(np.random.randn(2, config.d_model), mindspore.float32)

        outputs = model(input_ids)
        assert outputs.shape == (2, config.d_model)

    def test_t5_layer_ff(self):
        r"""
        Test T5LayerFF
        """
        config = T5Config()
        model = T5LayerFF(config)

        input_ids = Tensor(np.random.randn(2, config.d_model), mindspore.float32)

        outputs = model(input_ids)
        assert outputs.shape == (2, config.d_model)

    def test_t5_attention(self):
        r"""
        Test T5Attention
        """
        config = T5Config()
        model = T5Attention(config)

        input_ids = Tensor(np.random.randn(4, 64, 512), mindspore.float32)

        outputs = model(input_ids)
        assert outputs[0].shape == (4, 64, 512)
        assert outputs[2].shape == (1, 8, 64, 64)

    def test_t5_layer_self_attention(self):
        r"""
        Test T5LayerSelfAttention
        """
        config = T5Config()
        model = T5LayerSelfAttention(config)

        input_ids = Tensor(np.random.randn(4, 64, 512), mindspore.float32)

        outputs = model(input_ids)
        assert outputs[0].shape == (4, 64, 512)
        assert outputs[2].shape == (1, 8, 64, 64)

    def test_t5_layer_cross_attention(self):
        r"""
        Test T5LayerCrossAttention
        """
        config = T5Config()
        model = T5LayerCrossAttention(config)

        input_ids = Tensor(np.random.randn(4, 64, 512), mindspore.float32)

        outputs = model(input_ids, key_value_states=None)
        assert outputs[0].shape == (4, 64, 512)
        assert outputs[2].shape == (1, 8, 64, 64)

    def test_t5_block(self):
        r"""
        Test T5Block
        """
        config = T5Config()
        model = T5Block(config)

        input_ids = Tensor(np.random.randn(4, 64, 512), mindspore.float32)

        outputs = model(input_ids)
        assert outputs[0].shape == (4, 64, 512)
        assert outputs[1].shape == (1, 8, 64, 64)