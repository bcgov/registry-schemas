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
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import ADDRESS, OWNER, PERSON_NAME


# testdata pattern is ({desc}, {valid}, {org}, {individual}, {address}, {type}, {status}, {phone}, {suffix})
LONG_ORG_NAME = '01234567890123456789012345678901234567890123456789012345678901234567890'
SUFFIX_MAX_LENGTH = '0123456789012345678901234567890123456789012345678901234567890123456789'
TEST_DATA_OWNER = [
    ('Valid org active SO', True, 'org name', None, ADDRESS, 'SOLE', 'ACTIVE', None, None),
    ('Valid org active SOLE', True, 'org name', None, ADDRESS, 'SOLE', 'ACTIVE', None, None),
    ('Valid ind exempt', True, None, PERSON_NAME, ADDRESS, 'SOLE', 'EXEMPT', None, 'suffix'),
    ('Valid JOINT type previous', True, 'org name', None, ADDRESS, 'JOINT', 'PREVIOUS', None, 'suffix'),
    ('Valid COMMON type', True, 'org name', None, ADDRESS, 'COMMON', 'ACTIVE', '2501234567', SUFFIX_MAX_LENGTH),
    ('Valid SO type', True, 'org name', None, ADDRESS, 'SO', 'ACTIVE', None, None),
    ('Valid JT type', True, 'org name', None, ADDRESS, 'JT', 'PREVIOUS', None, 'suffix'),
    ('Valid TC type', True, 'org name', None, ADDRESS, 'TC', 'ACTIVE', '2501234567', SUFFIX_MAX_LENGTH),
    ('Invalid missing owner', False, None, None, ADDRESS, 'SOLE', 'ACTIVE', '2501234567', 'suffix'),
    ('Invalid missing address', False, 'org name', None, None, 'COMMON', 'ACTIVE', '2501234567', 'suffix'),
    ('Invalid type', False, 'org name', None, ADDRESS, 'XX', 'ACTIVE', '2501234567', 'suffix'),
    ('Invalid status', False, 'org name', None, ADDRESS, 'SOLE', 'XXX', '2501234567', 'suffix'),
    ('Invalid phone too long', False, 'org name', None, ADDRESS, 'SOLE', 'ACTIVE', '2501234567          8', 'suffix'),
    ('Invalid org too long', False, LONG_ORG_NAME, None, ADDRESS, 'SOLE', 'ACTIVE', '2501234567', 'suffix'),
    ('Invalid suffix too long', False, LONG_ORG_NAME, None, ADDRESS, 'SOLE', 'ACTIVE', '2501234567',
     SUFFIX_MAX_LENGTH + 'X')
]
# testdata pattern is ({valid}, {party_type}, {party_desc})
TEST_DATA_OWNER_PARTY_TYPE = [
    (True, 'OWNER_BUS', None),
    (True, 'OWNER_IND', None),
    (True, None, None),
    (True, 'EXECUTOR', 'EXECUTOR'),
    (True, 'TRUSTEE', 'TRUSTEE'),
    (True, 'TRUST', 'TRUST'),
    (True, 'ADMINISTRATOR', 'ADMINISTRATOR'),
    (False, 'JUNK', None)
]
# testdata pattern is ({valid}, {party_type}, {cert_number}, {death_ts})
TEST_DATA_DEATH_CERTIFICATE = [
    (True, 'OWNER_BUS', None, None),
    (True, 'OWNER_IND', None, None),
    (True, 'OWNER_BUS', '01234567890123456789', '2021-02-21T18:56:00+00:00'),
    (True, 'OWNER_IND', '01234567890123456789', '2021-02-21T18:56:00+00:00'),
    (False, 'OWNER_BUS', '012345678901234567891', '2021-02-21T18:56:00+00:00'),
    (False, 'OWNER_IND', '012345678901234567891', '2021-02-21T18:56:00+00:00')
]


@pytest.mark.parametrize('desc,valid,org,individual,address,type,status,phone,suffix', TEST_DATA_OWNER)
def test_owner(desc, valid, org, individual, address, type, status, phone, suffix):
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
    if suffix:
        data['suffix'] = suffix

    is_valid, errors = validate(data, 'owner', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('valid,party_type,party_desc', TEST_DATA_OWNER_PARTY_TYPE)
def test_owner_party_type(valid, party_type, party_desc):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(OWNER)
    if party_type:
        data['partyType'] = party_type
    elif data.get('partyType'):
        del data['partyType']
    if party_desc:
        data['description'] = party_desc
    elif data.get('description'):
        del data['description']

    is_valid, errors = validate(data, 'owner', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('valid,party_type,cert_number,death_ts', TEST_DATA_DEATH_CERTIFICATE)
def test_owner_death_cert(valid, party_type, cert_number, death_ts):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(OWNER)
    if party_type:
        data['partyType'] = party_type
    if cert_number:
        data['deathCertificateNumber'] = cert_number
    elif data.get('deathCertificateNumber'):
        del data['deathCertificateNumber']
    if death_ts:
        data['deathDateTime'] = death_ts
    elif data.get('deathDateTime'):
        del data['deathDateTime']

    is_valid, errors = validate(data, 'owner', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
