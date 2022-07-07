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


LONG_NAME = '01234567890123456789012345678901234567890'
LONG_NAME_MAX = '0123456789012345678901234567890123456789'
DEALER_NAME_MAX = '012345678901234567890123456789012345678901234567890123456789'
VALID_TIMESTAMP = '2022-05-14T21:16:32+00:00'
# testdata pattern is ({desc}, {valid}, {park_name}, {pad}, {address}, {pid}, {tax_date}, {dealer})
TEST_DATA_LOCATION = [
    ('Valid', True, 'park name', '1234', ADDRESS, None, None, None),
    ('Valid no park name', True, None, '1234', ADDRESS, None, None, None),
    ('Valid no pad', True, LONG_NAME_MAX, None, ADDRESS, None, None, None),
    ('Valid no pad, park name', True, None, None, ADDRESS, None, None, None),
    ('Valid pid', True, LONG_NAME_MAX, None, ADDRESS, '123456789', None, None),
    ('Valid tax date', True, LONG_NAME_MAX, None, ADDRESS, '123456789', VALID_TIMESTAMP, None),
    ('Valid dealer', True, LONG_NAME_MAX, None, ADDRESS, '123456789', None, DEALER_NAME_MAX),
    ('Invalid missing address', False, 'org name', '1234', None, None, None, None),
    ('Invalid pad too long', False, 'park name', '1234567', ADDRESS, None, None, None),
    ('Invalid pid too long', False, 'park name', '1234', ADDRESS, '0123456789', None, None),
    ('Invalid dealer too long', False, 'park name', '1234', ADDRESS, None, None, DEALER_NAME_MAX + 'x'),
#    ('Invalid tax date', False, LONG_NAME_MAX, None, ADDRESS, '123456789', 'invalid format', None),
    ('Invalid park name too long', False, LONG_NAME, None, ADDRESS, None, None, None)
]


@pytest.mark.parametrize('desc,valid,park_name,pad,address,pid,tax_date,dealer', TEST_DATA_LOCATION)
def test_location(desc, valid, park_name, pad, address, pid, tax_date, dealer):
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
    if pid:
        data['pidNumber'] = pid
    if tax_date:
        data['taxExpiryDate'] = tax_date
    if dealer:
        data['dealerName'] = dealer

    is_valid, errors = validate(data, 'location', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
