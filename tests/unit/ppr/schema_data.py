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
"""Test Suite data used across many tests.

Test array used in multiple pytests, and several PPR transactions that can be used in tests.
"""
# testdata pattern is ({str: environment}, {expected return value})
TEST_SCHEMAS_DATA = [
    ('address.json'),
    ('amendmentStatement.json'),
    ('baseDebtor.json'),
    ('changeStatement.json'),
    ('clientParty.json'),
    ('courtOrder.json'),
    ('dischargeStatement.json'),
    ('draft.json'),
    ('draftSummary.json'),
    ('financingStatement.json'),
    ('financingStatementHistory.json'),
    ('generalCollateral.json'),
    ('party.json'),
    ('payment.json'),
    ('personName.json'),
    ('renewalStatement.json'),
    ('searchQuery.json'),
    ('searchQueryResult.json'),
    ('searchSummary.json'),
    ('vehicleCollateral.json')
]
