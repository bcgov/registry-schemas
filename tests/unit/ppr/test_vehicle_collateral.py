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
"""Test Suite to ensure the PPR vehicle collateral schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.ppr import VEHICLE_COLLATERAL


# testdata pattern is ({vehicle type}, {is valid})
TEST_DATA_VEHICLE_TYPE = [
    ('AC', True),
    ('AF', True),
    ('AP', True),
    ('BO', True),
    ('MH', True),
    ('MV', True),
    ('OB', True),
    ('TR', True),
    ('XX', False)
]

# testdata pattern is ({vehicle type}, {serial number}, {mhr number}, {is valid}, {has_make}, {has_model})
TEST_DATA_SERIAL_NUMBER = [
    ('AC', 'CFYXW', None, True, True, True),
    ('AC', None, '123456', False, True, True),
    ('AF', '12343424', None, True, True, True),
    ('AF', None, '123456', False, True, True),
    ('AP', 'ABDCD12343', None, True, True, True),
    ('AP', None, '123456', False, True, True),
    ('BO', '13434X', None, True, True, True),
    ('BO', None, '123456', False, True, True),
    ('MH', '002434', None, True, True, True),
    ('MH', '002434', None, True, False, True),
    ('MH', '002434', None, True, True, False),
    ('MH', None, '123456', True, True, True),
    ('MH', '002434', '123456', True, True, True),
    ('MH', None, None, False, True, True),
    ('MV', '242342342', None, True, True, True),
    ('MV', '242342342', None, False, False, True),
    ('MV', '242342342', None, False, True, False),
    ('MV', None, '123456', False, True, True),
    ('OB', 'xsfsfd132', None, True, True, True),
    ('OB', None, '123456', False, True, True),
    ('TR', 'TR32324', None, True, True, True),
    ('TR', None, '123456', False, True, True)
]


@pytest.mark.parametrize('vehicle_type, valid', TEST_DATA_VEHICLE_TYPE)
def test_vehicle_type(vehicle_type, valid):
    """Assert that the schema is performing as expected for all serial collateral types."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['type'] = vehicle_type

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('vehicle_type, serial_number, mhr_number, valid, has_make, has_model', TEST_DATA_SERIAL_NUMBER)
def test_serial_number(vehicle_type, serial_number, mhr_number, valid, has_make, has_model):
    """Assert that the schema is performing as expected for all serial collateral type - serial number combinations."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['type'] = vehicle_type
    if serial_number is None:
        del vehicle['serialNumber']
    else:
        vehicle['serialNumber'] = serial_number
    if not has_make:
        del vehicle['make']
    if not has_model:
        del vehicle['model']
    if mhr_number is not None:
        vehicle['manufacturedHomeRegistrationNumber'] = mhr_number

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


def test_invalid_vehicle_serial():
    """Assert that an invalid vehicleCollateral fails - serial number too long."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['serialNumber'] = '012345678901234567890123456789X'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_vehicle_year():
    """Assert that an invalid vehicleCollateral fails - year outside 1900 - 2100."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['year'] = 2220

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_vehicle_make():
    """Assert that an invalid vehicleCollateral fails - make too long."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['make'] = '012345678901234567890123456789012345678901234567890123456789x'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_vehicle_model():
    """Assert that an invalid vehicleCollateral fails - model too long."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['model'] = '012345678901234567890123456789012345678901234567890123456789x'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_vehicle_mhr_number():
    """Assert that an invalid vehicleCollateral fails - MHR registration number too long."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['manufacturedHomeRegistrationNumber'] = '1234567'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_vehicle_missing_type():
    """Assert that an invalid vehicleCollateral fails - type is missing."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    del vehicle['type']

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_vehicle_missing_serial():
    """Assert that an invalid vehicleCollateral fails - serial number is missing."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    del vehicle['serialNumber']

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
