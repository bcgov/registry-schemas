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
"""Test Suite to ensure the PPR financing statement history schema is valid.

"""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import FINANCING_STATEMENT_HISTORY
from registry_schemas.example_data.ppr import CHANGE_STATEMENT
from registry_schemas.example_data.ppr import AMENDMENT_STATEMENT
from registry_schemas.example_data.ppr import RENEWAL_STATEMENT
from registry_schemas.example_data.ppr import DISCHARGE_STATEMENT


def test_valid_financing_history():
    """Assert that the schema is performing as expected for a financing statement history list."""
    is_valid, errors = validate(FINANCING_STATEMENT_HISTORY, 'financingStatementHistory', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_history_empty():
    """Assert that the schema is performing as expected for an empty financing statement history list."""
    history = copy.deepcopy(FINANCING_STATEMENT_HISTORY)
    del history[0]['changes'][3]
    del history[0]['changes'][2]
    del history[0]['changes'][1]
    del history[0]['changes'][0]

    is_valid, errors = validate(history, 'financingStatementHistory', 'ppr')


    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_history_amendment():
    """Assert that the schema is performing as expected for a financing statement history list with 1 amendment statement."""
    history = copy.deepcopy(FINANCING_STATEMENT_HISTORY)
    del history[0]['changes'][3]
    del history[0]['changes'][2]
    del history[0]['changes'][1]

    is_valid, errors = validate(history, 'financingStatementHistory', 'ppr')


    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_history_change():
    """Assert that the schema is performing as expected for a financing statement history list with 1 change statement."""
    history = copy.deepcopy(FINANCING_STATEMENT_HISTORY)
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del history[0]['changes'][3]
    del history[0]['changes'][2]
    del history[0]['changes'][1]
    del statement['baseDebtor']
    history[0]['changes'][0] = statement

    is_valid, errors = validate(history, 'financingStatementHistory', 'ppr')


    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_history_renewal():
    """Assert that the schema is performing as expected for a financing statement history list with 1 renewal statement."""
    history = copy.deepcopy(FINANCING_STATEMENT_HISTORY)
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['baseDebtor']
    del history[0]['changes'][3]
    del history[0]['changes'][2]
    del history[0]['changes'][1]
    history[0]['changes'][0] = statement

    is_valid, errors = validate(history, 'financingStatementHistory', 'ppr')


    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_history_discharge():
    """Assert that the schema is performing as expected for a financing statement history list with 1 discharge statement."""
    history = copy.deepcopy(FINANCING_STATEMENT_HISTORY)
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['baseDebtor']
    del history[0]['changes'][3]
    del history[0]['changes'][2]
    del history[0]['changes'][1]
    history[0]['changes'][0] = statement

    is_valid, errors = validate(history, 'financingStatementHistory', 'ppr')


    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_history_changes():
    """Assert that the schema is performing as expected for a financing statement history list with 2 change statements."""
    history = copy.deepcopy(FINANCING_STATEMENT_HISTORY)
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['baseDebtor']
    history[0]['changes'][3] = statement

    is_valid, errors = validate(history, 'financingStatementHistory', 'ppr')


    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_history_amendments():
    """Assert that the schema is performing as expected for a financing statement history list with 2 amendment statements."""
    history = copy.deepcopy(FINANCING_STATEMENT_HISTORY)
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    history[0]['changes'][3] = statement

    is_valid, errors = validate(history, 'financingStatementHistory', 'ppr')


    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_history_renewals():
    """Assert that the schema is performing as expected for a financing statement history list with 2 renewal statements."""
    history = copy.deepcopy(FINANCING_STATEMENT_HISTORY)
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['baseDebtor']
    history[0]['changes'][3] = statement

    is_valid, errors = validate(history, 'financingStatementHistory', 'ppr')


    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


