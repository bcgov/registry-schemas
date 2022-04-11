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
"""Test Suite to ensure the MHR section information schema is valid."""

import pytest

from registry_schemas import validate


# testdata pattern is ({desc}, {valid}, {serial}, {lengthFeet}, {lengthIn}, {widthFeet}, {widthIn})
TEST_DATA_SECTION = [
    ('Valid all', True, 'serial123', 50, 2, 12, 10),
    ('Valid no length inches', True, 'serial123', 50, None, 12, 10),
    ('Valid no width inches', True, 'serial123', 50, 2, 12, None),
    ('Valid minimal', True, 'serial123', 50, None, 12, None),
    ('Invalid missing serial', False, None, 50, 2, 12, 10),
    ('Invalid missing length feet', False, 'serial123', None, 2, 12, 10),
    ('Invalid missing width feet', False, 'serial123', 50, 2, None, 10),
    ('Invalid serial too long', False, '012345678901234567890', 50, 2, 12, 10)
]


@pytest.mark.parametrize('desc,valid,serial,length_feet,length_in,width_feet,width_in', TEST_DATA_SECTION)
def test_base_info(desc, valid, serial, length_feet, length_in, width_feet, width_in):
    """Assert that the schema is performing as expected."""
    data = {
        'serialNumber': serial,
        'lengthFeet': length_feet,
        'lengthInches': length_in,
        'widthFeet': width_feet,
        'widthInches': width_in
    }
    is_valid, errors = validate(data, 'sectionInformation', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
