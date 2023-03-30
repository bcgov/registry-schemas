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
"""Test Suite to ensure the MHR Search Summary schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import SEARCH_SUMMARY


SEARCH_SUMMARY_MINIMAL = [
  {
    'mhrNumber': '001234',
    'createDateTime': '2020-02-21T18:56:20Z',
    'status': 'ACTIVE',
    'includeLienInfo': False,
    'activeCount': 1,
    'exemptCount': 0,
    'historicalCount': 0,
    'homeLocation': 'PENTICTON',
    'ownerName': {
      'first': 'James',
      'last': 'Smith'
    },
    'serialNumber': '52D70556',
    'baseInformation': {
      'year': 2018,
      'make': 'WATSON IND. (ALTA)',
      'model': 'DUCHESS'
    }
  }
]
SEARCH_SUMMARY_ORG = [
  {
    'mhrNumber': '001234',
    'status': 'ACTIVE',
    'baseInformation': {
      'year': 2018,
      'make': 'WATSON IND. (ALTA)',
      'model': 'DUCHESS'
    }
  }
]

# testdata pattern is ({status}, {is valid})
TEST_DATA_STATUS = [
    ('ACTIVE', True),
    ('EXEMPT', True),
    ('HISTORICAL', True),
    ('FROZEN', True),
    ('XX', False)
]
# testdata pattern is ({is valid}, {has_mrh}, {has_status}, {has_base})
TEST_DATA_MINIMAL = [
    (True, True, True, True),
    (False, False, True, True),
    (False, True, False, True),
    (False, True, True, False)
]
# testdata pattern is ({is valid}, {summary_data})
TEST_DATA_ALL = [
    (True, SEARCH_SUMMARY),
    (True, SEARCH_SUMMARY_ORG)
]
# testdata pattern is ({is valid}, {active}, {exempt}, {historical})
TEST_DATA_COUNTS = [
    (True, 0, 0, 0),
    (True, 1, 0, 0),
    (True, 0, 1, 0),
    (True, 0, 0, 1),
    (True, 1, 1, 1),
    (False, -1, 1, 1),
    (False, 1, 1, -1),
    (False, 1, -1, 1)
]


@pytest.mark.parametrize('valid, has_mhr, has_status, has_base', TEST_DATA_MINIMAL)
def test_search_summary_min(valid, has_mhr, has_status, has_base):
    """Assert the validation of a minimal response."""
    search = copy.deepcopy(SEARCH_SUMMARY_MINIMAL)
    if not has_mhr:
        del search[0]['mhrNumber']
    if not has_status:
        del search[0]['status']
    if not has_base:
        del search[0]['baseInformation']

    is_valid, errors = validate(search, 'searchSummary', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('status, valid', TEST_DATA_STATUS)
def test_search_summary_status(status, valid):
    """Assert the validation of all status types."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    search[0]['status'] = status

    is_valid, errors = validate(search, 'searchSummary', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('valid, summary_data', TEST_DATA_ALL)
def test_search_summary_all(valid, summary_data):
    """Assert the validation of all a response with all properties."""
    search = copy.deepcopy(summary_data)
    is_valid, errors = validate(search, 'searchSummary', 'mhr')

    if errors:
        for err in errors:
            print(err.message)
    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('valid, active, exempt, historical', TEST_DATA_COUNTS)
def test_search_summary_counts(valid, active, exempt, historical):
    """Assert the validation of a active and historical counts."""
    search = copy.deepcopy(SEARCH_SUMMARY_MINIMAL)
    search[0]['activeCount'] = active
    search[0]['exemptCount'] = exempt
    search[0]['historicalCount'] = historical

    is_valid, errors = validate(search, 'searchSummary', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
