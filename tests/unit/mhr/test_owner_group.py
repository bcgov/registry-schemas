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
"""Test Suite to ensure the MHR owner group schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import OWNER_GROUP


LONG_INTEREST = '01234567890123456789'
# testdata pattern is ({desc}, {valid}, {group_id}, {owners}, {interest}, {numerator}, {type}, {status}, {denominator})
TEST_DATA_OWNER_GROUP = [
    ('Valid SOLE type', True, 1, True, None, 0, 'SOLE', None, None),
    ('Valid no group id', True, None, True, None, 0, 'SOLE', 'ACTIVE', None),
    ('Valid active', True, 1, True, None, 0, 'SOLE', 'ACTIVE', None),
    ('Valid exempt', True, 1, True, None, 0, 'SOLE', 'EXEMPT', None),
    ('Valid previous', True, 1, True, None, 0, 'SOLE', 'PREVIOUS', None),
    ('Valid JOINT type', True, 1, True, 'UNDIVIDED', 1, 'JOINT', 'ACTIVE', 2),
    ('Valid COMMON type', True, 1, True, LONG_INTEREST, 1, 'COMMON', 'ACTIVE', 2),
    ('Valid NA type', True, 1, True, 'UNDIVIDED', 1, 'NA', 'ACTIVE', 2),
    ('Valid SO type', True, 1, True, None, 0, 'SO', None, None),
    ('Valid JT type', True, 1, True, 'UNDIVIDED', 0, 'JT', 'ACTIVE', None),
    ('Valid TC type', True, 1, True, LONG_INTEREST, 1, 'TC', 'ACTIVE', 2),
    ('Invalid missing owner', False, 1, False, None, 0, 'SOLE', None, None),
    ('Invalid missing type', False, 1, True, None, 0, None, None, None),
    ('Invalid type', False, 1, True, None, 0, 'XX', None, None),
    ('Invalid status', False, 1, True, None, 0, 'JOINT', 'XX', None),
    ('Invalid numerator', False, 1, True, None, -1, None, None, 2),
    ('Invalid denominator', False, 1, True, None, 1, None, None, -1),
    ('Invalid interest too long', False, 1, True, LONG_INTEREST + 'X', 1, 'COMMON', None, None)
]


@pytest.mark.parametrize('desc,valid,group_id,owners,interest,numerator,type,status,denominator', TEST_DATA_OWNER_GROUP)
def test_owner_group(desc, valid, group_id, owners, interest, numerator, type, status, denominator):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(OWNER_GROUP)
    if not owners:
        del data['owners']
    if group_id:
        data['groupId'] = group_id
    else:
        del data['groupId']
    if interest:
        data['interest'] = interest
    else:
        del data['interest']
    if numerator:
        data['interestNumerator'] = numerator
    else:
        del data['interestNumerator']
    if denominator:
        data['interesDenominator'] = denominator
    else:
        del data['interestDenominator']
    if type:
        data['type'] = type
    else:
        del data['type']
    if status:
        data['status'] = status
    else:
        del data['status']

    is_valid, errors = validate(data, 'ownerGroup', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
