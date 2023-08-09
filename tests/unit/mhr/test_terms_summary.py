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
from registry_schemas.example_data.mhr import TERMS_SUMMARY


# testdata pattern is ({desc},{valid},{ttype},{version},{latest},{create_ts},{accepted})
TEST_DATA_TERMS = [
    ('Valid list GET', True, 'DEFAULT', 'v1', True, True, None),
    ('Valid POST request', True, None, 'v1', None, None, True),
    ('Valid POST response', True, 'DEFAULT', 'v1', True, None, True),
    ('Valid GET response not accepted', True, 'DEFAULT', 'v1', True, None, False),
    ('Invalid POST request no version', False, 'DEFAULT', None, None, None, True)
]


@pytest.mark.parametrize('desc,valid,ttype,version,latest,create_ts,accepted', TEST_DATA_TERMS)
def test_terms_summary(desc, valid, ttype, version, latest, create_ts, accepted):
    """Assert that the schema is performing as expected."""
    data = copy.deepcopy(TERMS_SUMMARY)
    if not ttype:
        del data['agreementType']
    else:
        data['agreementType'] = ttype
    if version is None:
        del data['version']
    else:
        data['version'] = version
    if latest is None:
        del data['latestVersion']
    else:
        data['latestVersion'] = latest
    if not create_ts:
        del data['createDateTime']
    if accepted is None:
        del data['accepted']
        del data['acceptedDateTime']
    elif not accepted:
        del data['acceptedDateTime']
        data['accepted'] = True
    else:
        data['accepted'] = False
    is_valid, errors = validate(data, 'termsSummary', 'mhr')

    if errors:
        for err in errors:
            print(err.message)
    if valid:
        assert is_valid
    else:
        assert not is_valid
