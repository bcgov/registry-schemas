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
"""Test Suite to ensure the PPR Financing Statement (request and response) schema is valid.

"""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import FINANCING_STATEMENT


def test_valid_financing_request_SA():
    """Assert that the schema is performing as expected for a security agreement financing request."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'SA'
    del statement['createDateTime']
    del statement['baseRegistrationNumber']
    del statement['payment']
    del statement['lifeInfinite']
    del statement['lienAmount']
    del statement['surrenderDate']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_request_RL():
    """Assert that the schema is performing as expected for a repairer's lien financing request."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'RL'
    del statement['createDateTime']
    del statement['baseRegistrationNumber']
    del statement['payment']
    del statement['lifeYears']
    del statement['lifeInfinite']
    del statement['trustIndenture']
    del statement['generalCollateral']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_request_FR():
    """Assert that the schema is performing as expected for a FR financing request."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'FR'
    del statement['createDateTime']
    del statement['baseRegistrationNumber']
    del statement['payment']
    del statement['lienAmount']
    del statement['surrenderDate']
    del statement['trustIndenture']
    del statement['generalCollateral']
    del statement['lifeYears']
    del statement['expiryDate']
    statement['lifeInfinite'] = True

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_request_LT():
    """Assert that the schema is performing as expected for a land tax lien financing request."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'LT'
    del statement['createDateTime']
    del statement['baseRegistrationNumber']
    del statement['payment']
    del statement['lifeInfinite']
    del statement['trustIndenture']
    del statement['lienAmount']
    del statement['surrenderDate']
    del statement['vehicleCollateral']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_request_MH():
    """Assert that the schema is performing as expected for a manufactured home lien financing request."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'MH'
    del statement['createDateTime']
    del statement['baseRegistrationNumber']
    del statement['payment']
    del statement['trustIndenture']
    del statement['lifeInfinite']
    del statement['lienAmount']
    del statement['surrenderDate']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_request_SG():
    """Assert that the schema is performing as expected for a sale of goods financing request."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'SG'
    del statement['createDateTime']
    del statement['baseRegistrationNumber']
    del statement['payment']
    del statement['trustIndenture']
    del statement['lifeInfinite']
    del statement['lienAmount']
    del statement['surrenderDate']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_request_FL():
    """Assert that the schema is performing as expected for a forestry contractor lien financing request."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'FL'
    del statement['createDateTime']
    del statement['baseRegistrationNumber']
    del statement['payment']
    del statement['trustIndenture']
    del statement['lifeInfinite']
    del statement['lienAmount']
    del statement['surrenderDate']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_request_FA():
    """Assert that the schema is performing as expected for a forestry contractor charge lien financing request."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'FA'
    del statement['createDateTime']
    del statement['baseRegistrationNumber']
    del statement['payment']
    del statement['trustIndenture']
    del statement['lifeInfinite']
    del statement['lienAmount']
    del statement['surrenderDate']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_request_FS():
    """Assert that the schema is performing as expected for a forestry contractor subcharge lien financing request."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'FS'
    del statement['createDateTime']
    del statement['baseRegistrationNumber']
    del statement['payment']
    del statement['trustIndenture']
    del statement['lifeInfinite']
    del statement['lienAmount']
    del statement['surrenderDate']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_request_MR():
    """Assert that the schema is performing as expected for a miscellaneous regulations act financing request."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'MR'
    del statement['createDateTime']
    del statement['baseRegistrationNumber']
    del statement['payment']
    del statement['trustIndenture']
    del statement['lifeInfinite']
    del statement['lienAmount']
    del statement['surrenderDate']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_financing_response_SA():
    """Assert that the schema is performing as expected for an financing response."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['lifeInfinite']
    del statement['lienAmount']
    del statement['surrenderDate']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_financing_baseregnum():
    """Assert that an invalid financing statement fails - base registration number too long."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['baseRegistrationNumber'] = 'B0000123456789'

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_clientref():
    """Assert that an invalid financing statement fails - client reference number too long."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['clientReferenceId'] = 'RSXXXXXXXX00001234567'

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_doc_id():
    """Assert that an invalid financing statement fails - document id too long."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['documentId'] = '00123456789'

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_type():
    """Assert that an invalid financing statement fails - financing type is invalid."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['type'] = 'XX'

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_timestamp():
    """Assert that an invalid financing statement fails - create timestamp format is invalid."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['createDateTime'] = 'XXXXXXXXXXXX'

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_expiry():
    """Assert that an invalid financing statement fails - expiry date format is invalid."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['expiryDate'] = 'XXXXXXXX'

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_lifeyears():
    """Assert that an invalid financing statement fails - life years value is invalid."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['lifeYears'] = 26

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_lienamount():
    """Assert that an invalid financing statement fails - liend amount is too long."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['lienAmount'] = '0123456789123456'

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_surrender():
    """Assert that an invalid financing statement fails - surrender date format is invalid."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    statement['surrenderDate'] = 'XXXXXXXX'

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_debtor_name():
    """Assert that an invalid financing statement fails - debtor name is missing."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['debtors'][0]['businessName']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_delete_secured_name():
    """Assert that an invalid financing statement fails - secured party name is missing."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['securedParties'][0]['businessName']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_regparty_address():
    """Assert that an invalid financing statement fails - registering party address is missing."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['registeringParty']['address']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_missing_vehicle_type():
    """Assert that an invalid financing statement fails - vehicle collateral type is missing."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['vehicleCollateral'][0]['type']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_missing_general_desc():
    """Assert that an invalid financing statement fails - general collateral description is missing."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['generalCollateral'][0]['description']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_missing_regparty():
    """Assert that an invalid financing statement fails - registering party is missing."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['registeringParty']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_missing_type():
    """Assert that an invalid financing statement fails - financing type missing."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['type']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_missing_secparties():
    """Assert that an invalid financing statement fails - secured parties are missing."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['securedParties']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid



def test_invalid_financing_missing_debtors():
    """Assert that an invalid financing statement fails - debtors are missing."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['debtors']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_financing_missing_collateral():
    """Assert that an invalid financing statement fails - vehicle and general collateral are missing."""
    statement = copy.deepcopy(FINANCING_STATEMENT)
    del statement['vehicleCollateral']
    del statement['generalCollateral']

    is_valid, errors = validate(statement, 'financingStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid

