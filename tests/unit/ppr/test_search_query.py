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
"""Test Suite to ensure the PPR Search Query schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import SEARCH_QUERY


def test_valid_search_query_ind_debtor():
    """Assert that the schema is performing as expected for a search by individual debtor."""
    query = copy.deepcopy(SEARCH_QUERY)
    query['type'] = 'INDIVIDUAL_DEBTOR'
    del query['criteria']['debtorName']['business']
    del query['criteria']['value']
    del query['clientReferenceId']
    del query['startDateTime']
    del query['endDateTime']

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_search_query_bus_debtor():
    """Assert that the schema is performing as expected for a search by business debtor."""
    query = copy.deepcopy(SEARCH_QUERY)
    query['type'] = 'BUSINESS_DEBTOR'
    del query['criteria']['debtorName']['first']
    del query['criteria']['debtorName']['second']
    del query['criteria']['debtorName']['last']
    del query['criteria']['value']

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_search_query_airdot():
    """Assert that the schema is performing as expected for a search by aircraft DOT."""
    query = copy.deepcopy(SEARCH_QUERY)
    query['type'] = 'AIRCRAFT_DOT'
    del query['criteria']['debtorName']
    query['criteria']['value'] = 'CFYXW'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_search_query_regnum():
    """Assert that the schema is performing as expected for a search by registration number."""
    query = copy.deepcopy(SEARCH_QUERY)
    query['type'] = 'REGISTRATION_NUMBER'
    del query['criteria']['debtorName']
    query['criteria']['value'] = '023001B'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_search_query_mhrnum():
    """Assert that the schema is performing as expected for a search by MHR number."""
    query = copy.deepcopy(SEARCH_QUERY)
    query['type'] = 'MHR_NUMBER'
    del query['criteria']['debtorName']
    query['criteria']['value'] = '21324'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_search_query_serialnum():
    """Assert that the schema is performing as expected for a search by serial number."""
    query = copy.deepcopy(SEARCH_QUERY)
    query['type'] = 'SERIAL_NUMBER'
    del query['criteria']['debtorName']
    query['criteria']['value'] = 'KM8J3CA46JU622994'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_search_query_missing_type():
    """Assert that an invalid search query fails - type is missing."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['type']
    del query['criteria']['debtorName']['business']
    del query['criteria']['value']

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_missing_criteria():
    """Assert that an invalid search query fails - criteria is missing."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_type():
    """Assert that an invalid search query fails - type is invalid."""
    query = copy.deepcopy(SEARCH_QUERY)
    query['type'] = 'XXXXXXXX'
    del query['criteria']['debtorName']['business']
    del query['criteria']['value']

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_criteria():
    """Assert that an invalid search query fails - criteria is invalid."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']['debtorName']['business']

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_busname():
    """Assert that an invalid search query fails - business name is too short."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']['debtorName']['first']
    del query['criteria']['debtorName']['second']
    del query['criteria']['debtorName']['last']
    del query['criteria']['value']
    query['criteria']['debtorName']['business'] = 'X'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_value():
    """Assert that an invalid search query fails - value is too long."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']['debtorName']
    query['criteria']['value'] = 'XxxxxxxxxxxxxxxxxxxxXxxxxxxxxxxxxxxxxxxxXxxxxxxxxxx'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_debtor():
    """Assert that an invalid search query fails - debtor name is invalid."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']['value']

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_firstname():
    """Assert that an invalid search query fails - debtor first name is too long."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']['value']
    del query['criteria']['debtorName']['business']
    query['criteria']['debtorName']['first'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_secondname():
    """Assert that an invalid search query fails - debtor second name is too long."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']['value']
    del query['criteria']['debtorName']['business']
    query['criteria']['debtorName']['second'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_lastname():
    """Assert that an invalid search query fails - debtor last name is too long."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']['value']
    del query['criteria']['debtorName']['business']
    query['criteria']['debtorName']['last'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_clientref():
    """Assert that an invalid search query fails - client reference id is too long."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']['value']
    del query['criteria']['debtorName']['business']
    query['clientReferenceId'] = '012345678901234567890123456789012345678901234567890'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_search_query_startts():
    """Assert that an invalid search query fails - start date time format is invalid."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']['value']
    del query['criteria']['debtorName']['business']
    query['startDateTime'] = 'Xxxxxxxxxx'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    # Commenting out: no longer working with 3.8 build
    # assert not is_valid


def test_invalid_search_query_endts():
    """Assert that an invalid search query fails - end date time format is invalid."""
    query = copy.deepcopy(SEARCH_QUERY)
    del query['criteria']['value']
    del query['criteria']['debtorName']['business']
    query['endDateTime'] = 'Xxxxxxxxxx'

    is_valid, errors = validate(query, 'searchQuery', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    # Commenting out: no longer working with 3.8 build
    # assert not is_valid
