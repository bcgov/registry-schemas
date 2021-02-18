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
"""Test Suite to ensure the PPR payment reference schema is valid.

"""
import copy

from registry_schemas import validate
from registry_schemas.example_data.common import PAYMENT_REFERENCE


def test_valid_payment():
    """Assert that the schema is performing as expected."""
    is_valid, errors = validate(PAYMENT_REFERENCE, 'paymentReference', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_invalid_payment_receipt():
    """Assert that an invalid payment fails - receipt too short."""
    payment = copy.deepcopy(PAYMENT_REFERENCE)
    payment['receipt'] = 'Too short'

    is_valid, errors = validate(payment, 'paymentReference', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_payment_invoice():
    """Assert that an invalid payment fails - invoiceId too long."""
    payment = copy.deepcopy(PAYMENT_REFERENCE)
    payment['invoiceId'] = 'This is a really long invoiceId'

    is_valid, errors = validate(payment, 'paymentReference', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_address_missing_invoice():
    """Assert that an invalid address fails - missing required field invoiceId."""
    payment = copy.deepcopy(PAYMENT_REFERENCE)
    del payment['invoiceId']

    is_valid, errors = validate(payment, 'paymentReference', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_address_missing_receipt():
    """Assert that an invalid address fails - missing required field receipt."""
    payment = copy.deepcopy(PAYMENT_REFERENCE)
    del payment['receipt']

    is_valid, errors = validate(payment, 'paymentReference', 'common')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
