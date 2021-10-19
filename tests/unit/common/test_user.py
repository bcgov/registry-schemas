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
"""Test Suite to ensure the common user schema is valid."""
import pytest

from registry_schemas import validate


TEST_ALL_JSON = {
    'creationDate': '2021-04-01T16:20:20+00:00',
    'username': 'bcsc/avyw3cbumorr91k7f5uq2i3mzcqrm4av',
    'sub': 'fd362600-x234-9115-c427-fed859c6d093',
    'iss': 'https://dev.oidc.gov.bc.ca/auth/realms/fcf0kpqr',
    'firstname': 'Michael',
    'lastname': 'Smith',
    'email': 'msmith@gmail.com',
    'accountId': '12345'
}
TEST_REQUIRED_JSON = {
    'username': 'bcsc/avyw3cbumorr91k7f5uq2i3mzcqrm4av',
    'sub': 'fd362600-x234-9115-c427-fed859c6d093'
}
TEST_OPTIONAL_JSON = {
    'creationDate': '2021-04-01T16:20:20+00:00',
    'username': 'bcsc/avyw3cbumorr91k7f5uq2i3mzcqrm4av',
    'sub': 'fd362600-x234-9115-c427-fed859c6d093',
    'iss': 'https://dev.oidc.gov.bc.ca/auth/realms/fcf0kpqr',
    'firstname': 'Michael',
    'lastname': 'Smith'
}
TEST_EMPTY_JSON = {
}
TEST_MISSING_USERNAME_JSON = {
    'sub': 'fd362600-x234-9115-c427-fed859c6d093'
}
TEST_MISSING_SUB_JSON = {
    'username': 'bcsc/avyw3cbumorr91k7f5uq2i3mzcqrm4av'
}
TEST_SUB_TOO_LONG_JSON = {
    'username': 'bcsc/avyw3cbumorr91k7f5uq2i3mzcqrm4av',
    'sub': '0123456789012345678901234567890123456'
}
TEST_CREATE_FORMAT_JSON = {
    'creationDate': '2021-04-01Txx:20:20+00:00',
    'username': 'bcsc/avyw3cbumorr91k7f5uq2i3mzcqrm4av',
    'sub': 'fd362600-x234-9115-c427-fed859c6d093'
}
TEST_EMAIL_FORMAT_JSON = {
    'creationDate': '2021-04-01T16:20:20+00:00',
    'username': 'bcsc/avyw3cbumorr91k7f5uq2i3mzcqrm4av',
    'sub': 'fd362600-x234-9115-c427-fed859c6d093',
    'iss': 'https://dev.oidc.gov.bc.ca/auth/realms/fcf0kpqr',
    'firstname': 'Michael',
    'lastname': 'Smith',
    'email': 'msmith'
}

# testdata pattern is ({description}, {is valid}, {data})
TEST_DATA = [
    ('All properties', True, TEST_ALL_JSON),
    ('Just required properties', True, TEST_REQUIRED_JSON),
    ('Required with some optional', True, TEST_OPTIONAL_JSON),
    ('No settings', False, TEST_EMPTY_JSON),
    ('Reqired username missing', False, TEST_MISSING_USERNAME_JSON),
    ('Reqired sub missing', False, TEST_MISSING_SUB_JSON),
    ('Sub value too long', False, TEST_SUB_TOO_LONG_JSON),
    # ('Create date time format invalid', False, TEST_CREATE_FORMAT_JSON),
    ('Email format invalid', False, TEST_EMAIL_FORMAT_JSON)
]


@pytest.mark.parametrize('desc,valid,data', TEST_DATA)
def test_user(desc, valid, data):
    """Assert that the schema is performing as expected for a user."""
    is_valid, errors = validate(data, 'user', 'common')

    if errors:
        # print(errors)
        for err in errors:
            print(err.message)

    assert is_valid == valid
