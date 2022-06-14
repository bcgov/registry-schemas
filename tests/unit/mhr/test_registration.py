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
"""Test Suite to ensure the MHR registration schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import REGISTRATION


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
    'birthDate': '1986-12-01T19:20:20-08:00',
    'phoneNumber': '6042314598'
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
    'birthDate': '1986-12-01T19:20:20-08:00',
    'phoneNumber': '2314598'
}
PPR_REG_VALID = [
    {
        'reg_data': 'any data allowed'
    }
]
PPR_REG_EMPTY = []

LONG_CLIENT_REF = '01234567890123456789012345678901234567890'

# testdata pattern is ({desc},{valid},{mhr},{status},{rev},{decv},{haso},{hasl},{hasd},{hasn},{hasdt},{hasp})
TEST_DATA_REG = [
    ('Valid request', True, None, None, 'ref', '50000.00', True, True, True, True, False, False),
    ('Valid response', True, '003456', 'R', 'ref', '50000.00', True, True, True, True, True, True),
    ('Valid no ref', True, None, None, None, '50000.00', True, True, True, True, False, False),
    ('Valid no declared value', True, None, None, 'ref', None, True, True, True, True, False, False),
    ('Valid no notes', True, None, None, 'ref', '50000.00', True, True, True, False, False, False),
    ('Invalid no owners', False, None, None, 'ref', '50000.00', False, True, True, True, False, False),
    ('Invalid no location', False, None, None, 'ref', '50000.00', True, False, True, True, False, False),
    ('Invalid no description', False, None, None, 'ref', '50000.00', True, True, False, True, False, False),
    ('Invalid mhr num too long', False, '1234567', None, 'ref', '50000.00', True, True, True, True, False, False),
    ('Invalid status', False, None, 'X', 'ref', '50000.00', True, True, True, True, False, False),
    ('Invalid ref too long', False, None, None, LONG_CLIENT_REF, '50000.00', True, True, True, True, False, False),
    ('Invalid declared val too long', False, None, None, 'ref', '1234567890.00', True, True, True, True, False, False)
]

# testdata pattern is ({desc},{valid},{reg_party})
TEST_DATA_REG_PARTY = [
    ('Valid request with party', True, PARTY_VALID),
    ('Invalid request invalid party', False, PARTY_INVALID),
    ('Valid request no party', True, None)
]

# testdata pattern is ({desc},{valid},{ppr_registrations})
TEST_DATA_PPR_REGISTRATIONS = [
    ('Valid request with ppr registrations', True, PPR_REG_VALID),
    ('Valid request empty ppr registrations', True, PPR_REG_EMPTY),
    ('Valid request no ppr registrations', True, None)
]


@pytest.mark.parametrize('desc,valid,mhr,status,ref,decv,haso,hasl,hasd,hasn,hasdt,hasp', TEST_DATA_REG)
def test_registration(desc, valid, mhr, status, ref, decv, haso, hasl, hasd, hasn, hasdt, hasp):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(REGISTRATION)
    if not haso:
        del data['owners']
    if not hasl:
        del data['location']
    if not hasd:
        del data['description']
    if not hasn:
        del data['notes']
    if not hasdt:
        del data['createDateTime']
    if not hasp:
        del data['payment']
    if not mhr:
        del data['mhrNumber']
    else:
        data['mhrNumber'] = mhr
    if not status:
        del data['status']
    else:
        data['status'] = status
    if not ref:
        del data['clientReferenceId']
    else:
        data['clientReferenceId'] = ref
    if not decv:
        del data['declaredValue']
    else:
        data['declaredValue'] = decv

    is_valid, errors = validate(data, 'registration', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,reg_party', TEST_DATA_REG_PARTY)
def test_registration_reg_party(desc, valid, reg_party):
    """Assert that the schema is performing as expected with a registering party."""
    data = copy.deepcopy(REGISTRATION)
    if reg_party:
        data['registeringParty'] = reg_party

    is_valid, errors = validate(data, 'registration', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,ppr_registrations', TEST_DATA_PPR_REGISTRATIONS)
def test_registration_ppr_registrations(desc, valid, ppr_registrations):
    """Assert that the schema is performing as expected with a registering party."""
    data = copy.deepcopy(REGISTRATION)
    if ppr_registrations:
        data['pprRegistrations'] = ppr_registrations

    is_valid, errors = validate(data, 'registration', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
