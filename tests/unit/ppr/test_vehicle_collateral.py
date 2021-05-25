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
    ('EV', True),
    ('MH', True),
    ('MV', True),
    ('OB', True),
    ('TR', True),
    ('XX', False)
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


def test_invalid_vehicle_serial():
    """Assert that an invalid vehicleCollateral fails - serial number too long."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['serialNumber'] = '123434342XXXXXXXXXXXXXXXXXXXXXXXXXXX'

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
    vehicle['make'] = '123434342XXXXXXXXXXXXXXXXXXXXXXXXXXX'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_vehicle_model():
    """Assert that an invalid vehicleCollateral fails - model too long."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['model'] = '123434342XXXXXXXXXXXXXXXXXXXXXXXXXXX'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_vehicle_mhr_number():
    """Assert that an invalid vehicleCollateral fails - MHR registration number too long."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['manufacturedHomeRegistrationNumber'] = '123456789'

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
