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


# testdata pattern is ({desc}, {valid}, {org}, {individual}, {address}, {type}, {status}, {phone})
LONG_ORG_NAME = '01234567890123456789012345678901234567890123456789012345678901234567890'
TEST_DATA_OWNER = [
    ('Valid org active', True, 'org name', None, ADDRESS, 'SO', 'ACTIVE', None),
    ('Valid ind exempt', True, None, PERSON_NAME, ADDRESS, 'SO', 'EXEMPT', None),
    ('Valid JT type previous', True, 'org name', None, ADDRESS, 'JT', 'PREVIOUS', None),
    ('Valid TC type', True, 'org name', None, ADDRESS, 'TC', 'ACTIVE', '2501234567'),
    ('Invalid missing owner', False, None, None, ADDRESS, 'SO', 'ACTIVE', '2501234567'),
    ('Invalid missing address', False, 'org name', None, None, 'TC', 'ACTIVE', '2501234567'),
    ('Invalid type', False, 'org name', None, ADDRESS, 'XX', 'ACTIVE', '2501234567'),
    ('Invalid status', False, 'org name', None, ADDRESS, 'SO', 'XXX', '2501234567'),
    ('Invalid phone too long', False, 'org name', None, ADDRESS, 'SO', 'ACTIVE', '2501234567          8'),
    ('Invalid org too long', False, LONG_ORG_NAME, None, ADDRESS, 'SO', 'ACTIVE', '2501234567')
]


@pytest.mark.parametrize('desc,valid,org,individual,address,type,status,phone', TEST_DATA_OWNER)
def test_owner(desc, valid, org, individual, address, type, status, phone):
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
    data['status'] = status
    if phone:
        data['phoneNumber'] = phone

    is_valid, errors = validate(data, 'owner', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
