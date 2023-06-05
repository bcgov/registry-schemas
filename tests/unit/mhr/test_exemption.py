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
from registry_schemas.example_data.mhr import EXEMPTION


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
LONG_ATTENTION_REF = LONG_CLIENT_REF

# testdata pattern is ({desc},{valid},{sub_party},{has_note},{is_request},{client_ref},{attn_ref})
TEST_DATA = [
    ('Valid request', True, PARTY_VALID, True, True, '1234', '1234'),
    ('Valid response', True, PARTY_VALID, True, False, '1234', '1234'),
    ('Valid no client ref', True, PARTY_VALID, True, True, None, '1234'),
    ('Valid no attention ref', True, PARTY_VALID, True, True, '1234', None),
    ('Valid no note', True, PARTY_VALID, False, True, '1234', '1234'),
    ('Invalid client ref', False, PARTY_VALID, True, True, LONG_CLIENT_REF, '1234'),
    ('Invalid attention ref', False, PARTY_VALID, True, True, '1234', LONG_ATTENTION_REF),
    ('Invalid sub party', False, PARTY_INVALID, True, True, True, '1234'),
    ('Missing sub party', False, None, True, True, True, '1234')
]


@pytest.mark.parametrize('desc,valid,sub_party,has_note,is_request,client_ref,attn_ref', TEST_DATA)
def test_exemption(desc, valid, sub_party, has_note, is_request, client_ref, attn_ref):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(EXEMPTION)
    if sub_party:
        data['submittingParty'] = sub_party
    else:
        del data['submittingParty']
    if client_ref:
        data['clientReferenceId'] = client_ref
    else:
        del data['clientReferenceId']
    if attn_ref:
        data['attentionReference'] = attn_ref
    else:
        del data['attentionReference']
    if not has_note:
        del data['note']
    if is_request:
        del data['createDateTime']
        del data['payment']
        del data['mhrNumber']
        del data['documentId']
        del data['documentRegistrationNumber']
        del data['documentDescription']
        del data['registrationType']

    is_valid, errors = validate(data, 'exemption', 'mhr')

    if errors:
        for err in errors:
            print(err.message)
    if valid:
        assert is_valid
    else:
        assert not is_valid
