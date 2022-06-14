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
import pytest

from registry_schemas import validate


TEST_VALID_ALL = {
    'mhrNumber': '020000',
    'statusType': 'R',
    'clientReferenceId': 'T-0000001',
    'path': '/mhr/api/v1/registrations/020000',
    'createDateTime': '2021-06-03T22:58:45+00:00',
    'registeringParty': 'Bank of British Columbia',
    'inUserList': False
}
TEST_VALID_MINIMUM = {
    'mhrNumber': '020000',
    'statusType': 'R',
    'path': '/mhr/api/v1/registrations/020000',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_STATUS_TYPE = {
    'mhrNumber': '020000',
    'statusType': 'X',
    'path': '/mhr/api/v1/registrations/020000',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MHR_NUMBER = {
    'mhrNumber': '2020000',
    'statusType': 'R',
    'path': '/mhr/api/v1/registrations/020000',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MISSING_MHR_NUMBER = {
    'statusType': 'R',
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
    'statusType': 'R',
    'createDateTime': '2021-06-03T22:58:45+00:00'
}
TEST_INVALID_MISSING_CREATE_TS = {
    'mhrNumber': '020000',
    'statusType': 'R',
    'path': '/mhr/api/v1/registrations/020000'
}
TEST_EMPTY_JSON = {
}

# testdata pattern is ({description}, {is valid}, {data})
TEST_DATA = [
    ('All valid', True, TEST_VALID_ALL),
    ('Minimum valid', True, TEST_VALID_MINIMUM),
    ('Invalid status type', False, TEST_INVALID_STATUS_TYPE),
    ('Invalid mhr number length', False, TEST_INVALID_MHR_NUMBER),
    ('Invalid missing mhr num', False, TEST_INVALID_MISSING_MHR_NUMBER),
    ('Invalid missing status', False, TEST_INVALID_MISSING_STATUS),
    ('Invalid missing path', False, TEST_INVALID_MISSING_PATH),
    ('Invalid missing create_ts', False, TEST_INVALID_MISSING_CREATE_TS),
    ('No settings', False, TEST_EMPTY_JSON)
]


@pytest.mark.parametrize('desc,valid,data', TEST_DATA)
def test_registration_summary(desc, valid, data):
    """Assert that the schema is performing as expected for a registration summary."""
    is_valid, errors = validate(data, 'registrationSummary', 'mhr')

    if errors:
        # print(errors)
        for err in errors:
            print(err.message)

    assert is_valid == valid
