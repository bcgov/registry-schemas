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
"""Test Suite to ensure the MHR location schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data.mhr import ADDRESS, LOCATION


LONG_NAME = '01234567890123456789012345678901234567890'
LONG_NAME_MAX = '0123456789012345678901234567890123456789'
DEALER_NAME_MAX = '012345678901234567890123456789012345678901234567890123456789'
DESCRIPTION_MAX = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'
VALID_TIMESTAMP = '2022-05-14T21:16:32+00:00'
LTSA_MAX = '0123456789'
LTSA_DISTRICT_MAX = '01234567890123456'
LTSA_LAND_DISTRICT_MAX = '01234567890123456789'
LTSA_PLAN_MAX = '012345678901'
# testdata pattern is ({desc}, {valid}, {park_name}, {pad}, {address}, {pid}, {tax_date}, {dealer})
TEST_DATA_LOCATION = [
    ('Valid', True, 'park name', '1234', ADDRESS, None, None, None),
    ('Valid no park name', True, None, '1234', ADDRESS, None, None, None),
    ('Valid no pad', True, LONG_NAME_MAX, None, ADDRESS, None, None, None),
    ('Valid no pad, park name', True, None, None, ADDRESS, None, None, None),
    ('Valid pid', True, LONG_NAME_MAX, None, ADDRESS, '123456789', None, None),
    ('Valid tax date', True, LONG_NAME_MAX, None, ADDRESS, '123456789', VALID_TIMESTAMP, None),
    ('Valid dealer', True, LONG_NAME_MAX, None, ADDRESS, '123456789', None, DEALER_NAME_MAX),
    ('Invalid missing address', False, 'org name', '1234', None, None, None, None),
    ('Invalid pad too long', False, 'park name', '1234567', ADDRESS, None, None, None),
    ('Invalid pid too long', False, 'park name', '1234', ADDRESS, '0123456789', None, None),
    ('Invalid dealer too long', False, 'park name', '1234', ADDRESS, None, None, DEALER_NAME_MAX + 'x'),
    # ('Invalid tax date', False, LONG_NAME_MAX, None, ADDRESS, '123456789', 'invalid format', None),
    ('Invalid park name too long', False, LONG_NAME, None, ADDRESS, None, None, None)
]
# testdata pattern is ({desc}, {valid}, {exception}, {additional})
TEST_DATA_LOCATION_DESCRIPTIONS = [
    ('Valid both max lengths', True, DESCRIPTION_MAX, DESCRIPTION_MAX),
    ('Invalid exception plan too long', False, DESCRIPTION_MAX + 'X', DESCRIPTION_MAX),
    ('Invalid additional too long', False, DESCRIPTION_MAX, DESCRIPTION_MAX + 'X')
]
# testdata pattern is ({desc},{valid},{lot},{parcel},{block},{dlot},{part},{section},
# {town},{range},{meridian},{dland},{plan})
TEST_DATA_LOCATION_LTSA = [
    ('Valid max lengths', True, LTSA_MAX, LTSA_MAX, LTSA_MAX, LTSA_DISTRICT_MAX, LTSA_MAX, LTSA_MAX,
     '12', '12', '123', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX),
    ('Invalid lot too long', False, LTSA_MAX + 'X', LTSA_MAX, LTSA_MAX, LTSA_DISTRICT_MAX, LTSA_MAX, LTSA_MAX,
     '12', '12', '123', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX),
    ('Invalid parcel too long', False, LTSA_MAX, LTSA_MAX + 'X', LTSA_MAX, LTSA_DISTRICT_MAX, LTSA_MAX, LTSA_MAX,
     '12', '12', '123', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX),
    ('Invalid block too long', False, LTSA_MAX, LTSA_MAX, LTSA_MAX + 'X', LTSA_DISTRICT_MAX, LTSA_MAX, LTSA_MAX,
     '12', '12', '123', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX),
    ('Invalid dlot too long', False, LTSA_MAX, LTSA_MAX, LTSA_MAX, LTSA_DISTRICT_MAX + 'X', LTSA_MAX, LTSA_MAX,
     '12', '12', '123', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX),
    ('Invalid part too long', False, LTSA_MAX, LTSA_MAX, LTSA_MAX, LTSA_DISTRICT_MAX, LTSA_MAX + 'X', LTSA_MAX,
     '12', '12', '123', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX),
    ('Invalid section too long', False, LTSA_MAX, LTSA_MAX, LTSA_MAX, LTSA_DISTRICT_MAX, LTSA_MAX, LTSA_MAX + 'X',
     '12', '12', '123', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX),
    ('Invalid town too long', False, LTSA_MAX, LTSA_MAX, LTSA_MAX, LTSA_DISTRICT_MAX, LTSA_MAX, LTSA_MAX,
     '123', '12', '123', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX),
    ('Invalid range too long', False, LTSA_MAX, LTSA_MAX, LTSA_MAX, LTSA_DISTRICT_MAX, LTSA_MAX, LTSA_MAX,
     '12', '123', '123', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX),
    ('Invalid meridian too long', False, LTSA_MAX, LTSA_MAX, LTSA_MAX, LTSA_DISTRICT_MAX, LTSA_MAX, LTSA_MAX,
     '12', '12', '1234', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX),
    ('Invalid dland too long', False, LTSA_MAX, LTSA_MAX, LTSA_MAX, LTSA_DISTRICT_MAX, LTSA_MAX, LTSA_MAX,
     '12', '12', '123', LTSA_LAND_DISTRICT_MAX + 'X', LTSA_PLAN_MAX),
    ('Invalid plan too long', False, LTSA_MAX, LTSA_MAX, LTSA_MAX, LTSA_DISTRICT_MAX, LTSA_MAX, LTSA_MAX,
     '12', '12', '123', LTSA_LAND_DISTRICT_MAX, LTSA_PLAN_MAX + 'X')
]


@pytest.mark.parametrize('desc,valid,park_name,pad,address,pid,tax_date,dealer', TEST_DATA_LOCATION)
def test_location(desc, valid, park_name, pad, address, pid, tax_date, dealer):
    """Assert that the schema is performing as expected."""
    data = {
        'address': address
    }
    if park_name:
        data['parkName'] = park_name
    if pad:
        data['pad'] = pad
    if not address:
        del data['address']
    if pid:
        data['pidNumber'] = pid
    if tax_date:
        data['taxExpiryDate'] = tax_date
    if dealer:
        data['dealerName'] = dealer

    is_valid, errors = validate(data, 'location', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,exception,additional', TEST_DATA_LOCATION_DESCRIPTIONS)
def test_location_descriptions(desc, valid, exception, additional):
    """Assert that the schema descriptions valiation is performing as expected."""
    data = copy.deepcopy(LOCATION)
    data['exceptionPlan'] = exception
    data['additionalDescription'] = additional
    is_valid, errors = validate(data, 'location', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid


@pytest.mark.parametrize('desc,valid,lot,parcel,block,dlot,part,section,town,range,meridian,dland,plan',
                         TEST_DATA_LOCATION_LTSA)
def test_location_ltsa(desc, valid, lot, parcel, block, dlot, part, section, town, range, meridian, dland, plan):
    """Assert that the schema ltsa field valiation is performing as expected."""
    data = copy.deepcopy(LOCATION)
    data['lot'] = lot
    data['parcel'] = parcel
    data['block'] = block
    data['districtLot'] = dlot
    data['partOf'] = part
    data['section'] = section
    data['township'] = town
    data['range'] = range
    data['meridian'] = meridian
    data['landDistrict'] = dland
    data['plan'] = plan
    is_valid, errors = validate(data, 'location', 'mhr')

    if errors:
        for err in errors:
            print(err.message)

    if valid:
        assert is_valid
    else:
        assert not is_valid
