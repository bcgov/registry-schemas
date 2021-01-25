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
"""Test Suite to ensure the PPR vehicle collateral schema is valid.

"""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import VEHICLE_COLLATERAL


def test_valid_vehicle_MV():
    """Assert that the schema is performing as expected for MV type."""
    is_valid, errors = validate(VEHICLE_COLLATERAL, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_vehicle_AC():
    """Assert that the schema is performing as expected for AC type."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['type'] = 'AC'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_vehicle_AF():
    """Assert that the schema is performing as expected for AF type."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['type'] = 'AF'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_vehicle_BO():
    """Assert that the schema is performing as expected for BO type."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['type'] = 'BO'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_vehicle_EV():
    """Assert that the schema is performing as expected for EV type."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['type'] = 'EV'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_vehicle_MH():
    """Assert that the schema is performing as expected for MH type."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['type'] = 'MH'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_vehicle_OB():
    """Assert that the schema is performing as expected for OB type."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['type'] = 'OB'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_vehicle_TR():
    """Assert that the schema is performing as expected for TR type."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['type'] = 'TR'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_vehicle_type():
    """Assert that an invalid vehicleCollateral fails - invalid type."""
    vehicle = copy.deepcopy(VEHICLE_COLLATERAL)
    vehicle['type'] = 'XX'

    is_valid, errors = validate(vehicle, 'vehicleCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

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


def test_invalid_vehicle_MHR_number():
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

