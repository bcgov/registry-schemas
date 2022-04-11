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
"""Test Suite to ensure the MHR Search Detail Result schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import SEARCH_DETAIL_RESULT


SEARCH_DETAIL_RESULT_EMPTY = {
  'searchDateTime': '2020-05-14T21:08:32+00:00',
  'totalResultsSize': 1,
  'searchQuery': {
    'type': 'MHR_NUMBER',
    'criteria': {
      'value': '001234'
    }
  },
  'selected': [],
  'payment': {
    'receipt': '/pay/api/v1/payment-requests/2198743/receipts',
    'invoiceId': '2198743'
  },
  'details': []
}
SEARCH_DETAIL_RESULT_NONE = {
  'searchDateTime': '2020-05-14T21:08:32+00:00',
  'totalResultsSize': 1,
  'searchQuery': {
    'type': 'MHR_NUMBER',
    'criteria': {
      'value': '001234'
    }
  },
  'selected': [],
  'payment': {
    'receipt': '/pay/api/v1/payment-requests/2198743/receipts',
    'invoiceId': '2198743'
  }
}


# testdata pattern is ({desc}, {is valid}, {result_data})
TEST_DATA_RESULT_VALID = [
    ('Valid results', True, SEARCH_DETAIL_RESULT),
    ('Valid no results', True, SEARCH_DETAIL_RESULT_NONE),
    ('Valid empty results', True, SEARCH_DETAIL_RESULT_EMPTY)
]
# testdata pattern is ({desc}, {has_ts}, {has_total}, {has_query}, {has_payment})
TEST_DATA_RESULT_INVALID = [
    ('No search TS', False, True, True, True),
    ('No total results', True, False, True, True),
    ('No search query', True, True, False, True),
    ('No payment', True, True, True, False)
]


@pytest.mark.parametrize('desc, valid, result_data', TEST_DATA_RESULT_VALID)
def test_search_results_valid(desc, valid, result_data):
    """Assert that the schema is performing as expected for a valid search detail result."""
    is_valid, errors = validate(result_data, 'searchDetailResult', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc, has_ts, has_total, has_query, has_payment', TEST_DATA_RESULT_INVALID)
def test_detail_results_invalid(desc, has_ts, has_total, has_query, has_payment):
    """Assert that the schema is performing as expected for a search detail result with a missing required property."""
    result = copy.deepcopy(SEARCH_DETAIL_RESULT)
    if not has_ts:
        del result['searchDateTime']
    if not has_total:
        del result['totalResultsSize']
    if not has_query:
        del result['searchQuery']
    if not has_payment:
        del result['payment']

    is_valid, errors = validate(result, 'searchDetailResult', 'mhr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
