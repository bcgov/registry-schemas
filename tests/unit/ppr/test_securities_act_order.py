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
"""Test Suite to ensure the PPR securities act order information schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.ppr import COURT_ORDER


# testdata pattern is ({desc}, {valid}, {name}, {registry}, {file_num}, {order_date}, {effect}, {court_order})
TEST_DATA = [
    ('Valid', True, 'default', 'default', 'default', 'default', 'default', True),
    ('Valid minimal', True, None, None, None, None, None, True),
    ('Invalid no court_order', False, 'default', 'default', 'default', 'default', 'default', None),
    ('Invalid name', False, 'XX', 'default', 'default', 'default', 'default', False),
    ('Invalid registry', False, 'default', 'XX', 'default', 'default', 'default', False),
    ('Invalid file number', False, 'default', 'default', 'FILE NUMBER TOO LONGXXXX', 'default', 'default', False),
    ('Invalid order date', False, 'default', 'default', 'default', 'XXXXXXXX', 'default', False),
    ('Invalid effect of order', False, 'default', 'default', 'default', 'default', 'XX', False)
]


@pytest.mark.parametrize('desc,valid,name,registry,file_num,order_date,effect,court_order', TEST_DATA)
def test_securities_act_order(desc, valid, name, registry, file_num, order_date, effect, court_order):
    """Assert that the schema is performing as expected."""
    order = copy.deepcopy(COURT_ORDER)
    if name and name != 'default':
        order['courtName'] = name
    elif not name:
        del order['courtName']
    if registry and registry != 'default':
        order['courtRegistry'] = registry
    elif not registry:
        del order['courtRegistry']
    if file_num and file_num != 'default':
        order['fileNumber'] = file_num
    elif not file_num:
        del order['fileNumber']
    if order_date and order_date != 'default':
        order['orderDate'] = order_date
    elif not order_date:
        del order['orderDate']
    if effect and effect != 'default':
        order['effectOfOrder'] = effect
    elif not effect:
        del order['effectOfOrder']
    if court_order is not None:
        order['courtOrder'] = court_order

    is_valid, errors = validate(order, 'securitiesActOrder', 'ppr')

    if errors:
        for err in errors:
            print(err.message)
        print(errors)

    if valid:
        assert is_valid
    else:
        assert not is_valid
