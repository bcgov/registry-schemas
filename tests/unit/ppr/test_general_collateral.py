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
"""Test Suite to ensure the PPR general collateral schema is valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data.ppr import GENERAL_COLLATERAL


def test_valid_general_collateral():
    """Assert that the schema is performing as expected."""
    is_valid, errors = validate(GENERAL_COLLATERAL, 'generalCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_general_collateral_description():
    """Assert that an invalid generalCollateral fails - description too short."""
    collateral = copy.deepcopy(GENERAL_COLLATERAL)
    collateral['description'] = 'XX'

    is_valid, errors = validate(collateral, 'generalCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_general_collateral_added():
    """Assert that an invalid generalCollateral fails - added date time invalid format."""
    collateral = copy.deepcopy(GENERAL_COLLATERAL)
    collateral['addedDateTime'] = 'XXXXXXXXXXXX'

    is_valid, errors = validate(collateral, 'generalCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_general_collateral_missing_description():
    """Assert that an invalid generalCollateral fails - description is missing."""
    collateral = copy.deepcopy(GENERAL_COLLATERAL)
    del collateral['description']

    is_valid, errors = validate(collateral, 'generalCollateral', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
