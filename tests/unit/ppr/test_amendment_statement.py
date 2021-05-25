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
"""Test Suite to ensure the PPR Amendment Statement (request and response) schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import AMENDMENT_STATEMENT


def test_valid_amendment_request_am():
    """Assert that the schema is performing as expected for an amendment request."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    statement['changeType'] = 'AM'
    del statement['courtOrderInformation']
    del statement['createDateTime']
    del statement['amendmentRegistrationNumber']
    del statement['payment']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_request_co():
    """Assert that the schema is performing as expected for a court order amendment request."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['createDateTime']
    del statement['amendmentRegistrationNumber']
    del statement['payment']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_removeindenture():
    """Assert that the schema is performing as expected for a amendment to remove a trust indenture."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    statement['removeTrustIndenture'] = True
    del statement['baseDebtor']
    del statement['addTrustIndenture']
    del statement['deleteSecuredParties']
    del statement['addSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['addVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_addindenture():
    """Assert that the schema is performing as expected for a amendment to add a trust indenture."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    statement['addTrustIndenture'] = True
    del statement['baseDebtor']
    del statement['removeTrustIndenture']
    del statement['deleteSecuredParties']
    del statement['addSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['addVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_deletesecured():
    """Assert that the schema is performing as expected for a amendment to delete secured parties."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['removeTrustIndenture']
    del statement['addTrustIndenture']
    del statement['addSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['addVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_addsecured():
    """Assert that the schema is performing as expected for a amendment to add secured parties."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['removeTrustIndenture']
    del statement['addTrustIndenture']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['addVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_deletedebtors():
    """Assert that the schema is performing as expected for a amendment to delete debtors."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['removeTrustIndenture']
    del statement['addTrustIndenture']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['addVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_adddebtors():
    """Assert that the schema is performing as expected for a amendment to add debtors."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['removeTrustIndenture']
    del statement['addTrustIndenture']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['deleteVehicleCollateral']
    del statement['addVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_deletevehicles():
    """Assert that the schema is performing as expected for a amendment to delete vehicle collateral."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['removeTrustIndenture']
    del statement['addTrustIndenture']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['addVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_addvehicles():
    """Assert that the schema is performing as expected for a amendment to add vehicle collateral."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['removeTrustIndenture']
    del statement['addTrustIndenture']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_deletegeneral():
    """Assert that the schema is performing as expected for a amendment to delete general collateral."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['removeTrustIndenture']
    del statement['addTrustIndenture']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['addVehicleCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_addgeneral():
    """Assert that the schema is performing as expected for a amendment to add general collateral."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['removeTrustIndenture']
    del statement['addTrustIndenture']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['addVehicleCollateral']
    del statement['deleteGeneralCollateral']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_amendment_response():
    """Assert that the schema is performing as expected for an amendment response."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_amendment_baseregnum():
    """Assert that an invalid amendment statement fails - base registration number too long."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    statement['baseRegistrationNumber'] = 'B0000123456789'

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_clientref():
    """Assert that an invalid amendment statement fails - client reference number too long."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    statement['clientReferenceId'] = 'RSXXXXXXXX00001234567'

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_doc_id():
    """Assert that an invalid amendment statement fails - document id too long."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    statement['documentId'] = '00123456789'

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_changetype():
    """Assert that an invalid amendment statement fails - change type is invalid."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    statement['changeType'] = 'XX'

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_courtorder():
    """Assert that an invalid amendment statement fails - court order court name is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['courtOrderInformation']['courtName']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_timestamp():
    """Assert that an invalid amendment statement fails - create timestamp format is invalid."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    statement['createDateTime'] = 'XXXXXXXXXXXX'

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_regnum():
    """Assert that an invalid amendment statement fails - registration number too long."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    statement['amendmentRegistrationNumber'] = 'D000012345678'

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_delete_debtor_name():
    """Assert that an invalid amendment statement fails - delete debtor name is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['deleteDebtors'][0]['businessName']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_add_debtor_address():
    """Assert that an invalid amendment statement fails - add debtor address is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['addDebtors'][0]['address']
    del statement['addDebtors'][0]['partyId']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_delete_secured_name():
    """Assert that an invalid amendment statement fails - delete secured party name is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['deleteSecuredParties'][0]['businessName']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_add_secured_address():
    """Assert that an invalid amendment statement fails - add secured party address is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['addSecuredParties'][0]['address']
    del statement['addSecuredParties'][0]['partyId']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_delete_vehicle_type():
    """Assert that an invalid amendment statement fails - delete vehicle collateral type is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['deleteVehicleCollateral'][0]['type']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_add_vehicle_serial():
    """Assert that an invalid amendment statement fails - add vehicle collateral serial number is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['addVehicleCollateral'][0]['serialNumber']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_delete_general_desc():
    """Assert that an invalid amendment statement fails - delete general collateral description is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['deleteGeneralCollateral'][0]['description']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_add_general_desc():
    """Assert that an invalid amendment statement fails - add general collateral description is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['addGeneralCollateral'][0]['description']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_missing_debtor_first():
    """Assert that an invalid amendment statement fails - base debtor name is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['createDateTime']
    del statement['amendmentRegistrationNumber']
    del statement['payment']
    del statement['baseDebtor']['businessName']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_missing_regparty_address():
    """Assert that an invalid amendment statement fails - registering party address is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['registeringParty']['address']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_missing_basereg():
    """Assert that an invalid amendment statement fails - base registration number is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['baseRegistrationNumber']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_missing_regparty():
    """Assert that an invalid amendment statement fails - registering party is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['registeringParty']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_missing_changetype():
    """Assert that an invalid amendment statement fails - change type missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['changeType']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_co_missing_info():
    """Assert that an invalid amendment statement fails - CO change type missing court order information."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['baseDebtor']
    del statement['changeType']
    del statement['courtOrderInformation']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
