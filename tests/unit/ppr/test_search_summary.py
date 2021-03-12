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
"""Test Suite to ensure the PPR Search Summary schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import SEARCH_SUMMARY


def test_valid_search_summary():
    """Assert that the schema is performing as expected for a search summary list."""
    is_valid, errors = validate(SEARCH_SUMMARY, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_search_summary_exact():
    """Assert that the schema is performing as expected for an exact search summary list."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    del search[2]
    del search[1]

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_search_summary_missing_match():
    """Assert that an invalid search summary fails - match type is missing."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    del search[0]['matchType']

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_search_summary_missing_baseregnum():
    """Assert that an invalid search summary fails - base registration number is missing."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    del search[0]['baseRegistrationNumber']

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_valid_search_summary_missing_regtype():
    """Assert that a valid search summary with no registration type does not fail."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    del search[0]['registrationType']

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert is_valid


def test_valid_search_summary_missing_create():
    """Assert that an valid search summary with no create date time does not fail."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    del search[0]['createDateTime']

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert is_valid


def test_valid_search_summary_missing_selected():
    """Assert that an valid search summary with no create date time does not fail."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    del search[0]['selected']

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert is_valid


def test_invalid_search_summary_create():
    """Assert that an invalid search summary fails - create date time format is invalid."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    search[0]['createDateTime'] = 'XXXXXXXXXX'

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_search_summary_matchtype():
    """Assert that an invalid search summary fails - match type is invalid."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    search[0]['matchType'] = 'XXXXX'

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_search_summary_regtype():
    """Assert that an invalid search summary fails - registration type is invalid."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    search[0]['registrationType'] = 'XX'

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_search_summary_regnum():
    """Assert that an invalid search summary fails - registration number is too long."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    search[0]['registrationNumber'] = 'XXXXXXXXXXXXX'

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_search_summary_baseregnum():
    """Assert that an invalid search summary fails - base registration number is too long."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    search[0]['baseRegistrationNumber'] = 'XXXXXXXXXXXXX'

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_search_summary_debtor():
    """Assert that an invalid search summary fails - debtor business name is missing."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    del search[3]['debtor']['businessName']

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_invalid_search_summary_vehicle():
    """Assert that an invalid search summary fails - vehicle collateral type is missing."""
    search = copy.deepcopy(SEARCH_SUMMARY)
    del search[2]['vehicleCollateral']['type']

    is_valid, errors = validate(search, 'searchSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid
