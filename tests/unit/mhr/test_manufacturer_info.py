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
"""Test Suite to ensure the MHR manufacturer info schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import MANUFACTURER_INFO


NAME_50 = '01234567890123456789012345678901234567890123456789'
DBA_MAX_LENGTH = NAME_50 + NAME_50 + NAME_50
DEALER_MAX_LENGTH = NAME_50 + NAME_50 + NAME_50 + NAME_50 + NAME_50 + NAME_50 + '0123456789'
MANUFACTURER_MAX_LENGTH = DEALER_MAX_LENGTH

# testdata pattern is ({desc},{valid},{bcol},{dealer},{has_submitting},{has_owner},{manufacturer},{dba_name})
TEST_DATA_MANUFACTURER = [
    ('Valid all', True, '123456', 'Dealer', True, True, 'manufacturer', 'dba name'),
    ('Valid no bcol', True, None, 'Dealer', True, True, 'manufacturer', 'dba name'),
    ('Valid max names', True, '123456', DEALER_MAX_LENGTH, True, True, MANUFACTURER_MAX_LENGTH, DBA_MAX_LENGTH),
    ('Invalid bcol too long', False, '1234567', DEALER_MAX_LENGTH, True, True, MANUFACTURER_MAX_LENGTH, None),
    ('Invalid dealer too long', False, '123456', DEALER_MAX_LENGTH + 'X', True, True, MANUFACTURER_MAX_LENGTH,
     'dba name'),
    ('Invalid manufacturer too long', False, '123456', DEALER_MAX_LENGTH, True, True, MANUFACTURER_MAX_LENGTH + 'X',
     'dba name'),
    ('Invalid dba too long', False, None, 'Dealer', True, True, 'manufacturer', DBA_MAX_LENGTH + 'X'),
    ('Invalid missing dealer', False, '123456', None, True, True, MANUFACTURER_MAX_LENGTH, 'dba name'),
    ('Valid missing submitting', True, '123456', DEALER_MAX_LENGTH, False, True, MANUFACTURER_MAX_LENGTH, 'dba name'),
    ('Invalid no owner', False, None, 'Dealer', True, False, 'manufacturer', 'dba name'),
    ('Invalid missing manufacturer', False, '123456', DEALER_MAX_LENGTH, True, True, None, 'dba name')
]


@pytest.mark.parametrize('desc,valid,bcol,dealer,has_submitting,has_owner,manufacturer,dba_name',
                         TEST_DATA_MANUFACTURER)
def test_manufacturer_info(desc, valid, bcol, dealer, has_submitting, has_owner, manufacturer, dba_name):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(MANUFACTURER_INFO)
    if not bcol:
        del data['bcolAccountNumber']
    else:
        data['bcolAccountNumber'] = bcol
    if not dealer:
        del data['location']
    else:
        data['location']['dealerName'] = dealer
    if not manufacturer:
        del data['description']
    else:
        data['description']['manufacturer'] = manufacturer
    if not has_submitting:
        del data['submittingParty']
    if not has_owner:
        del data['ownerGroups'][0]['owners']
    if not dba_name:
        del data['dbaName']
    else:
        data['dbaName'] = dba_name

    is_valid, errors = validate(data, 'manufacturerInfo', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
