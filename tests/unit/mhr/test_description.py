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
"""Test Suite to ensure the MHR description schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import DESCRIPTION


TEXT_60 = '012345678901234567890123456789012345678901234567890123456789'
TEXT_30 = '012345678901234567890123456789'
REBUILT_MAX_LENGTH = TEXT_60 + TEXT_60 + TEXT_60 + TEXT_60 + TEXT_60
OTHER_MAX_LENGTH = TEXT_60 + TEXT_60 + TEXT_30
MANUFACTURER_MAX_LENGTH = TEXT_60 + TEXT_60 + TEXT_60 + TEXT_60 + TEXT_60 + '0123456789'
LONG_ENG_NAME = TEXT_60 + TEXT_60 + TEXT_30
# testdata pattern is ({desc}, {valid}, {manu}, {base}, {sc}, {has_s}, {csa_n}, {csa_s}, {eng_date}, {eng_name})
TEST_DATA_DESC = [
    ('Valid all', True, 'manufacturer', True, 1, True, 'csa num', 'csas', True, 'eng name'),
    ('Valid no csa', True, 'manufacturer', True, 1, True, None, None, True, 'eng name'),
    ('Valid no eng', True, 'manufacturer', True, 1, True, 'csa num', 'csas', False, None),
    ('Valid eng max length', True, 'manufacturer', True, 1, True, 'csa num', 'csas', False, LONG_ENG_NAME),
    ('Valid manu max long', True, MANUFACTURER_MAX_LENGTH, True, 1, True, 'csa num', 'csas', True, 'eng name'),
    ('Invalid no manufacturer', False, None, True, 1, True, 'csa num', 'csas', True, 'eng name'),
    ('Invalid no base info', False, 'manufacturer', False, 1, True, 'csa num', 'csas', True, 'eng name'),
    ('Invalid no section count', False, 'manufacturer', True, None, True, 'csa num', 'csas', True, 'eng name'),
    ('Invalid no sections', False, 'manufacturer', True, 1, False, 'csa num', 'csas', True, 'eng name'),
    ('Invalid no csa,eng', False, 'manufacturer', True, 1, True, None, None, False, None),
    ('Invalid manu too long', False, MANUFACTURER_MAX_LENGTH + 'X', True, 1, True, 'csa num', 'csas', True, 'eng name'),
    ('Invalid csa num too long', False, 'manufacturer', True, 1, True, '01234567890', 'csas', True, 'eng name'),
    ('Invalid csa standard too long', False, 'manufacturer', True, 1, True, '0123456789', '12345', True, 'eng name'),
    ('Invalid eng name too long', False, 'manufacturer', True, 1, True, '012345678', 'csas', True, LONG_ENG_NAME + 'X')
]
# testdata pattern is ({desc}, {valid}, {rebuilt}, {other})
TEST_REMARKS_DATA_DESC = [
    ('Valid Max Both', True, REBUILT_MAX_LENGTH, OTHER_MAX_LENGTH),
    ('Invalid rebuilt too long', False, REBUILT_MAX_LENGTH + 'X', OTHER_MAX_LENGTH),
    ('Invalid other too long', False, REBUILT_MAX_LENGTH, OTHER_MAX_LENGTH + 'X')
]


@pytest.mark.parametrize('desc,valid,manu,base,sc,has_s,csa_n,csa_s,eng_date,eng_name', TEST_DATA_DESC)
def test_description(desc, valid, manu, base, sc, has_s, csa_n, csa_s, eng_date, eng_name):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(DESCRIPTION)
    data['manufacturer'] = manu
    if not sc:
        del data['sectionCount']
    if not has_s:
        del data['sections']
    if not base:
        del data['baseInformation']
    if not csa_n:
        del data['csaNumber']
    else:
        data['csaNumber'] = csa_n
    if not csa_s:
        del data['csaStandard']
    else:
        data['csaStandard'] = csa_s
    if not eng_date:
        del data['engineerDate']
    if not eng_name:
        del data['engineerName']
    else:
        data['engineerName'] = eng_name

    is_valid, errors = validate(data, 'description', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,rebuilt,other', TEST_REMARKS_DATA_DESC)
def test_description_remarks(desc, valid, rebuilt, other):
    """Assert that the schema remarks validation is performing as expected."""
    data = copy.deepcopy(DESCRIPTION)
    data['rebuiltRemarks'] = rebuilt
    data['otherRemarks'] = other
    is_valid, errors = validate(data, 'description', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
