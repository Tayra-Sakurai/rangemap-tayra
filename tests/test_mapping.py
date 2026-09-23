# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
import pytest
from rangemap_tayra import *

def test_loader():
    data = load_data('Pyongyang', 100.)
    assert isinstance(data, DataMap)