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
from registry_schemas.example_data.mhr import QUALIFIED_SUPPLIER


NAME_50 = '01234567890123456789012345678901234567890123456789'
BUS_MAX_LENGTH = NAME_50 + NAME_50 + NAME_50
DBA_MAX_LENGTH = NAME_50 + NAME_50 + NAME_50
LOCATION_ADDRESS = {
    'street': '520 Location St',
    'city': 'Victoria',
    'region': 'BC',
    'country': 'CA',
    'postalCode': 'V8S 2V4'
}


# testdata pattern is ({desc},{valid},{bus},{dba},{phone},{email},{has_address})
TEST_DATA_SUPPLIER = [
    ('Valid all', True, 'BUS NAME', 'DBA NAME', '2501234567', 'test@gmail.com', True),
    ('Valid minimal', True, 'BUS NAME', None, None, None, True),
    ('Valid max names', True, BUS_MAX_LENGTH, DBA_MAX_LENGTH, None, None, True),
    ('Invalid no name', False, None, None, None, None, True),
    ('Invalid no address', False, 'BUS NAME', None, None, None, False),
    ('Invalid phone', False, 'BUS NAME', None, '01234567890', None, True),
    ('Invalid bus name', False, BUS_MAX_LENGTH + 'X', None, None, None, True),
    ('Invalid dba name', False, 'BUS NAME', DBA_MAX_LENGTH + 'X', None, None, True),
    ('Invalid email', False, 'BUS NAME', None, None, 'invalid format', True)
]
# testdata pattern is ({desc},{valid},{confirm_req},{loc_address})
TEST_DATA_DEALER = [
    ('Valid all', True, True, LOCATION_ADDRESS),
    ('Valid no confirm req', True, None, LOCATION_ADDRESS),
    ('Valid confirm req false', True, False, LOCATION_ADDRESS),
    ('Valid no loc address', True, True, None),
    ('Invalid address', False, True, LOCATION_ADDRESS)
]


@pytest.mark.parametrize('desc,valid, confirm_req, loc_address', TEST_DATA_DEALER)
def test_dealer(desc, valid, confirm_req, loc_address):
    """Assert that the schema is performing as expected for dealer information."""
    data = copy.deepcopy(QUALIFIED_SUPPLIER)
    del data['phoneExtension']
    if confirm_req is not None:
        if confirm_req:
            data['confirmRequirements'] = True
        else:
            data['confirmRequirements'] = False
    if loc_address:
        address = copy.deepcopy(loc_address)
        if desc == 'Invalid address':
            del address['postalCode']
        data['locationAddress'] = address

    is_valid, errors = validate(data, 'qualifiedSupplier', 'mhr')

    if errors:
        for err in errors:
            print(err.message)
    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,bus_name,dba_name,phone,email,has_address', TEST_DATA_SUPPLIER)
def test_qualified_supplier(desc, valid, bus_name, dba_name, phone, email, has_address):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(QUALIFIED_SUPPLIER)
    del data['phoneExtension']
    if not bus_name:
        del data['businessName']
    else:
        data['businessName'] = bus_name
    if not dba_name:
        del data['dbaName']
    else:
        data['dbaName'] = dba_name
    if not phone:
        del data['phoneNumber']
    else:
        data['phoneNumber'] = phone
    if not email:
        del data['emailAddress']
    else:
        data['emailAddress'] = email
    if not has_address:
        del data['address']

    is_valid, errors = validate(data, 'qualifiedSupplier', 'mhr')

    if errors:
        for err in errors:
            print(err.message)
    if valid:
        assert is_valid
    else:
        assert not is_valid
