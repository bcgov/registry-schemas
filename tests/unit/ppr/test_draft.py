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
"""Test Suite to ensure the PPR Draft schema is valid.

"""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import DRAFT_FINANCING_STATEMENT
from registry_schemas.example_data.ppr import DRAFT_CHANGE_STATEMENT
from registry_schemas.example_data.ppr import DRAFT_AMENDMENT_STATEMENT


def test_valid_draft_financing():
    """Assert that the schema is performing as expected for a financing statement draft."""
    is_valid, errors = validate(DRAFT_FINANCING_STATEMENT, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_draft_amendment():
    """Assert that the schema is performing as expected for an amendment statement draft."""
    is_valid, errors = validate(DRAFT_AMENDMENT_STATEMENT, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_draft_change():
    """Assert that the schema is performing as expected for a change statement draft."""
    is_valid, errors = validate(DRAFT_CHANGE_STATEMENT, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_draft_missing_type():
    """Assert that an invalid draft fails - type is missing."""
    draft = copy.deepcopy(DRAFT_AMENDMENT_STATEMENT)
    del draft['type']

    is_valid, errors = validate(draft, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_amendment_type_mismatch():
    """Assert that an invalid draft fails - statement is amendment but type is not."""
    draft = copy.deepcopy(DRAFT_AMENDMENT_STATEMENT)
    draft['type'] = 'CHANGE_STATEMENT'

    is_valid, errors = validate(draft, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_change_type_mismatch():
    """Assert that an invalid draft fails - statement is change but type is not."""
    draft = copy.deepcopy(DRAFT_CHANGE_STATEMENT)
    draft['type'] = 'AMENDMENT_STATEMENT'

    is_valid, errors = validate(draft, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_financing_type_mismatch():
    """Assert that an invalid draft fails - statement is financing but type is not."""
    draft = copy.deepcopy(DRAFT_FINANCING_STATEMENT)
    draft['type'] = 'CHANGE_STATEMENT'

    is_valid, errors = validate(draft, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_missing_statement():
    """Assert that an invalid draft fails - statement is missing."""
    draft = copy.deepcopy(DRAFT_CHANGE_STATEMENT)
    del draft['changeStatement']

    is_valid, errors = validate(draft, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_multiple_statement():
    """Assert that an invalid draft fails - more than 1 statement exists."""
    draft = copy.deepcopy(DRAFT_CHANGE_STATEMENT)
    draft2 = copy.deepcopy(DRAFT_FINANCING_STATEMENT)
    draft['financingStatement'] = draft2['financingStatement']

    is_valid, errors = validate(draft, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_type():
    """Assert that an invalid draft fails - type is invalid."""
    draft = copy.deepcopy(DRAFT_CHANGE_STATEMENT)
    draft['type'] = 'XXXX'

    is_valid, errors = validate(draft, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_timestamp():
    """Assert that an invalid draft fails - create timestamp format is invalid."""
    draft = copy.deepcopy(DRAFT_CHANGE_STATEMENT)
    draft['createDateTime'] = 'XXXXXXXXXXXX'

    is_valid, errors = validate(draft, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_update():
    """Assert that an invalid draft fails - update timestamp format is invalid."""
    draft = copy.deepcopy(DRAFT_CHANGE_STATEMENT)
    draft['lastUpdateDateTime'] = 'XXXXXXXXXXXX'

    is_valid, errors = validate(draft, 'draft', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid

