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
from registry_schemas.example_data.mhr import NOTE_REGISTRATION


LONG_CLIENT_REF = '012345678901234567890123456789012345678901234567890'
# testdata pattern is ({desc},{valid},{has_note},{has_submitting},{is_request},{client_ref}, {attention})
TEST_DATA = [
    ('Valid request', True, True, True, True, None, None),
    ('Valid response', True, True, True, False, '1234', 'JOHN SMITH'),
    ('Invalid client ref', False, True, True, True, LONG_CLIENT_REF, None),
    ('Invalid attention', False, True, True, True, None, LONG_CLIENT_REF),
    ('Invalid missing note', False, False, True, True, None, None),
    ('Invalid missing sub party', False, True, False, True, None, None)
]


@pytest.mark.parametrize('desc,valid,has_note,has_sub,is_request,client_ref,attention', TEST_DATA)
def test_note_registration(desc, valid, has_note, has_sub, is_request, client_ref, attention):
    """Assert that the unit note registration schema is performing as expected."""
    data = copy.deepcopy(NOTE_REGISTRATION)
    if not has_note:
        del data['note']
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
        if has_note:
            del data['note']['documentId']
            del data['note']['createDateTime']
            del data['note']['status']
            del data['note']['documentDescription']
            del data['note']['documentRegistrationNumber']
    is_valid, errors = validate(data, 'noteRegistration', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
