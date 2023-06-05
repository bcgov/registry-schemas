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
"""Test Suite to ensure the MHR registration summary schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import REGISTRATION_SUMMARY


TEST_VALID_ALL = {
    'mhrNumber': '020000',
    'registrationDescription': 'Manufactured Home Registration',
    'username': 'Michael Scott',
    'statusType': 'ACTIVE',
    'clientReferenceId': 'T-0000001',
    'path': '/mhr/api/v1/registrations/020000',
    'createDateTime': '2021-06-03T22:58:45+00:00',
    'submittingParty': 'Bank of British Columbia',
    'ownerNames': 'GRAEME THOMAS CUNNINGHAM, NEIL MARTIN FOLEY',
    'inUserList': False,
    'lienRegistrationType': 'SA',
    'hasCaution': False,
    'expireDays': 0
}
TEST_VALID_MINIMUM = {
    'mhrNumber': '020000',
    'statusType': 'ACTIVE',
    'path': '/mhr/api/v1/registrations/020000',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MHR_NUMBER = {
    'mhrNumber': '2020000',
    'statusType': 'ACTIVE',
    'path': '/mhr/api/v1/registrations/020000',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MISSING_MHR_NUMBER = {
    'statusType': 'ACTIVE',
    'path': '/mhr/api/v1/registrations/020000',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MISSING_STATUS = {
    'mhrNumber': '020000',
    'path': '/mhr/api/v1/registrations/020000',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MISSING_PATH = {
    'mhrNumber': '020000',
    'statusType': 'ACTIVE',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MISSING_CREATE_TS = {
    'mhrNumber': '020000',
    'statusType': 'ACTIVE',
    'path': '/mhr/api/v1/registrations/020000'
}
TEST_EMPTY_JSON = {
}

# testdata pattern is ({description}, {is valid}, {data}, {status})
TEST_DATA = [
    ('All valid', True, TEST_VALID_ALL, 'ACTIVE'),
    ('Minimum valid', True, TEST_VALID_MINIMUM, 'ACTIVE'),
    ('Valid EXEMPT', True, TEST_VALID_MINIMUM, 'EXEMPT'),
    ('Valid HISTORICAL', True, TEST_VALID_MINIMUM, 'HISTORICAL'),
    ('Valid FROZEN', True, TEST_VALID_MINIMUM, 'FROZEN'),
    ('Invalid status type', False, TEST_VALID_MINIMUM, 'X'),
    ('Invalid mhr number length', False, TEST_INVALID_MHR_NUMBER, 'ACTIVE'),
    ('Invalid missing mhr num', False, TEST_INVALID_MISSING_MHR_NUMBER, 'ACTIVE'),
    ('Invalid missing status', False, TEST_INVALID_MISSING_STATUS, None),
    ('Invalid missing path', False, TEST_INVALID_MISSING_PATH, 'ACTIVE'),
    ('Invalid missing create_ts', False, TEST_INVALID_MISSING_CREATE_TS, 'ACTIVE'),
    ('No settings', False, TEST_EMPTY_JSON, None)
]

# testdata pattern is ({desc}, {valid}, {type})
TEST_DATA_REGISTRATION_TYPE = [
    ('Valid DECAL_REPLACE', True, 'DECAL_REPLACE'),
    ('Valid EXEMPTION_RES', True, 'EXEMPTION_RES'),
    ('Valid EXEMPTION_NON_RES', True, 'EXEMPTION_NON_RES'),
    ('Valid MHREG', True, 'MHREG'),
    ('Valid MHREG_CONVERSION', True, 'MHREG_CONVERSION'),
    ('Valid PERMIT', True, 'PERMIT'),
    ('Valid PERMIT_EXTENSION', True, 'PERMIT_EXTENSION'),
    ('Valid TRANS', True, 'TRANS'),
    ('Valid TRANS_AFFIDAVIT', True, 'TRANS_AFFIDAVIT'),
    ('Valid TRANS_ADMIN', True, 'TRANS_ADMIN'),
    ('Valid TRANS_WILL', True, 'TRANS_WILL'),
    ('Valid TRAND', True, 'TRAND'),
    ('Valid REG_STAFF_ADMIN', True, 'REG_STAFF_ADMIN'),
    ('Invalid', False, 'JUNKJ')
]
# testdata pattern is ({description}, {is valid}, {data})
TEST_DATA_EXPIRY = [
    ('Valid 0', True, 0),
    ('Valid > 0', True, 90),
    ('Valid < 0', True, -9999),
    ('Invalid data type', False, 'junk')
]


@pytest.mark.parametrize('desc,valid,data,status', TEST_DATA)
def test_registration_summary(desc, valid, data, status):
    """Assert that the schema is performing as expected for a registration summary."""
    if status:
        data['statusType'] = status
    is_valid, errors = validate(data, 'registrationSummary', 'mhr')

    if errors:
        # print(errors)
        for err in errors:
            print(err.message)

    assert is_valid == valid


@pytest.mark.parametrize('desc,valid,reg_type', TEST_DATA_REGISTRATION_TYPE)
def test_registration_summary_reg_type(desc, valid, reg_type):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(REGISTRATION_SUMMARY)
    data[0]['registrationType'] = reg_type

    is_valid, errors = validate(data[0], 'registrationSummary', 'mhr')

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,value', TEST_DATA_EXPIRY)
def test_registration_summary_expiry(desc, valid, value):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(TEST_VALID_ALL)
    data['expireDays'] = value

    is_valid, errors = validate(data, 'registrationSummary', 'mhr')

    if valid:
        assert is_valid
    else:
        assert not is_valid
