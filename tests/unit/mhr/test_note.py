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
"""Test Suite to ensure the MHR note schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import ADDRESS, NOTE


# testdata pattern is ({desc},{valid},{type},{doc_id},{has_create},{has_expiry},{remarks},{contact_name},{address})
LONG_NAME = '01234567890123456789012345678901234567890'
TEST_DATA_NOTE = [
    ('Valid all', True, 'type', '123456', True, True, 'remarks', 'contact', ADDRESS),
    ('Valid no expiry', True, 'type', '123456', True, False, 'remarks', 'contact', ADDRESS),
    ('Valid no remarks', True, 'type', '123456', True, True, None, 'contact', ADDRESS),
    ('Valid no contact', True, 'type', '123456', True, True, 'remarks', None, ADDRESS),
    ('Valid no address', True, 'type', '123456', True, True, 'remarks', 'contact', None),
    ('Invalid no createTS', False, 'type', '123456', False, True, 'remarks', 'contact', ADDRESS),
    ('Invalid no doc id', False, 'type', None, True, True, 'remarks', 'contact', ADDRESS),
    ('Invalid no type', False, None, '123456', True, True, 'remarks', 'contact', ADDRESS),
    ('Invalid type too long', False, '12345', '123456', True, True, 'remarks', 'contact', ADDRESS),
    ('Invalid doc id too long', False, '1234', '123456789', True, True, 'remarks', 'contact', ADDRESS),
    ('Invalid contact too long', False, '1234', '123456', True, True, 'remarks', LONG_NAME, ADDRESS)
]


@pytest.mark.parametrize('desc,valid,type,doc_id,has_create,has_expiry,remarks,contact,address', TEST_DATA_NOTE)
def test_note(desc, valid, type, doc_id, has_create, has_expiry, remarks, contact, address):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(NOTE)
    data['documentType'] = type
    data['documentId'] = doc_id
    if not has_create:
        del data['createDateTime']
    if not has_expiry:
        del data['expiryDate']
    data['remarks'] = remarks
    data['contactName'] = contact
    if not address:
        del data['contactAddress']

    is_valid, errors = validate(data, 'note', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
