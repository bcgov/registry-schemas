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
from registry_schemas.example_data.mhr import PERMIT


LONG_CLIENT_REF = '012345678901234567890123456789012345678901234567890'
# testdata pattern is ({desc},{valid},{sub_party},{owner},{existing},{new},{is_request},{client_ref})
TEST_DATA = [
    ('Valid request', True, True, True, True, True, True, None),
    ('Valid response', True, True, True, True, True, False, '1234'),
    ('Invalid client ref', False, True, True, True, True, True, LONG_CLIENT_REF),
    ('Invalid missing sub party', False, False, True, True, True, True, '1234'),
    ('Invalid missing owner', False, True, False, True, True, True, '1234'),
    ('Invalid missing existing location', False, True, True, False, True, True, ''),
    ('Invalid missing new location', False, True, True, True, False, True, ''),
]


@pytest.mark.parametrize('desc,valid,sub_party,owner,existing,new,is_request,client_ref', TEST_DATA)
def test_permit(desc, valid, sub_party, owner, existing, new, is_request, client_ref):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(PERMIT)
    if not sub_party:
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
        del data['documentRegistrationNumber']
        del data['registrationType']
        del data['note']
    else:
        del data['landStatusConfirmation']
        del data['note']
    if not owner:
        del data['owner']
    if not existing:
        del data['existingLocation']
    if not new:
        del data['newLocation']
    is_valid, errors = validate(data, 'permit', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
