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
"""Test Suite to ensure the MHR transport permit registration schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import ADMIN_REGISTRATION, DESCRIPTION, LOCATION, OWNER_GROUP


LONG_CLIENT_REF = '012345678901234567890123456789012345678901234567890'
OWNER_GROUPS = [
    OWNER_GROUP
]
# testdata pattern is ({desc},{valid},{doc_type},{has_submitting},{is_request},{client_ref}, {attention})
TEST_DATA = [
    ('Valid request COUR', True, 'COUR', True, True, None, None),
    ('Valid request NRED', True, 'NRED', True, True, None, None),
    ('Valid request NCAN', True, 'NCAN', True, True, None, None),
    ('Valid request STAT', True, 'STAT', True, True, None, None),
    ('Valid request CANCEL_PERMIT', True, 'CANCEL_PERMIT', True, True, None, None),
    ('Valid response CANCEL_PERMIT', True, 'CANCEL_PERMIT', True, True, None, None),
    ('Valid response', True, 'THAW', True, False, '1234', 'JOHN SMITH'),
    ('Invalid client ref', False, 'NRED', True, True, LONG_CLIENT_REF, None),
    ('Invalid attention', False, 'EXRE', True, True, None, LONG_CLIENT_REF),
    ('Invalid missing doc type', False, None, True, True, None, None),
    ('Invalid doc type', False, 'TAXN', True, True, None, None),
    ('Invalid missing sub party', False, 'NRED', False, True, None, None),
    ('Invalid update doc id', False, 'NRED', True, True, None, None)
]
# testdata pattern is ({desc},{valid},{doc_type},{status},{location},{description}, {owner_group})
TEST_DATA_AMEND_CORRECT = [
    ('Valid amendment location', True, 'PUBA', None, LOCATION, None, None),
    ('Valid staff correction location', True, 'REGC_STAFF', None, LOCATION, None, None),
    ('Valid client correction location', True, 'REGC_CLIENT', None, LOCATION, None, None),
    ('Valid amendment description', True, 'PUBA', None, None, DESCRIPTION, None),
    ('Valid staff correction description', True, 'REGC_STAFF', None, None, DESCRIPTION, None),
    ('Valid client correction description', True, 'REGC_CLIENT', None, None, DESCRIPTION, None),
    ('Valid amendment owners', True, 'PUBA', None, None, None, OWNER_GROUPS),
    ('Valid staff correction owners', True, 'REGC_STAFF', None, None, None, OWNER_GROUPS),
    ('Valid client correction owners', True, 'REGC_CLIENT', None, None, None, OWNER_GROUPS),
    ('Valid amendment status', True, 'PUBA', 'ACTIVE', None, None, None),
    ('Valid staff correction status', True, 'REGC_STAFF', 'EXEMPT', None, None, None),
    ('Invalid client correction status', False, 'REGC_CLIENT', 'JUNK', None, None, None),
    ('Invalid client correction location', False, 'REGC_CLIENT', None, LOCATION, None, None),
    ('Invalid staff correction description', False, 'REGC_STAFF', None, None, DESCRIPTION, None),
    ('Invalid amendment owners', False, 'PUBA', None, None, None, OWNER_GROUPS),
]


@pytest.mark.parametrize('desc,valid,doc_type,has_sub,is_request,client_ref,attention', TEST_DATA)
def test_admin_registration(desc, valid, doc_type, has_sub, is_request, client_ref, attention):
    """Assert that the staff admin registration schema is performing as expected."""
    data = copy.deepcopy(ADMIN_REGISTRATION)
    if not doc_type:
        del data['documentType']
    else:
        data['documentType'] = doc_type
    if not has_sub:
        del data['submittingParty']
    if client_ref:
        data['clientReferenceId'] = client_ref
    else:
        del data['clientReferenceId']
    if attention:
        data['attentionReference'] = attention
    else:
        del data['attentionReference']
    if is_request:
        del data['mhrNumber']
        del data['createDateTime']
        del data['payment']
        del data['registrationType']
    if desc == 'Invalid update doc id':
        data['updateDocumentId'] = '123456789'
    elif desc in ('Valid request STAT',
                  'Valid request CANCEL_PERMIT',
                  'Valid response CANCEL_PERMIT'):
        data['location'] = copy.deepcopy(LOCATION)
        if desc in ('Valid request CANCEL_PERMIT', 'Valid response CANCEL_PERMIT'):
            data['documentType'] = 'CANCEL_PERMIT'
            data['registrationType'] = 'REG_STAFF_ADMIN'
    is_valid, errors = validate(data, 'adminRegistration', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,doc_type,status,location,description,owner_group', TEST_DATA_AMEND_CORRECT)
def test_admin_amend_correct(desc, valid, doc_type, status, location, description, owner_group):
    """Assert that the staff admin registration schema is performing as expected for amendments/corrections."""
    data = copy.deepcopy(ADMIN_REGISTRATION)
    data['documentType'] = doc_type
    del data['mhrNumber']
    del data['createDateTime']
    del data['payment']
    del data['registrationType']
    if status:
        data['status'] = status
    if location:
        if valid:
            data['location'] = location
        else:
            bad_location = copy.deepcopy(location)
            del bad_location['locationType']
            data['location'] = bad_location
    if description:
        if valid:
            data['description'] = description
        else:
            bad_desc = copy.deepcopy(description)
            del bad_desc['sections']
            data['description'] = bad_desc
    if owner_group:
        data['deleteOwnerGroups'] = owner_group
        if valid:
            data['addOwnerGroups'] = owner_group
        else:
            bad_owners = copy.deepcopy(owner_group)
            del bad_owners[0]['type']
            data['addOwnerGroups'] = bad_owners

    is_valid, errors = validate(data, 'adminRegistration', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
