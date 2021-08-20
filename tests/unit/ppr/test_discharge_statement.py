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
"""Test Suite to ensure the PPR Discharge Statement (request and response) schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import DISCHARGE_STATEMENT


def test_valid_discharge_request():
    """Assert that the schema is performing as expected for a discharge request."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['createDateTime']
    del statement['dischargeRegistrationNumber']
    del statement['payment']

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_discharge_response():
    """Assert that the schema is performing as expected for a discharge response."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['debtorName']

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_discharge_baseregnum():
    """Assert that an invalid discharge statement fails - base registration number too long."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['debtorName']
    statement['baseRegistrationNumber'] = 'B0000123456789'

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_discharge_clientref():
    """Assert that an invalid discharge statement fails - client reference number too long."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['debtorName']
    statement['clientReferenceId'] = 'RSXXXXXXXX00001234567'

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_discharge_timestamp():
    """Assert that an invalid discharge statement fails - create timestamp format is invalid."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['debtorName']
    statement['createDateTime'] = 'XXXXXXXXXXXX'

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_discharge_regnum():
    """Assert that an invalid discharge statement fails - registration number too long."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['debtorName']
    statement['dischargeRegistrationNumber'] = 'D000012345678'

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_discharge_missing_debtor_first():
    """Assert that an invalid discharge statement fails - base debtor name is missing."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['createDateTime']
    del statement['dischargeRegistrationNumber']
    del statement['payment']
    del statement['debtorName']['businessName']

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_discharge_missing_regparty_address():
    """Assert that an invalid discharge statement fails - registering party address is missing."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['debtorName']
    del statement['registeringParty']['address']

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_discharge_missing_basereg():
    """Assert that an invalid discharge statement fails - base registration number is missing."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['debtorName']
    del statement['baseRegistrationNumber']

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_discharge_missing_regparty():
    """Assert that an invalid discharge statement fails - registering party is missing."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['debtorName']
    del statement['registeringParty']

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_discharge_missing_debtor():
    """Assert that an invalid discharge statement fails - base debtor and statement reg number are missing."""
    statement = copy.deepcopy(DISCHARGE_STATEMENT)
    del statement['debtorName']
    del statement['createDateTime']
    del statement['dischargeRegistrationNumber']
    del statement['payment']

    is_valid, errors = validate(statement, 'dischargeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
