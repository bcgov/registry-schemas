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
"""Test Suite to ensure the common person name schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.common import PERSON_NAME


def test_valid_person():
    """Assert that the schema is performing as expected for an individual name."""
    is_valid, errors = validate(PERSON_NAME, 'personName', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_person_firstname():
    """Assert that an invalid person name fails - first name too long."""
    name = copy.deepcopy(PERSON_NAME)
    name['first'] = 'Too long0123456789012345678901234567890123456789012'

    is_valid, errors = validate(name, 'personName', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_person_lastname():
    """Assert that an invalid person name fails - last name too long."""
    name = copy.deepcopy(PERSON_NAME)
    name['last'] = 'Too long0123456789012345678901234567890123456789012'

    is_valid, errors = validate(name, 'personName', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_person_middlename():
    """Assert that an invalid person name fails - middle name too long."""
    name = copy.deepcopy(PERSON_NAME)
    name['middle'] = 'Too long0123456789012345678901234567890123456789012'

    is_valid, errors = validate(name, 'personName', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_person_missing_first():
    """Assert that an invalid person name fails - first name is missing."""
    name = copy.deepcopy(PERSON_NAME)
    del name['first']

    is_valid, errors = validate(name, 'personName', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_person_missing_last():
    """Assert that an invalid person name fails - last name is missing."""
    name = copy.deepcopy(PERSON_NAME)
    del name['last']

    is_valid, errors = validate(name, 'personName', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
