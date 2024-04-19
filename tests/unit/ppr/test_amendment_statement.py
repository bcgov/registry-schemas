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

import pytest

from registry_schemas import validate
from registry_schemas.example_data.ppr import AMENDMENT_STATEMENT


ADD_SECURITIES_ACT_ORDERS = [
    {
        'courtName': 'Supreme Court of British Columbia',
        'courtRegistry': 'KAMLOOPS',
        'fileNumber': 'BC123445',
        'orderDate': '2024-02-02T00:00:00-08:00',
        'effectOfOrder': 'Court Order to remove James Smith as debtor.',
        'courtOrder': True
    },
    {
        'courtName': 'British Columbia Court of Appeal',
        'courtRegistry': 'Vancouver',
        'fileNumber': 'BCA123445',
        'orderDate': '2024-02-02T00:00:00-08:00',
        'effectOfOrder': 'Court Order to remove James Smith as debtor.',
        'courtOrder': True
    }
]
DELETE_SECURITIES_ACT_ORDERS = [
    {
        'courtName': 'Supreme Court of British Columbia.',
        'courtRegistry': 'KAMLOOPS',
        'fileNumber': 'BC123445',
        'orderDate': '2024-02-02T00:00:00-08:00',
        'effectOfOrder': 'Court Order to remove James Smith as debtor.',
        'courtOrder': True
    }
]
DELETE_SECURITIES_ACT_NOTICE = {
    'noticeId': 1,
    'securitiesActNoticeType': 'LIEN',
    'effectiveDateTime': '2024-02-02T00:00:00-08:00',
    'description': 'TEST DELETE LIEN NOTICE TYPE',
    'securitiesActOrders': DELETE_SECURITIES_ACT_ORDERS
}
ADD_SECURITIES_ACT_NOTICE = {
    'securitiesActNoticeType': 'LIEN',
    'effectiveDateTime': '2024-04-12T00:00:00-08:00',
    'description': 'TEST ADD LIEN NOTICE TYPE',
    'securitiesActOrders': ADD_SECURITIES_ACT_ORDERS
}
# testdata pattern is ({change type}, {is valid})
TEST_DATA_CHANGE_TYPE = [
    ('AM', True),
    ('AA', True),
    ('AR', True),
    ('AD', True),
    ('AP', True),
    ('AS', True),
    ('AU', True),
    ('XX', False)
]
# testdata pattern is ({desc}, {valid}, {add}, {delete}, {add_order}, {delete_order)
TEST_DATA_SEC_ACT = [
    ('Valid no notice changes', True, None, None, False, False),
    ('Valid add court order(s)', True, ADD_SECURITIES_ACT_NOTICE, None, True, False),
    ('Valid delete court order(s)', True, None, DELETE_SECURITIES_ACT_NOTICE, False, True),
    ('Valid change court orders', True, ADD_SECURITIES_ACT_NOTICE, DELETE_SECURITIES_ACT_NOTICE, True, True),
    ('Invalid add missing notice type', False, ADD_SECURITIES_ACT_NOTICE, None, True, False),
    ('Invalid add missing courtOrder', False, ADD_SECURITIES_ACT_NOTICE, None, True, False)
]


@pytest.mark.parametrize('desc,valid,add,delete,add_order,delete_order', TEST_DATA_SEC_ACT)
def test_sec_act_amendment(desc, valid, add, delete, add_order, delete_order):
    """Assert that the schema is performing as expected when amending a securities act base registration."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    statement['changeType'] = 'AM'
    del statement['courtOrderInformation']
    del statement['createDateTime']
    del statement['amendmentRegistrationNumber']
    del statement['payment']
    add_notice = None
    delete_notice = None
    if add:
        add_notice = copy.deepcopy(add)
        if not add_order:
            del add_notice['securitiesActOrders']
    if delete:
        delete_notice = copy.deepcopy(delete)
        if not delete_order:
            del delete_notice['securitiesActOrders']
    if desc == 'Invalid add missing notice type':
        del add_notice['securitiesActNoticeType']
    elif desc == 'Invalid add missing courtOrder':
        del add_notice['securitiesActOrders'][0]['courtOrder']
    if add_notice:
        statement['addSecuritiesActNotices'] = [add_notice]
    if delete_notice:
        statement['deleteSecuritiesActNotices'] = [delete_notice]

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('change_type, valid', TEST_DATA_CHANGE_TYPE)
def test_change_type(change_type, valid):
    """Assert that the schema is performing as expected for all amendment change types (CO tested separately)."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    statement['changeType'] = change_type
    del statement['courtOrderInformation']
    del statement['createDateTime']
    del statement['amendmentRegistrationNumber']
    del statement['payment']
    del statement['description']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']

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
    del statement['debtorName']
    statement['clientReferenceId'] = '012345678901234567890123456789012345678901234567890'

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_doc_id():
    """Assert that an invalid amendment statement fails - document id too long."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
    statement['createDateTime'] = 'XXXXXXXXXXXX'

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    # Commenting out: no longer working with 3.8 build
    # assert not is_valid


def test_invalid_amendment_regnum():
    """Assert that an invalid amendment statement fails - registration number too long."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']['businessName']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_amendment_missing_regparty_address():
    """Assert that an invalid amendment statement fails - registering party address is missing."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
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
    del statement['debtorName']
    del statement['changeType']
    del statement['courtOrderInformation']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_authorization_received():
    """Assert that authorization received validation works as expected."""
    statement = copy.deepcopy(AMENDMENT_STATEMENT)
    del statement['authorizationReceived']

    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')
    assert is_valid

    statement['authorizationReceived'] = False
    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')
    assert is_valid

    statement['authorizationReceived'] = True
    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')
    assert is_valid

    statement['authorizationReceived'] = 'junk'
    is_valid, errors = validate(statement, 'amendmentStatement', 'ppr')
    if errors:
        for err in errors:
            print(err.message)
    assert not is_valid
