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
"""Sample data used across many tests."""
# pylint: disable=too-many-lines

ADDRESS = {
    'street': 'delivery_address - address line one',
    'streetAdditional': 'line 2',
    'city': 'delivery_address city',
    'country': 'CA',
    'postalCode': 'H0H0H0',
    'region': 'BC'
}

PARTY = {
    'personName': {
        'first': 'Michael',
        'middle': 'J',
        'last': 'Smith'
    },
    'address': {
        'street': '520 Johnson St',
        'city': 'Victoria',
        'region': 'BC',
        'country': 'CA',
        'postalCode': 'V8S 2V4'
    },
    'emailAddress': 'msmith@gmail.com',
    'birthDate': '1986-12-01T19:20:20-08:00',
    'partyId': 1321064
}

PAYMENT_REFERENCE = {
    'invoiceId': '2198743',
    'receipt': '/pay/api/v1/payment-requests/2198743/receipts'
}

PERSON_NAME = {
    'first': 'Michael',
    'middle': 'J',
    'last': 'Smith'
}

USER = {
    'creationDate': '2021-04-01T16:20:20+00:00',
    'username': 'bcsc/avyw3cbumorr91k7f5uq2i3mzcqrm4av',
    'sub': 'fd362600-x234-9115-c427-fed859c6d093',
    'iss': 'https://dev.oidc.gov.bc.ca/auth/realms/fcf0kpqr',
    'firstname': 'Michael',
    'lastname': 'Smith',
    'email': 'msmith@gmail.com',
    'accountId': '12345'
}

USER_PROFILE = {
    'paymentConfirmationDialog': True,
    'selectConfirmationDialog': False,
    'defaultDropDowns': True,
    'defaultTableFilters': False
}
