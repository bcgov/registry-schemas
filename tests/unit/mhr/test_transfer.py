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
"""Test Suite to ensure the MHR transfer (tranfer of sale) schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import TRANSFER


PARTY_VALID = {
    'personName': {
        'first': 'Michael',
        'middle': 'J',
        'last': 'Smith'
    },
    'address': {
        'street': '520 Johnson St',
        'city': 'Victoria',
        'region': 'BC',
        'country': 'CA',
        'postalCode': 'V8S 2V4'
    },
    'emailAddress': 'msmith@gmail.com',
    'phoneNumber': '6042314598',
    'phoneExtension': '546'
}
PARTY_INVALID = {
    'personName': {
        'first': 'Michael',
        'middle': 'J',
        'last': 'Smith'
    },
    'address': {
        'street': '520 Johnson St',
        'city': 'Victoria',
        'region': 'BC',
        'country': 'CA',
        'postalCode': 'V8S 2V4'
    },
    'emailAddress': 'msmith@gmail.com',
    'phoneNumber': '2314598'
}
LONG_CLIENT_REF = '012345678901234567890123456789012345678901234567890'
MAX_CONSIDERATION = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'

# testdata pattern is ({desc},{valid},{sub_party},{add},{delete},{is_request},{client_ref})
TEST_DATA = [
    ('Valid request', True, PARTY_VALID, True, True, True, None),
    ('Valid response', True, PARTY_VALID, True, True, False, '1234'),
    ('Invalid client ref', False, PARTY_VALID, True, True, True, LONG_CLIENT_REF),
    ('Invalid sub party', False, PARTY_INVALID, True, True, True, '1234'),
    ('Missing sub party', False, None, True, True, True, '1234'),
    ('Invalid missing add', False, PARTY_VALID, False, True, True, '1234'),
    ('Invalid missing delete', False, PARTY_VALID, True, False, True, ''),
]
# testdata pattern is ({desc},{valid},{declared},{consid},{tran_dt},{own_land})
TEST_DATA_DETAILS = [
    ('Valid all', True, 60000, MAX_CONSIDERATION, '2022-09-20T10:39:03-07:53', False),
    ('Valid none', True, None, None, None, None),
    ('Invalid declared', False, 'xxxx', MAX_CONSIDERATION, '2022-09-20T10:39:03-07:53', False),
    ('Invalid consideration', False, 60000, MAX_CONSIDERATION + 'X', '2022-09-20T10:39:03-07:53', False),
    ('Invalid date', False, 60000, MAX_CONSIDERATION, 'XXXXXXXX', False)
]


@pytest.mark.parametrize('desc,valid,sub_party,add,delete,is_request,client_ref', TEST_DATA)
def test_transfer(desc, valid, sub_party, add, delete, is_request, client_ref):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(TRANSFER)
    if sub_party:
        data['submittingParty'] = sub_party
    else:
        del data['submittingParty']
    if client_ref:
        data['clientReferenceId'] = client_ref
    else:
        del data['clientReferenceId']
    if is_request:
        del data['createDateTime']
        del data['payment']
        del data['mhrNumber']
        del data['documentId']
        del data['documentDescription']
    if not add:
        del data['addOwnerGroups']
    if not delete:
        del data['deleteOwnerGroups']

    is_valid, errors = validate(data, 'transfer', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,declared,consideration,tran_dt,own_land', TEST_DATA_DETAILS)
def test_transfer_details(desc, valid, declared, consideration, tran_dt, own_land):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(TRANSFER)
    if declared:
        data['declaredValue'] = declared
    else:
        del data['declaredValue']
    if consideration:
        data['consideration'] = consideration
    else:
        del data['consideration']
    if tran_dt:
        data['transferDate'] = tran_dt
    else:
        del data['transferDate']
    if own_land:
        data['ownLand'] = own_land
    else:
        del data['ownLand']

    is_valid, errors = validate(data, 'transfer', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
