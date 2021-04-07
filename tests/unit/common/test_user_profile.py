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
"""Test Suite to ensure the common user profile schema is valid."""
import pytest

from registry_schemas import validate


TEST_ALL_JSON = {
    'paymentConfirmationDialog': True,
    'selectConfirmationDialog': False,
    'defaultDropDowns': True,
    'defaultTableFilters': False
}
TEST_COMBO_JSON = {
    'paymentConfirmationDialog': True,
    'selectConfirmationDialog': False
}
TEST_PAYMENT_JSON = {
    'paymentConfirmationDialog': True
}
TEST_SELECT_JSON = {
    'selectConfirmationDialog': False
}
TEST_DROPDOWN_JSON = {
    'defaultDropDowns': True
}
TEST_FILTER_JSON = {
    'defaultTableFilters': False
}
TEST_EMPTY_JSON = {
}
TEST_UNKNOWN_JSON = {
    'unknown': 'xxxx'
}
TEST_INVALID_TYPE_JSON = {
    'selectConfirmationDialog': 'wrong'
}

# testdata pattern is ({description}, {is valid}, {data})
TEST_DATA = [
    ('All settings', True, TEST_ALL_JSON),
    ('2 settings', True, TEST_COMBO_JSON),
    ('Just payment', True, TEST_PAYMENT_JSON),
    ('Just search select', True, TEST_SELECT_JSON),
    ('Just dropdown', True, TEST_DROPDOWN_JSON),
    ('Just table filter', True, TEST_FILTER_JSON),
    ('No settings', False, TEST_EMPTY_JSON),
    ('Unknown setting', False, TEST_UNKNOWN_JSON),
    ('Invalid type setting', False, TEST_INVALID_TYPE_JSON)
]


@pytest.mark.parametrize('desc,valid,data', TEST_DATA)
def test_user_profile(desc, valid, data):
    """Assert that the schema is performing as expected for a user profile."""
    is_valid, errors = validate(data, 'userProfile', 'common')

    if errors:
        # print(errors)
        for err in errors:
            print(err.message)

    assert is_valid == valid
