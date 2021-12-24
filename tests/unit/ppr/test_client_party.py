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
"""Test Suite to ensure the PPR client party schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import CLIENT_PARTY


def test_valid_client_person():
    """Assert that the schema is performing as expected for an individual client party."""
    is_valid, errors = validate(CLIENT_PARTY, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_client_business():
    """Assert that the schema is performing as expected for a business client party."""
    party = copy.deepcopy(CLIENT_PARTY)
    party['businessName'] = 'BUSINESS NAME'
    del party['personName']
    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_client_contact_name():
    """Assert that an invalid client party fails - contact name is too long."""
    party = copy.deepcopy(CLIENT_PARTY)
    name = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789x'
    party['contact']['name'] = name

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_contact_areacode():
    """Assert that an invalid client party fails - contact area code is too long."""
    party = copy.deepcopy(CLIENT_PARTY)
    party['contact']['areaCode'] = '2500'

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_contact_phonenumber():
    """Assert that an invalid client party fails - contact phone number is too long."""
    party = copy.deepcopy(CLIENT_PARTY)
    party['contact']['phoneNumber'] = '1234567897171234'

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_missing_contact_name():
    """Assert that an invalid client party fails - contact name is missing."""
    party = copy.deepcopy(CLIENT_PARTY)
    del party['contact']['name']

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_missing_contact_areacode():
    """Assert that an invalid client party fails - contact area code is missing."""
    party = copy.deepcopy(CLIENT_PARTY)
    del party['contact']['areaCode']

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_missing_contact_phonenumber():
    """Assert that an invalid client party fails - contact phoneNumber is missing."""
    party = copy.deepcopy(CLIENT_PARTY)
    del party['contact']['phoneNumber']

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_missing_lastname():
    """Assert that an invalid client party fails - person last name is missing."""
    party = copy.deepcopy(CLIENT_PARTY)
    del party['personName']['last']

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_missing_person():
    """Assert that an invalid client party fails - personName is missing."""
    party = copy.deepcopy(CLIENT_PARTY)
    del party['personName']

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_missing_person_address():
    """Assert that an invalid client party fails - person address is missing."""
    party = copy.deepcopy(CLIENT_PARTY)
    del party['address']

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_missing_person_contact():
    """Assert that an invalid client party fails - person contact is missing."""
    party = copy.deepcopy(CLIENT_PARTY)
    del party['contact']

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_missing_business_address():
    """Assert that an invalid client party fails - business address is missing."""
    party = copy.deepcopy(CLIENT_PARTY)
    del party['personName']
    del party['address']
    party['businessName'] = 'BUSINESS NAME'

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_client_missing_business_contact():
    """Assert that an invalid client party fails - business contact is missing."""
    party = copy.deepcopy(CLIENT_PARTY)
    del party['personName']
    del party['contact']
    party['businessName'] = 'BUSINESS NAME'

    is_valid, errors = validate(party, 'clientParty', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
