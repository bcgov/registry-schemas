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
"""Test Suite to ensure the PPR base debtor schema is valid.

"""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import BASE_DEBTOR


def test_valid_debtor_person():
    """Assert that the schema is performing as expected for an individual debtor."""
    is_valid, errors = validate(BASE_DEBTOR, 'baseDebtor', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_debtor_business():
    """Assert that the schema is performing as expected for a business debtor."""
    debtor = copy.deepcopy(BASE_DEBTOR)
    debtor['businessName'] = 'BUSINESS NAME DEBTOR INC.' 
    del debtor['personName']
    is_valid, errors = validate(debtor, 'baseDebtor', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_debtor_missing_firstname():
    """Assert that an invalid debtor fails - person first name is missing."""
    debtor = copy.deepcopy(BASE_DEBTOR)
    del debtor['personName']['first']

    is_valid, errors = validate(debtor, 'baseDebtor', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_debtor_missing_lastname():
    """Assert that an invalid debtor fails - person last name is missing."""
    debtor = copy.deepcopy(BASE_DEBTOR)
    del debtor['personName']['last']

    is_valid, errors = validate(debtor, 'baseDebtor', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_debtor_missing_debtor():
    """Assert that an invalid debtor fails - debtor name is missing."""
    debtor = copy.deepcopy(BASE_DEBTOR)
    del debtor['personName']

    is_valid, errors = validate(debtor, 'baseDebtor', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid

