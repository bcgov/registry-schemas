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
"""Test Suite to ensure the PPR Draft Summary schema is valid.

"""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import DRAFT_SUMMARY


def test_valid_draft_summary():
    """Assert that the schema is performing as expected for a draft summary list."""
    is_valid, errors = validate(DRAFT_SUMMARY, 'draftSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_draft_summary_empty():
    """Assert that the schema is performing as expected for an empty draft summary list."""
    draft = copy.deepcopy(DRAFT_SUMMARY)
    del draft[2]
    del draft[1]
    del draft[0]

    is_valid, errors = validate(draft, 'draftSummary', 'ppr')


    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_draft_summary_missing_type():
    """Assert that an invalid draft summary fails - type is missing."""
    draft = copy.deepcopy(DRAFT_SUMMARY)
    del draft[0]['type']

    is_valid, errors = validate(draft, 'draftSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_summary_missing_regtype():
    """Assert that an invalid draft summary fails - registration type is missing."""
    draft = copy.deepcopy(DRAFT_SUMMARY)
    del draft[0]['registrationType']

    is_valid, errors = validate(draft, 'draftSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_summary_missing_docId():
    """Assert that an invalid draft summary fails - document ID is missing."""
    draft = copy.deepcopy(DRAFT_SUMMARY)
    del draft[0]['documentId']

    is_valid, errors = validate(draft, 'draftSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_summary_missing_path():
    """Assert that an invalid draft summary fails - path is missing."""
    draft = copy.deepcopy(DRAFT_SUMMARY)
    del draft[0]['path']

    is_valid, errors = validate(draft, 'draftSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_summary_missing_timestamp():
    """Assert that an invalid draft summary fails - create date time is missing."""
    draft = copy.deepcopy(DRAFT_SUMMARY)
    del draft[0]['createDateTime']

    is_valid, errors = validate(draft, 'draftSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_summary_docId():
    """Assert that an invalid draft summary fails - document Id is too long."""
    draft = copy.deepcopy(DRAFT_SUMMARY)
    draft[0]['documentId'] = 'XXXXXXXXXXXXX'

    is_valid, errors = validate(draft, 'draftSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_summary_type():
    """Assert that an invalid draft summary fails - type is too long."""
    draft = copy.deepcopy(DRAFT_SUMMARY)
    draft[0]['type'] = 'XXXXXXXXXXX'

    is_valid, errors = validate(draft, 'draftSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_draft_summary_regtype():
    """Assert that an invalid draft summary fails - registration type is too long."""
    draft = copy.deepcopy(DRAFT_SUMMARY)
    draft[0]['registrationType'] = 'XXX'

    is_valid, errors = validate(draft, 'draftSummary', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


