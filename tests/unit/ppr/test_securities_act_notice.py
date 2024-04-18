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
"""Test Suite to ensure the PPR securities act notice information schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.ppr import COURT_ORDER


SECURITIES_ACT_NOTICE = {
    'securitiesActNoticeType': 'LIEN',
    'effectiveDateTime': '2024-02-02T00:00:00-08:00',
    'description': 'TEST LIEN NOTICE TYPE'
}


# testdata pattern is ({desc}, {valid}, {sec_type}, {effective_dt}, {has_orders}, {court_order})
TEST_DATA = [
    ('Valid LIEN', True, 'LIEN', '2024-04-12T06:59:59-07:00', True, True),
    ('Valid PRESERVATION', True, 'PRESERVATION', '2024-04-12T06:59:59-07:00', False, None),
    ('Valid PROCEEDINGS', True, 'PROCEEDINGS', '2024-04-12T06:59:59-07:00', True, True),
    ('Valid LIEN minimal', True, 'LIEN', None, False, None),
    ('Invalid notice type', False, 'JUNK', '2024-04-12T06:59:59-07:00', True, True),
    ('Invalid no notice type', False, None, '2024-04-12T06:59:59-07:00', True, True),
    ('Invalid missing courtOrder', False, 'LIEN', None, True, None)
]


@pytest.mark.parametrize('desc,valid,sec_type,effective_dt,has_orders,court_order', TEST_DATA)
def test_securities_act_notice(desc, valid, sec_type, effective_dt, has_orders, court_order):
    """Assert that the schema is performing as expected."""
    notice = copy.deepcopy(SECURITIES_ACT_NOTICE)
    if has_orders:
        orders = []
        order = copy.deepcopy(COURT_ORDER)
        if court_order:
            order['courtOrder'] = court_order
        orders.append(order)
        notice['securitiesActOrders'] = orders

    if not sec_type:
        del notice['securitiesActNoticeType']
    else:
        notice['securitiesActNoticeType'] = sec_type
    if not effective_dt:
        del notice['effectiveDateTime']
    else:
        notice['effectiveDateTime'] = effective_dt

    is_valid, errors = validate(notice, 'securitiesActNotice', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
        print(errors)

    if valid:
        assert is_valid
    else:
        assert not is_valid
