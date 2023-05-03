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
"""Test Suite to ensure the MHGR Draft schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import DRAFT_TRANSFER


# testdata pattern is ({desc}, {valid}, {type}, {has_reg}, {create}, {update}, {draft_id})
TEST_DATA_TRANSFER = [
    ('Valid TRANS', True, 'TRANS', True, None, None, None),
    ('Valid TRAND', True, 'TRAND', True, None, None, None),
    ('Valid MHREG', True, 'MHREG', True, None, None, None),
    ('Valid PERMIT', True, 'PERMIT', True, None, None, None),
    ('Valid EXEMPTION_RES', True, 'EXEMPTION_RES', True, None, None, None),
    ('Valid EXEMPTION_NON_RES', True, 'EXEMPTION_NON_RES', True, None, None, None),
    ('Invalid missing type', False, None, True, None, None, None),
    ('Invalid type', False, 'XXXXX', True, None, None, None),
    ('Invalid missing registration', False, 'TRANS', False, None, None, None),
    ('Invalid draft id too long', False, 'TRANS', True, None, None, '01234567891')
]

# testdata pattern is ({desc}, {valid}, {type})
TEST_DATA_REGISTRATION_TYPE = [
    ('Valid DECAL_REPLACE', True, 'DECAL_REPLACE'),
    ('Valid EXEMPTION_RES', True, 'EXEMPTION_RES'),
    ('Valid EXEMPTION_NON_RES', True, 'EXEMPTION_NON_RES'),
    ('Valid MHREG', True, 'MHREG'),
    ('Valid PERMIT', True, 'PERMIT'),
    ('Valid PERMIT_EXTENSION', True, 'PERMIT_EXTENSION'),
    ('Valid TRANS', True, 'TRANS'),
    ('Valid TRANS_AFFIDAVIT', True, 'TRANS_AFFIDAVIT'),
    ('Valid TRANS_ADMIN', True, 'TRANS_ADMIN'),
    ('Valid TRANS_WILL', True, 'TRANS_WILL'),
    ('Valid TRAND', True, 'TRAND'),
    ('Valid REG_STAFF_ADMIN', True, 'REG_STAFF_ADMIN'),
    ('Invalid', False, 'JUNKJ')
]


@pytest.mark.parametrize('desc,valid,type,has_reg,create,update,draft_id', TEST_DATA_TRANSFER)
def test_draft(desc, valid, type, has_reg, create, update, draft_id):
    """Assert that the schema is performing as expected for a draft."""
    draft = copy.deepcopy(DRAFT_TRANSFER)
    if not type:
        del draft['type']
    else:
        draft['type'] = type
    if not has_reg:
        del draft['registration']
    if create:
        draft['createDateTime'] = create
    if update:
        draft['lastUpdateDateTime'] = update
    if draft_id:
        draft['draftNumber'] = draft_id

    is_valid, errors = validate(draft, 'draft', 'mhr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,reg_type', TEST_DATA_REGISTRATION_TYPE)
def test_draft_type(desc, valid, reg_type):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(DRAFT_TRANSFER)
    data['type'] = reg_type

    is_valid, errors = validate(data, 'draft', 'mhr')

    if valid:
        assert is_valid
    else:
        assert not is_valid
