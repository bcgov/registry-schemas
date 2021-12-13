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
"""Test Suite to ensure the common event tracking schema is valid."""
import pytest

from registry_schemas import validate


TEST_ALL_JSON = {
    'eventTrackingId': 123456,
    'keyId': 99923,
    'createDateTime': '2021-12-01T19:20:20-00:00',
    'type': 'EMAIL',
    'status': 200,
    'message': 'Error message',
    'emailAddress': 'msmith@gmail.com'
}
TEST_REQUIRED_JSON = {
    'keyId': 99923,
    'type': 'EMAIL'
}
TEST_OPTIONAL_JSON = {
    'keyId': 99923,
    'type': 'EMAIL',
    'status': 200,
    'message': 'Error message'
}
TEST_EMPTY_JSON = {
}
TEST_MISSING_KEYID_JSON = {
    'eventTrackingId': 123456,
    'createDateTime': '2021-12-01T19:20:20-00:00',
    'type': 'EMAIL',
    'status': 200,
    'message': 'Error message',
    'emailAddress': 'msmith@gmail.com'
}
TEST_MISSING_TYPE_JSON = {
    'eventTrackingId': 123456,
    'keyId': 99923,
    'createDateTime': '2021-12-01T19:20:20-00:00',
    'status': 200,
    'message': 'Error message',
    'emailAddress': 'msmith@gmail.com'
}
TEST_TYPE_TOO_LONG_JSON = {
    'eventTrackingId': 123456,
    'keyId': 99923,
    'createDateTime': '2021-12-01T19:20:20-00:00',
    'type': '012345678901234567890',
    'status': 200,
    'message': 'Error message',
    'emailAddress': 'msmith@gmail.com'
}
TEST_EMAIL_FORMAT_JSON = {
    'eventTrackingId': 123456,
    'keyId': 99923,
    'createDateTime': '2021-12-01T19:20:20-00:00',
    'type': 'EMAIL',
    'status': 200,
    'message': 'Error message',
    'emailAddress': 'msmith'
}

# testdata pattern is ({description}, {is valid}, {data})
TEST_DATA = [
    ('All properties', True, TEST_ALL_JSON),
    ('Just required properties', True, TEST_REQUIRED_JSON),
    ('Required with some optional', True, TEST_OPTIONAL_JSON),
    ('No settings', False, TEST_EMPTY_JSON),
    ('Reqired key id missing', False, TEST_MISSING_KEYID_JSON),
    ('Reqired type missing', False, TEST_MISSING_TYPE_JSON),
    ('Type value too long', False, TEST_TYPE_TOO_LONG_JSON),
    ('Email format invalid', False, TEST_EMAIL_FORMAT_JSON)
]


@pytest.mark.parametrize('desc,valid,data', TEST_DATA)
def test_event_tracking(desc, valid, data):
    """Assert that the schema is performing as expected for event tracking."""
    is_valid, errors = validate(data, 'eventTracking', 'common')

    if errors:
        # print(errors)
        for err in errors:
            print(err.message)

    assert is_valid == valid
