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
from registry_schemas.example_data.mhr import ADMIN_REGISTRATION, LOCATION


LONG_CLIENT_REF = '012345678901234567890123456789012345678901234567890'
# testdata pattern is ({desc},{valid},{doc_type},{has_submitting},{is_request},{client_ref}, {attention})
TEST_DATA = [
    ('Valid request COUR', True, 'COUR', True, True, None, None),
    ('Valid request NRED', True, 'NRED', True, True, None, None),
    ('Valid request NCAN', True, 'NCAN', True, True, None, None),
    ('Valid request REGC', True, 'REGC', True, True, None, None),
    ('Valid request CHANGE_LOCATION', True, 'CHANGE_LOCATION', True, True, None, None),
    ('Valid response', True, 'THAW', True, False, '1234', 'JOHN SMITH'),
    ('Invalid client ref', False, 'NRED', True, True, LONG_CLIENT_REF, None),
    ('Invalid attention', False, 'EXRE', True, True, None, LONG_CLIENT_REF),
    ('Invalid missing doc type', False, None, True, True, None, None),
    ('Invalid doc type', False, 'TAXN', True, True, None, None),
    ('Invalid missing sub party', False, 'NRED', False, True, None, None),
    ('Invalid update doc id', False, 'NRED', True, True, None, None)
]


@pytest.mark.parametrize('desc,valid,doc_type,has_sub,is_request,client_ref,attention', TEST_DATA)
def test_note_registration(desc, valid, doc_type, has_sub, is_request, client_ref, attention):
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
    elif desc in ('Valid request REGC', 'Valid request CHANGE_LOCATION'):
        data['location'] = copy.deepcopy(LOCATION)
    is_valid, errors = validate(data, 'adminRegistration', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
