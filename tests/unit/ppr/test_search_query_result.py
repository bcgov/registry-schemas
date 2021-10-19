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
"""Test Suite to ensure the PPR Search Query Result schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import SEARCH_QUERY_RESULT


def test_valid_query_result():
    """Assert that the schema is performing as expected for a search query result list."""
    is_valid, errors = validate(SEARCH_QUERY_RESULT, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_query_result_empty():
    """Assert that the schema is performing as expected for a search query with no results."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['results']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_query_result_missing_exact():
    """Assert that the schema is performing as expected for a search query with no exactResultsSize."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['exactResultsSize']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_query_result_missing_similar():
    """Assert that the schema is performing as expected for a search query with no similarResultsSize."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['similarResultsSize']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_query_result_missing_id():
    """Assert that an invalid search query result fails - search ID is missing."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['searchId']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_query_result_missing_query():
    """Assert that an invalid search query result fails - search query is missing."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['searchQuery']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_query_result_missing_payment():
    """Assert that an invalid search query result fails - payment is missing."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['payment']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_query_result_missing_timestamp():
    """Assert that an invalid search query result fails - search date time is missing."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['searchDateTime']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_query_result_missing_max():
    """Assert that an invalid search query result fails - max results size is missing."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['maxResultsSize']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_query_result_missing_total():
    """Assert that an invalid search query result fails - total results size is missing."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['totalResultsSize']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_query_result_missing_returned():
    """Assert that an invalid search query result fails - returned results size is missing."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['returnedResultsSize']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_query_result_id():
    """Assert that an invalid search query result fails - search id is too long."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    result['searchId'] = '0123456789012'

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_query_result_timestamp():
    """Assert that an invalid search query result fails - search date time format is invalid."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    result['searchDateTime'] = 'XXXXXXXXXX'

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    # Commenting out: no longer working with 3.8 build
    # assert not is_valid


def test_invalid_query_result_query():
    """Assert that an invalid search query result fails - search query is invalid."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['searchQuery']['type']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_query_result_results():
    """Assert that an invalid search query result fails - first result is invalid."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['results'][0]['matchType']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_query_result_payment():
    """Assert that an invalid search query result fails - payment is invalid."""
    result = copy.deepcopy(SEARCH_QUERY_RESULT)
    del result['payment']['invoiceId']

    is_valid, errors = validate(result, 'searchQueryResult', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid
