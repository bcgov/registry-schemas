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
"""Test Suite to ensure the MHR Search Query Result schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import SEARCH_QUERY_RESULT


SEARCH_QUERY_RESULT_MIN1 = {
  'searchId': '1294371',
  'searchDateTime': '2020-05-14T21:16:32+00:00',
  'returnedResultsSize': 0,
  'totalResultsSize': 0,
  'maxResultsSize': 1000,
  'searchQuery': {
    'type': 'MHR_NUMBER',
    'criteria': {
      'value': '001234'
    }
  }
}
SEARCH_QUERY_RESULT_MIN2 = {
  'searchId': '1294371',
  'searchDateTime': '2020-05-14T21:16:32+00:00',
  'returnedResultsSize': 1,
  'totalResultsSize': 1,
  'maxResultsSize': 1000,
  'searchQuery': {
    'type': 'MHR_NUMBER',
    'criteria': {
      'value': '001234'
    }
  },
  'results': []
}

# testdata pattern is ({desc}, {is valid}, {result_data})
TEST_DATA_RESULT_VALID = [
    ('Valid results', True, SEARCH_QUERY_RESULT),
    ('Valid no results', True, SEARCH_QUERY_RESULT_MIN1),
    ('Valid empty results', True, SEARCH_QUERY_RESULT_MIN2)
]
# testdata pattern is ({desc}, {has_id}, {has_ts}, {has_max}, {has_total}, {has_returned}, {has_query})
TEST_DATA_RESULT_INVALID = [
    ('No search ID', False, True, True, True, True, True),
    ('No search TS', True, False, True, True, True, True),
    ('No max results', True, True, False, True, True, True),
    ('No total results', True, True, True, False, True, True),
    ('No returned results', True, True, True, True, False, True),
    ('No search query', True, True, True, True, True, False)
]


@pytest.mark.parametrize('desc, valid, result_data', TEST_DATA_RESULT_VALID)
def test_search_results_valid(desc, valid, result_data):
    """Assert that the schema is performing as expected for a valid search query result."""
    is_valid, errors = validate(result_data, 'searchQueryResult', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc, has_id, has_ts, has_max, has_total, has_returned, has_query', TEST_DATA_RESULT_INVALID)
def test_query_results_invalid(desc, has_id, has_ts, has_max, has_total, has_returned, has_query):
    """Assert that the schema is performing as expected for a search result with a missing required property."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    if not has_id:
        del result['searchId']
    if not has_ts:
        del result['searchDateTime']
    if not has_max:
        del result['maxResultsSize']
    if not has_total:
        del result['totalResultsSize']
    if not has_returned:
        del result['returnedResultsSize']
    if not has_query:
        del result['searchQuery']

    is_valid, errors = validate(result, 'searchQueryResult', 'mhr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
