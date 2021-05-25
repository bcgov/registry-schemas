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
"""Test Suite to ensure the PPR party schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.common import PARTY


def test_valid_party_person():
    """Assert that the schema is performing as expected for an individual party."""
    is_valid, errors = validate(PARTY, 'party', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_party_business():
    """Assert that the schema is performing as expected for a business party."""
    party = copy.deepcopy(PARTY)
    party['businessName'] = 'BUSINESS NAME'
    del party['personName']
    is_valid, errors = validate(party, 'party', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_party_code():
    """Assert that the schema is performing as expected for a party code."""
    party = copy.deepcopy(PARTY)
    party['code'] = '1234'
    del party['personName']
    del party['address']
    del party['emailAddress']
    is_valid, errors = validate(party, 'party', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_party_missing_lastname():
    """Assert that an invalid party fails - person last name is missing."""
    party = copy.deepcopy(PARTY)
    del party['personName']['last']

    is_valid, errors = validate(party, 'party', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_party_birthdate():
    """Assert that an invalid party fails - birthdate format invalid."""
    party = copy.deepcopy(PARTY)
    party['birthDate'] = 'XXXXXXX'

    is_valid, errors = validate(party, 'party', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_party_missing_person():
    """Assert that an invalid party fails - personName is missing."""
    party = copy.deepcopy(PARTY)
    del party['personName']

    is_valid, errors = validate(party, 'party', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_party_missing_person_address():
    """Assert that an invalid party fails - person address is missing."""
    party = copy.deepcopy(PARTY)
    del party['address']
    del party['partyId']

    is_valid, errors = validate(party, 'party', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_party_missing_business_address():
    """Assert that an invalid party fails - business address is missing."""
    party = copy.deepcopy(PARTY)
    del party['personName']
    del party['address']
    del party['partyId']
    party['businessName'] = 'BUSINESS NAME'

    is_valid, errors = validate(party, 'party', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
