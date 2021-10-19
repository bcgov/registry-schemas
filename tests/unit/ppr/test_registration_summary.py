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
"""Test Suite to ensure the PPR registration summary schema is valid."""
import pytest

from registry_schemas import validate


TEST_VALID_ALL = {
    'registrationNumber': '9000100B',
    'baseRegistrationNumber': '9000100B',
    'statusType': 'ACT',
    'registrationType': 'SA',
    'registrationDescription': 'PPSA SECURITY AGREEMENT',
    'registrationClass': 'PPSALIEN',
    'expireDays': 1422,
    'clientReferenceId': 'T-0000001',
    'path': '/ppr/api/v1/financing-statements/9000100B',
    'createDateTime': '2021-06-03T22:58:45+00:00',
    'lastUpdateDateTime': '2021-06-03T23:03:45+00:00',
    'registeringParty': 'Bank of British Columbia',
    'securedParties': 'Bank of British Columbia',
    'registeringName': 'Michael Smith',
    'inUserList': False
}
TEST_VALID_MINIMUM = {
    'registrationNumber': '9000100B',
    'registrationType': 'SA',
    'registrationClass': 'PPSALIEN',
    'path': '/ppr/api/v1/financing-statements/9000100B',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_STATUS_TYPE = {
    'registrationNumber': '9000100B',
    'baseRegistrationNumber': '9000100B',
    'statusType': 'XXX',
    'registrationType': 'SA',
    'registrationDescription': 'PPSA SECURITY AGREEMENT',
    'registrationClass': 'PPSALIEN',
    'expireDays': 1422,
    'clientReferenceId': 'T-0000001',
    'path': '/ppr/api/v1/financing-statements/9000100B',
    'createDateTime': '2021-06-03T22:58:45+00:00',
    'lastUpdateDateTime': '2021-06-03T23:03:45+00:00',
    'registeringParty': 'Bank of British Columbia',
    'securedParties': 'Bank of British Columbia',
    'registeringName': 'Michael Smith',
    'inUserList': False
}
TEST_INVALID_REG_TYPE = {
    'registrationNumber': '9000100B',
    'baseRegistrationNumber': '9000100B',
    'statusType': 'ACT',
    'registrationType': 'SAX',
    'registrationDescription': 'PPSA SECURITY AGREEMENT',
    'registrationClass': 'PPSALIEN',
    'expireDays': 1422,
    'clientReferenceId': 'T-0000001',
    'path': '/ppr/api/v1/financing-statements/9000100B',
    'createDateTime': '2021-06-03T22:58:45+00:00',
    'lastUpdateDateTime': '2021-06-03T23:03:45+00:00',
    'registeringParty': 'Bank of British Columbia',
    'securedParties': 'Bank of British Columbia',
    'registeringName': 'Michael Smith',
    'inUserList': False
}
TEST_INVALID_REG_NUMBER = {
    'registrationNumber': '9000100BXXX',
    'baseRegistrationNumber': '9000100B',
    'statusType': 'ACT',
    'registrationType': 'SA',
    'registrationDescription': 'PPSA SECURITY AGREEMENT',
    'registrationClass': 'PPSALIEN',
    'expireDays': 1422,
    'clientReferenceId': 'T-0000001',
    'path': '/ppr/api/v1/financing-statements/9000100B',
    'createDateTime': '2021-06-03T22:58:45+00:00',
    'lastUpdateDateTime': '2021-06-03T23:03:45+00:00',
    'registeringParty': 'Bank of British Columbia',
    'securedParties': 'Bank of British Columbia',
    'registeringName': 'Michael Smith',
    'inUserList': False
}
TEST_INVALID_EXPIRE_DAYS = {
    'registrationNumber': '9000100B',
    'baseRegistrationNumber': '9000100B',
    'statusType': 'ACT',
    'registrationType': 'SA',
    'registrationDescription': 'PPSA SECURITY AGREEMENT',
    'registrationClass': 'PPSALIEN',
    'expireDays': 'wrong',
    'clientReferenceId': 'T-0000001',
    'path': '/ppr/api/v1/financing-statements/9000100B',
    'createDateTime': '2021-06-03T22:58:45+00:00',
    'lastUpdateDateTime': '2021-06-03T23:03:45+00:00',
    'registeringParty': 'Bank of British Columbia',
    'securedParties': 'Bank of British Columbia',
    'registeringName': 'Michael Smith',
    'inUserList': False
}
TEST_INVALID_MISSING_REG_NUM = {
    'registrationType': 'SA',
    'registrationClass': 'PPSALIEN',
    'path': '/ppr/api/v1/financing-statements/9000100B',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MISSING_REG_TYPE = {
    'registrationNumber': '9000100B',
    'registrationClass': 'PPSALIEN',
    'path': '/ppr/api/v1/financing-statements/9000100B',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MISSING_REG_CLASS = {
    'registrationNumber': '9000100B',
    'registrationType': 'SA',
    'path': '/ppr/api/v1/financing-statements/9000100B',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MISSING_PATH = {
    'registrationNumber': '9000100B',
    'registrationType': 'SA',
    'registrationClass': 'PPSALIEN',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MISSING_CREATE_TS = {
    'registrationNumber': '9000100B',
    'registrationType': 'SA',
    'registrationClass': 'PPSALIEN',
    'path': '/ppr/api/v1/financing-statements/9000100B'
}
TEST_EMPTY_JSON = {
}
TEST_UNKNOWN_JSON = {
    'registrationNumber': '9000100B',
    'registrationType': 'SA',
    'registrationClass': 'PPSALIEN',
    'path': '/ppr/api/v1/financing-statements/9000100B',
    'createDateTime': '2021-06-03T22:58:45+00:00',
    'unknown': 'xxxx'
}

# testdata pattern is ({description}, {is valid}, {data})
TEST_DATA = [
    ('All valid', True, TEST_VALID_ALL),
    ('Minimum valid', True, TEST_VALID_MINIMUM),
    ('Invalid status type', False, TEST_INVALID_STATUS_TYPE),
    ('Invalid reg type length', False, TEST_INVALID_REG_TYPE),
    ('Invalid reg number length', False, TEST_INVALID_REG_NUMBER),
    ('Invalid expiry days value', False, TEST_INVALID_EXPIRE_DAYS),
    ('Invalid missing reg num', False, TEST_INVALID_MISSING_REG_NUM),
    ('Invalid missing reg type', False, TEST_INVALID_MISSING_REG_TYPE),
    ('Invalid missing reg class', False, TEST_INVALID_MISSING_REG_CLASS),
    ('Invalid missing path', False, TEST_INVALID_MISSING_PATH),
    ('Invalid missing create_ts', False, TEST_INVALID_MISSING_CREATE_TS),
    ('No settings', False, TEST_EMPTY_JSON),
    ('Unknown ignored setting', True, TEST_UNKNOWN_JSON)
]


@pytest.mark.parametrize('desc,valid,data', TEST_DATA)
def test_registration_summary(desc, valid, data):
    """Assert that the schema is performing as expected for a registration summary."""
    is_valid, errors = validate(data, 'registrationSummary', 'ppr')

    if errors:
        # print(errors)
        for err in errors:
            print(err.message)

    assert is_valid == valid
