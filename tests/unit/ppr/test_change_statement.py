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
"""Test Suite to ensure the PPR Change Statement (request and response) schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import CHANGE_STATEMENT


def test_valid_change_request_ac_vehicle():
    """Assert that the schema is performing as expected for an add vehicle collateral change request."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'AC'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_change_request_ac_general():
    """Assert that the schema is performing as expected for an add general collateral change request."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'AC'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addVehicleCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_change_request_ac_both():
    """Assert that the schema is performing as expected for an add vehicle and general collateral change request."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'AC'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['deleteGeneralCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_change_request_dr():
    """Assert that the schema is performing as expected for a debtor release change request."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'DR'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['addDebtors']
    del statement['addVehicleCollateral']
    del statement['deleteVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_change_request_dt():
    """Assert that the schema is performing as expected for a debtor transfer change request."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'DT'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['addVehicleCollateral']
    del statement['deleteVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_change_request_pd():
    """Assert that the schema is performing as expected for a partial discharge change request."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'PD'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addDebtors']
    del statement['deleteDebtors']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['addVehicleCollateral']
    del statement['deleteVehicleCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_change_request_st():
    """Assert that the schema is performing as expected for a secured party transfer change request."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'ST'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addDebtors']
    del statement['deleteDebtors']
    del statement['addVehicleCollateral']
    del statement['deleteVehicleCollateral']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_change_request_su_all():
    """Assert that the schema is performing as expected for a subsitution of general and vehicle collateral."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'SU'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addDebtors']
    del statement['deleteDebtors']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_change_request_su_vehicle():
    """Assert that the schema is performing as expected for a subsitution of vehicle collateral change request."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'SU'
    del statement['debtorName']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteGeneralCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_change_request_su_general():
    """Assert that the schema is performing as expected for a subsitution of general collateral change request."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'SU'
    del statement['debtorName']
    del statement['addSecuredParties']
    del statement['deleteSecuredParties']
    del statement['deleteDebtors']
    del statement['addDebtors']
    del statement['deleteVehicleCollateral']
    del statement['addVehicleCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_change_response():
    """Assert that the schema is performing as expected for an change response."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_change_ac_missing_collateral():
    """Assert that an invalid change statement fails - AC change but no add collateral."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addVehicleCollateral']
    del statement['addGeneralCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_pd_missing_collateral():
    """Assert that an invalid change statement fails - PD change but no delete collateral."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'PD'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['deleteVehicleCollateral']
    del statement['deleteGeneralCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_dr_missing_debtors():
    """Assert that an invalid change statement fails - DC change but no delete debtors."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'DR'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['deleteDebtors']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_dt_missing_delete():
    """Assert that an invalid change statement fails - DT change but no delete debtors."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'DT'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['deleteDebtors']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_dt_missing_add():
    """Assert that an invalid change statement fails - DT change but no add debtors."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'DT'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addDebtors']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_st_missing_add():
    """Assert that an invalid change statement fails - ST change but no add secured parties."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'ST'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addSecuredParties']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_st_missing_delete():
    """Assert that an invalid change statement fails - ST change but no delete secured parties."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'ST'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['deleteSecuredParties']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_su_missing_add():
    """Assert that an invalid change statement fails - SU change but no add collateral."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'SU'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['addGeneralCollateral']
    del statement['addVehicleCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_su_missing_delete():
    """Assert that an invalid change statement fails - SU change but no delete collateral."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['changeType'] = 'SU'
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['deleteGeneralCollateral']
    del statement['deleteVehicleCollateral']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_baseregnum():
    """Assert that an invalid change statement fails - base registration number too long."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    statement['baseRegistrationNumber'] = 'B0000123456789'

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_clientref():
    """Assert that an invalid change statement fails - client reference number too long."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    statement['clientReferenceId'] = 'RSXXXXXXXX00001234567'

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_doc_id():
    """Assert that an invalid change statement fails - document id too long."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    statement['documentId'] = '00123456789'

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_changetype():
    """Assert that an invalid change statement fails - change type is invalid."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    statement['changeType'] = 'XX'

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_timestamp():
    """Assert that an invalid change statement fails - create timestamp format is invalid."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    statement['createDateTime'] = 'XXXXXXXXXXXX'

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_regnum():
    """Assert that an invalid change statement fails - registration number too long."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    statement['changeRegistrationNumber'] = 'D000012345678'

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_delete_debtor_name():
    """Assert that an invalid change statement fails - delete debtor name is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['deleteDebtors'][0]['businessName']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_add_debtor_address():
    """Assert that an invalid change statement fails - add debtor address is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['addDebtors'][0]['address']
    del statement['addDebtors'][0]['partyId']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_delete_secured_name():
    """Assert that an invalid change statement fails - delete secured party name is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['deleteSecuredParties'][0]['businessName']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_add_secured_address():
    """Assert that an invalid change statement fails - add secured party address is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['addSecuredParties'][0]['address']
    del statement['addSecuredParties'][0]['partyId']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_delete_vehicle_type():
    """Assert that an invalid change statement fails - delete vehicle collateral type is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['deleteVehicleCollateral'][0]['type']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_add_vehicle_serial():
    """Assert that an invalid change statement fails - add vehicle collateral serial number is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['addVehicleCollateral'][0]['serialNumber']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_delete_general_desc():
    """Assert that an invalid change statement fails - delete general collateral description is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['deleteGeneralCollateral'][0]['description']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_add_general_desc():
    """Assert that an invalid change statement fails - add general collateral description is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['addGeneralCollateral'][0]['description']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_missing_debtor_first():
    """Assert that an invalid change statement fails - base debtor name is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['createDateTime']
    del statement['changeRegistrationNumber']
    del statement['payment']
    del statement['debtorName']['businessName']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_missing_regparty_address():
    """Assert that an invalid change statement fails - registering party address is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['registeringParty']['address']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_missing_basereg():
    """Assert that an invalid change statement fails - base registration number is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['baseRegistrationNumber']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_missing_regparty():
    """Assert that an invalid change statement fails - registering party is missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['registeringParty']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_change_missing_changetype():
    """Assert that an invalid change statement fails - change type missing."""
    statement = copy.deepcopy(CHANGE_STATEMENT)
    del statement['debtorName']
    del statement['changeType']

    is_valid, errors = validate(statement, 'changeStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
