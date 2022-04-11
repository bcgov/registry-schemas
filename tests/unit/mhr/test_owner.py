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
from registry_schemas.example_data.mhr import ADDRESS, PERSON_NAME


# testdata pattern is ({desc}, {valid}, {org}, {individual}, {address}, {type})
LONG_ORG_NAME = '01234567890123456789012345678901234567890123456789012345678901234567890'
TEST_DATA_OWNER = [
    ('Valid org', True, 'org name', None, ADDRESS, 'SO'),
    ('Valid ind', True, None, PERSON_NAME, ADDRESS, 'SO'),
    ('Valid JT type', True, 'org name', None, ADDRESS, 'JT'),
    ('Valid TC type', True, 'org name', None, ADDRESS, 'TC'),
    ('Invalid missing owner', False, None, None, ADDRESS, 'SO'),
    ('Invalid missing owner', False, 'org name', None, None, 'TC'),
    ('Invalid missing type', False, 'org', None, ADDRESS, None),
    ('Invalid type', False, 'org name', None, ADDRESS, 'XX'),
    ('Invalid org too long', False, LONG_ORG_NAME, None, ADDRESS, 'SO')
]


@pytest.mark.parametrize('desc,valid,org,individual,address,type', TEST_DATA_OWNER)
def test_base_info(desc, valid, org, individual, address, type):
    """Assert that the schema is performing as expected."""
    data = {
    }
    if org:
        data['organizationName'] = org
    if individual:
        data['individualName'] = individual
    if address:
        data['address'] = address
    if type:
        data['type'] = type

    is_valid, errors = validate(data, 'owner', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
