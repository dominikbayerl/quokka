"""Backends integration"""
#  Copyright 2022-2023 Quarkslab
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from quokka.backends.capstone import (
    get_capstone_context,
    capstone_decode_instruction,
)
from quokka.backends.pypcode import (
    pypcode_decode_block,
    pypcode_decode_instruction,
    get_pypcode_context,
)

__all__ = [
    # From capstone.py
    "get_capstone_context",
    "capstone_decode_instruction",
    # From pypcode.py
    "get_pypcode_context",
    "pypcode_decode_instruction",
    "pypcode_decode_block",
]
