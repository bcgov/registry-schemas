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
"""Test Suite to ensure the MHR location schema is valid."""

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import ADDRESS


# testdata pattern is ({desc}, {valid}, {park_name}, {pad}, {address})
LONG_NAME = '01234567890123456789012345678901234567890'
LONG_NAME_MAX = '0123456789012345678901234567890123456789'
TEST_DATA_LOCATION = [
    ('Valid', True, 'park name', '1234', ADDRESS,),
    ('Valid no park name', True, None, '1234', ADDRESS),
    ('Valid no pad', True, LONG_NAME_MAX, None, ADDRESS),
    ('Valid no pad, park name', True, None, None, ADDRESS),
    ('Invalid missing address', False, 'org name', '1234', None),
    ('Invalid pad too long', False, 'park name', '1234567', ADDRESS),
    ('Invalid park name too long', False, LONG_NAME, None, ADDRESS)
]


@pytest.mark.parametrize('desc,valid,park_name,pad,address', TEST_DATA_LOCATION)
def test_location(desc, valid, park_name, pad, address):
    """Assert that the schema is performing as expected."""
    data = {
        'address': address
    }
    if park_name:
        data['parkName'] = park_name
    if pad:
        data['pad'] = pad
    if not address:
        del data['address']

    is_valid, errors = validate(data, 'location', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
