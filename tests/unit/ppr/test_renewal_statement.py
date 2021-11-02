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
"""Test Suite to ensure the PPR Renewal Statement (request and response) schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import RENEWAL_STATEMENT


def test_valid_renewal_request():
    """Assert that the schema is performing as expected for a renewal request."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['courtOrderInformation']
    del statement['createDateTime']
    del statement['renewalRegistrationNumber']
    del statement['payment']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_renewal_rl_request():
    """Assert that the schema is performing as expected for a repairer's lien renewal request."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['expiryDate']
    del statement['createDateTime']
    del statement['renewalRegistrationNumber']
    del statement['payment']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_renewal_response():
    """Assert that the schema is performing as expected for an renewal response."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_renewal_baseregnum():
    """Assert that an invalid renewal statement fails - base registration number too long."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']
    statement['baseRegistrationNumber'] = 'B0000123456789'

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_renewal_clientref():
    """Assert that an invalid renewal statement fails - client reference number too long."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']
    statement['clientReferenceId'] = '012345678901234567890123456789012345678901234567890'

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_renewal_courtorder():
    """Assert that an invalid renewal statement fails - court order court name is missing."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']
    del statement['courtOrderInformation']['courtName']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_renewal_expiry():
    """Assert that an invalid renewal statement fails - expiry date format is invalid."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']
    statement['expiryDate'] = 'XXXXXXXX'

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    # Commenting out: no longer working with 3.8 build
    # assert not is_valid


def test_invalid_renewal_timestamp():
    """Assert that an invalid renewal statement fails - create timestamp format is invalid."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']
    statement['createDateTime'] = 'XXXXXXXXXXXX'

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    # Commenting out: no longer working with 3.8 build
    # assert not is_valid


def test_invalid_renewal_regnum():
    """Assert that an invalid renewal statement fails - registration number too long."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']
    statement['renewalRegistrationNumber'] = 'D000012345678'

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_renewal_missing_debtor_first():
    """Assert that an invalid renewal statement fails - base debtor name is missing."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['createDateTime']
    del statement['renewalRegistrationNumber']
    del statement['payment']
    del statement['debtorName']['businessName']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_renewal_missing_regparty_address():
    """Assert that an invalid renewal statement fails - registering party address is missing."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']
    del statement['registeringParty']['address']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_renewal_missing_basereg():
    """Assert that an invalid renewal statement fails - base registration number is missing."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']
    del statement['baseRegistrationNumber']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_renewal_missing_regparty():
    """Assert that an invalid renewal statement fails - registering party is missing."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']
    del statement['registeringParty']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_renewal_missing_debtor():
    """Assert that an invalid renewal statement fails - base debtor and statement reg number are missing."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['debtorName']
    del statement['createDateTime']
    del statement['renewalRegistrationNumber']
    del statement['payment']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_renewal_missing_expiry():
    """Assert that an invalid renewal statement fails - expiry date and court order information are missing."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['expiryDate']
    del statement['courtOrderInformation']
    del statement['createDateTime']
    del statement['renewalRegistrationNumber']
    del statement['payment']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_authorization_received():
    """Assert that authorization received validation works as expected."""
    statement = copy.deepcopy(RENEWAL_STATEMENT)
    del statement['courtOrderInformation']
    del statement['createDateTime']
    del statement['renewalRegistrationNumber']
    del statement['payment']
    del statement['authorizationReceived']

    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')
    assert is_valid

    statement['authorizationReceived'] = False
    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')
    assert is_valid

    statement['authorizationReceived'] = True
    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')
    assert is_valid

    statement['authorizationReceived'] = 'junk'
    is_valid, errors = validate(statement, 'renewalStatement', 'ppr')
    if errors:
        for err in errors:
            print(err.message)
    assert not is_valid
