# Copyright © 2020 Province of British Columbia
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
"""Test Suite to ensure the MHR base information schema is valid."""

import pytest

from registry_schemas import validate


# testdata pattern is ({desc}, {valid}, {year}, {make}, {model})
TEST_DATA_BASE_INFO = [
    ('Valid all', True, 1994, 'make', 'model'),
    ('Valid no make', True, 1994, None, 'model'),
    ('Valid no model', True, 1994, 'make', None),
    ('Valid just year', True, 1994, None, None),
    ('Missing year', False, None, None, None),
    ('Make too long', False, 1994, '0123456789012345678901234567890123456789012345678901234567890123456', None),
    ('Model too long', False, 1994, None, '0123456789012345678901234567890123456789012345678901234567890123456')
]


@pytest.mark.parametrize('desc,valid,year,make,model', TEST_DATA_BASE_INFO)
def test_base_info(desc, valid, year, make, model):
    """Assert that the schema is performing as expected."""
    data = {
        'year': year,
        'make': make,
        'model': model
    }
    is_valid, errors = validate(data, 'baseInformation', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
