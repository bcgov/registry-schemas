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
"""Test Suite to ensure the MHR transfer (tranfer of sale) schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import OWNER_GROUP, TRANSFER


PARTY_VALID = {
    'personName': {
        'first': 'Michael',
        'middle': 'J',
        'last': 'Smith'
    },
    'address': {
        'street': '520 Johnson St',
        'city': 'Victoria',
        'region': 'BC',
        'country': 'CA',
        'postalCode': 'V8S 2V4'
    },
    'emailAddress': 'msmith@gmail.com',
    'phoneNumber': '6042314598',
    'phoneExtension': '546'
}
PARTY_INVALID = {
    'personName': {
        'first': 'Michael',
        'middle': 'J',
        'last': 'Smith'
    },
    'address': {
        'street': '520 Johnson St',
        'city': 'Victoria',
        'region': 'BC',
        'country': 'CA',
        'postalCode': 'V8S 2V4'
    },
    'emailAddress': 'msmith@gmail.com',
    'phoneNumber': '2314598'
}
LONG_CLIENT_REF = '012345678901234567890123456789012345678901234567890'
MAX_CONSIDERATION = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'
OWNER_GROUPS = [
    OWNER_GROUP
]
ADDRESS1 = {
  'city': 'delivery_address city',
  'region': 'BC',
  'postalCode': 'V8S2J9',
  'country': 'CA'
}
ADDRESS2 = {
  'street': 'delivery_address - address line one',
  'region': 'BC',
  'postalCode': 'V8S2J9',
  'country': 'CA'
}
ADDRESS3 = {
  'street': 'delivery_address - address line one',
  'city': 'delivery_address city',
  'postalCode': 'V8S2J9',
  'country': 'CA'
}
ADDRESS4 = {
  'street': 'delivery_address - address line one',
  'city': 'delivery_address city',
  'region': 'BC',
  'country': 'CA'
}
ADDRESS5 = {
  'street': 'delivery_address - address line one',
  'city': 'delivery_address city',
  'region': 'BC',
  'postalCode': 'V8S2J9'
}

# testdata pattern is ({desc},{valid},{sub_party},{add},{delete},{is_request},{client_ref})
TEST_DATA = [
    ('Valid request', True, PARTY_VALID, True, True, True, None),
    ('Valid response', True, PARTY_VALID, True, True, False, '1234'),
    ('Invalid client ref', False, PARTY_VALID, True, True, True, LONG_CLIENT_REF),
    ('Invalid sub party', False, PARTY_INVALID, True, True, True, '1234'),
    ('Missing sub party', False, None, True, True, True, '1234'),
    ('Invalid missing add', False, PARTY_VALID, False, True, True, '1234'),
    ('Invalid missing delete', False, PARTY_VALID, True, False, True, ''),
]
# testdata pattern is ({desc},{valid},{declared},{consid},{tran_dt},{own_land})
TEST_DATA_DETAILS = [
    ('Valid all', True, 60000, MAX_CONSIDERATION, '2022-09-20T10:39:03-07:53', False),
    ('Valid none', True, None, None, None, None),
    ('Invalid declared', False, 'xxxx', MAX_CONSIDERATION, '2022-09-20T10:39:03-07:53', False),
    ('Invalid consideration', False, 60000, MAX_CONSIDERATION + 'X', '2022-09-20T10:39:03-07:53', False)
]
# testdata pattern is ({desc},{valid},{reg_type})
TEST_DATA_REG_TYPE = [
    ('Valid no type', True,  None),
    ('Valid TRANS', True,  'TRANS'),
    ('Valid TRAND', True,  'TRANS'),
    ('Valid TRANS_AFFIDAVIT', True,  'TRANS_AFFIDAVIT'),
    ('Valid TRANS_ADMIN', True,  'TRANS_ADMIN'),
    ('Valid TRANS_WILL', True,  'TRANS_WILL'),
    ('Invalid type', False,  'MH_REG')
]
# testdata pattern is ({desc},{valid},{doc_type})
TEST_DATA_DOC_TYPE = [
    ('Valid no type', True,  None),
    ('Valid TRANS_LAND_TITLE', True,  'TRANS_LAND_TITLE'),
    ('Valid TRANS_FAMILY_ACT', True,  'TRANS_FAMILY_ACT'),
    ('Valid TRANS_INFORMAL_SALE', True,  'TRANS_INFORMAL_SALE'),
    ('Valid TRANS_QUIT_CLAIM', True,  'TRANS_QUIT_CLAIM'),
    ('Valid TRANS_SEVER_GRANT', True,  'TRANS_SEVER_GRANT'),
    ('Valid TRANS_RECEIVERSHIP', True,  'TRANS_RECEIVERSHIP'),
    ('Valid TRANS_TRUST', True,  'TRANS_TRUST'),
    ('Valid TRANS_LANDLORD', True,  'TRANS_LANDLORD'),
    ('Valid TRANS_WRIT_SEIZURE', True,  'TRANS_WRIT_SEIZURE'),
    ('Valid ABAN', True,  'ABAN'),
    ('Valid COU', True,  'COU'),
    ('Valid BANK', True,  'BANK'),
    ('Valid FORE', True,  'FORE'),
    ('Valid GENT', True,  'GENT'),
    ('Valid REIV', True,  'REIV'),
    ('Valid REPV', True,  'REPV'),
    ('Valid SZL', True,  'SZL'),
    ('Valid TAXS', True,  'TAXS'),
    ('Valid VEST', True,  'VEST'),
    ('Invalid type', False,  'WILL')
]
# testdata pattern is ({desc},{valid},{delete_owners},{delete_address})
TEST_DATA_DELETE_GROUP = [
   ('Valid', True, False, None),
   ('Valid no owners', True, True, None),
   ('Valid no address street', True, False, ADDRESS1),
   ('Valid no address city', True, False, ADDRESS2),
   ('Valid no address region', True, False, ADDRESS3),
   ('Valid no address pcode', True, False, ADDRESS4),
   ('Valid no address country', True, False, ADDRESS5),
 ]


@pytest.mark.parametrize('desc,valid,del_owners,del_address', TEST_DATA_DELETE_GROUP)
def test_transfer_delete_group(desc, valid, del_owners, del_address):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(TRANSFER)
    del_group = copy.deepcopy(OWNER_GROUPS)
    if del_address:
        for owner in del_group[0].get('owners'):
            owner['address'] = del_address
    elif del_owners:
        del del_group[0]['owners']
    data['deleteOwnerGroups'] = del_group

    is_valid, errors = validate(data, 'transfer', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,sub_party,add,delete,is_request,client_ref', TEST_DATA)
def test_transfer(desc, valid, sub_party, add, delete, is_request, client_ref):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(TRANSFER)
    if sub_party:
        data['submittingParty'] = sub_party
    else:
        del data['submittingParty']
    if client_ref:
        data['clientReferenceId'] = client_ref
    else:
        del data['clientReferenceId']
    if is_request:
        del data['createDateTime']
        del data['payment']
        del data['mhrNumber']
        del data['documentId']
        del data['documentDescription']
    if not add:
        del data['addOwnerGroups']
    if not delete:
        del data['deleteOwnerGroups']

    is_valid, errors = validate(data, 'transfer', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,declared,consideration,tran_dt,own_land', TEST_DATA_DETAILS)
def test_transfer_details(desc, valid, declared, consideration, tran_dt, own_land):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(TRANSFER)
    if declared:
        data['declaredValue'] = declared
    else:
        del data['declaredValue']
    if consideration:
        data['consideration'] = consideration
    else:
        del data['consideration']
    if tran_dt:
        data['transferDate'] = tran_dt
    else:
        del data['transferDate']
    if own_land:
        data['ownLand'] = own_land
    else:
        del data['ownLand']

    is_valid, errors = validate(data, 'transfer', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,reg_type', TEST_DATA_REG_TYPE)
def test_transfer_reg_type(desc, valid, reg_type):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(TRANSFER)
    del data['createDateTime']
    del data['payment']
    del data['mhrNumber']
    del data['documentId']
    del data['documentDescription']
    if reg_type:
        data['registrationType'] = reg_type

    is_valid, errors = validate(data, 'transfer', 'mhr')

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,doc_type', TEST_DATA_DOC_TYPE)
def test_transfer_doc_type(desc, valid, doc_type):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(TRANSFER)
    del data['createDateTime']
    del data['payment']
    del data['mhrNumber']
    del data['documentId']
    del data['documentDescription']
    if doc_type:
        data['registrationType'] = 'TRANS'
        data['transferDocumentType'] = doc_type
    elif data.get('registrationType'):
        del data['registrationType']

    is_valid, errors = validate(data, 'transfer', 'mhr')

    if valid:
        assert is_valid
    else:
        assert not is_valid
