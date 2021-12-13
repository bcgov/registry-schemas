# Copyright © 2019 Province of British Columbia
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
"""Example PPR JSON segments and statements that are known to work.

These can be used in other tests as basis for the JSON registration statements.
"""
from .schema_data import ADDRESS, EVENT_TRACKING, PARTY, PAYMENT_REFERENCE, PERSON_NAME, USER, USER_PROFILE


__all__ = [
    'ADDRESS',
    'EVENT_TRACKING',
    'PARTY',
    'PAYMENT_REFERENCE',
    'PERSON_NAME',
    'USER',
    'USER_PROFILE'
]
