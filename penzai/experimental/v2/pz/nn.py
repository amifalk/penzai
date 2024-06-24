# Copyright 2024 The Penzai Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module of aliases for penzai neural networks."""

# pylint: disable=g-multiple-import,g-importing-member,unused-import

from penzai.experimental.v2.nn.attention import (
    ApplyAttentionMask,
    Attention,
    KVCachingAttention,
)
from penzai.experimental.v2.nn.basic_ops import (
    CastToDType,
    Elementwise,
    Softmax,
)
from penzai.experimental.v2.nn.combinators import (
    Residual,
    BranchAndAddTogether,
    BranchAndMultiplyTogether,
)
from penzai.experimental.v2.nn.dropout import (
    DisabledDropout,
    maybe_dropout,
    StochasticDropout,
)
from penzai.experimental.v2.nn.embeddings import (
    EmbeddingTable,
    EmbeddingLookup,
    EmbeddingDecode,
    ApplyRoPE,
)
from penzai.experimental.v2.nn.grouping import (
    CheckedSequential,
    CheckStructure,
    Identity,
    inline_anonymous_sequentials,
    inline_groups,
    is_anonymous_sequential,
    is_sequential_or_named,
    NamedGroup,
    Sequential,
)
from penzai.experimental.v2.nn.layer import (
    Layer,
)
from penzai.experimental.v2.nn.layer_stack import (
    LayerStackVarBehavior,
    LayerStackGetAttrKey,
    LayerStack,
    layerstack_axes_from_keypath,
)
from penzai.experimental.v2.nn.linear_and_affine import (
    AddBias,
    ConstantRescale,
    NamedEinsum,
    Affine,
    Linear,
    LinearOperatorWeightInitializer,
    LinearInPlace,
    RenameAxes,
    contract,
    variance_scaling_initializer,
    xavier_normal_initializer,
    xavier_uniform_initializer,
    constant_initializer,
    zero_initializer,
)
from penzai.experimental.v2.nn.parameters import (
    ParameterLike,
    derive_param_key,
    make_parameter,
    assert_no_parameter_slots,
)
from penzai.experimental.v2.nn.standardization import (
    LayerNorm,
    Standardize,
    RMSLayerNorm,
    RMSStandardize,
)
