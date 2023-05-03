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
"""Test Suite to ensure the PPR Draft Summary schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import DRAFT_SUMMARY


# testdata pattern is ({desc}, {valid}, {empty}, {has_id}, {has_type}, {has_path}, {has_create})
TEST_DATA = [
    ('Valid non-empty', True, False, True, True, True, True),
    ('Valid empty', True, True, True, True, True, True),
    ('Invalid missing draftNumber', False, False, False, True, True, True),
    ('Invalid missing type', False, False, True, False, True, True),
    ('Invalid missing path', False, False, True, True, False, True),
    ('Invalid missing createDateTime', False, False, True, True, True, False)
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


@pytest.mark.parametrize('desc,valid,empty,has_id,has_type,has_path,has_create', TEST_DATA)
def test_draft_summary(desc, valid, empty, has_id, has_type, has_path, has_create):
    """Assert that the schema is performing as expected for a draft summary list."""
    drafts = copy.deepcopy(DRAFT_SUMMARY)
    if empty:
        drafts = []
    else:
        if not has_id:
            del drafts[0]['draftNumber']
        if not has_type:
            del drafts[0]['registrationType']
        if not has_path:
            del drafts[0]['path']
        if not has_create:
            del drafts[0]['createDateTime']
    is_valid, errors = validate(drafts, 'draftSummary', 'mhr')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,reg_type', TEST_DATA_REGISTRATION_TYPE)
def test_draft_summary_reg_type(desc, valid, reg_type):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(DRAFT_SUMMARY)
    data[0]['registrationType'] = reg_type

    is_valid, errors = validate(data, 'draftSummary', 'mhr')

    if valid:
        assert is_valid
    else:
        assert not is_valid
