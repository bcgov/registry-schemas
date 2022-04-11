# Copyright © 2020 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Sample data used across many tests."""

ADDRESS = {
  'street': 'delivery_address - address line one',
  'city': 'delivery_address city',
  'region': 'BC',
  'postalCode': ' ',
  'country': 'CA'
}

BASE_INFORMATION = {
  'year': 2018,
  'make': 'WATSON IND. (ALTA)',
  'model': 'DUCHESS'
}

DESCRIPTION = {
  'manufacturer': 'STARLINE',
  'baseInformation': {
    'year': 2018,
    'make': 'WATSON IND. (ALTA)',
    'model': 'DUCHESS'
  },
  'sectionCount': 1,
  'sections': [
    {
      'serialNumber': '52D70556',
      'lengthFeet': 52,
      'lengthInches': 0,
      'widthFeet': 12,
      'widthInches': 0
    }
  ],
  'csaNumber': '786356',
  'csaStandard': 'Z240',
  'engineerDate': '2018-02-22T07:59:00+00:00',
  'engineerName': ' Dave Smith ENG. LTD.'
}

LOCATION = {
  'parkName': 'HIDDEN VALLEY TRAILER COURT',
  'pad': '20',
  'address': {
    'street': '940 BLANSHARD STREET',
    'city': 'VICTORIA',
    'region': 'BC',
    'postalCode': ' ',
    'country': 'CA'
  }
}

NOTE = {
  'documentType': 'CONV',
  'documentId': 'REG01234',
  'createDateTime': '2018-02-21T18:56:00+00:00',
  'expiryDate': '2023-02-22T07:59:00+00:00',
  'remarks': '',
  'contactName': 'JOHNNY NUCLEO',
  'contactAddress': {
    'street': '940 BLANSHARD STREET',
    'city': 'VICTORIA',
    'region': 'BC',
    'postalCode': 'V8W 3E6',
    'country': 'CA'
  }
}

OWNER = {
  'organizationName': 'SAGE HILL INC.',
  'address': {
    'street': '3122B LYNNLARK PLACE',
    'city': 'VICTORIA',
    'region': 'BC',
    'postalCode': ' ',
    'country': 'CA'
  },
  'type': 'SO'
}

PAYMENT = {
    'invoiceId': '2198743',
    'receipt': '/pay/api/v1/payment-requests/2198743/receipts'
}

PERSON_NAME = {
    'first': 'Michael',
    'middle': 'J',
    'last': 'Smith'
}

REGISTRATION = {
  'mhrNumber': '001234',
  'status': 'R',
  'clientReferenceId': 'EX-MH001234',
  'declaredValue': '120000.00',
  'owners': [
    {
      'individualName': {
        'first': 'James',
        'last': 'Smith'
      },
      'address': {
        'street': '3122B LYNNLARK PLACE',
        'city': 'VICTORIA',
        'region': 'BC',
        'postalCode': ' ',
        'country': 'CA'
      },
      'type': 'SO'
    }
  ],
  'location': {
    'parkName': 'HIDDEN VALLEY TRAILER COURT',
    'pad': '20',
    'address': {
      'street': '940 BLANSHARD STREET',
      'city': 'VICTORIA',
      'region': 'BC',
      'postalCode': ' ',
      'country': 'CA'
    }
  },
  'description': {
    'manufacturer': 'STARLINE',
    'baseInformation': {
      'year': 2018,
      'make': 'WATSON IND. (ALTA)',
      'model': 'DUCHESS'
    },
    'sectionCount': 1,
    'sections': [
      {
        'serialNumber': '52D70556',
        'lengthFeet': 52,
        'lengthInches': 0,
        'widthFeet': 12,
        'widthInches': 0
      }
    ],
    'csaNumber': '786356',
    'csaStandard': 'Z240'
  },
  'createDateTime': '2020-02-21T18:56:20+00:00',
  'notes': [
    {
      'documentType': 'CONV',
      'documentId': 'REG01234',
      'createDateTime': '1995-02-21T18:56:00+00:00',
      'remarks': '',
      'contactName': 'JOHNNY NUCLEO',
      'contactAddress': {
        'street': '940 BLANSHARD STREET',
        'city': 'VICTORIA',
        'region': 'BC',
        'postalCode': 'V8W 3E6',
        'country': 'CA'
      }
    }
  ],
  'payment': {
    'receipt': '/pay/api/v1/payment-requests/2199700/receipts',
    'invoiceId': '2199700'
  }
}

SEARCH_DETAIL_RESULT = {
  'searchDateTime': '2020-05-14T21:08:32+00:00',
  'totalResultsSize': 1,
  'searchQuery': {
    'type': 'MHR_NUMBER',
    'criteria': {
      'value': '001234'
    }
  },
  'selected': [
    {
      'createDateTime': '2020-02-21T18:56:20Z',
      'mhrNumber': '001234',
      'status': 'ACTIVE',
      'includeLienInfo': False,
      'homeLocation': 'PENTICTON',
      'ownerName': {
        'first': 'James',
        'last': 'Smith'
      },
      'serialNumber': '52D70556',
      'baseInformation': {
        'year': 2018,
        'make': 'WATSON IND. (ALTA)',
        'model': 'DUCHESS'
      }
    }
  ],
  'payment': {
    'receipt': '/pay/api/v1/payment-requests/2198743/receipts',
    'invoiceId': '2198743'
  },
  'details': [
    {
      'mhrNumber': '001234',
      'status': 'R',
      'clientReferenceId': 'EX-MH001234',
      'declaredValue': '120000.00',
      'owners': [
        {
          'individualName': {
            'first': 'James',
            'last': 'Smith'
          },
          'address': {
            'street': '3122B LYNNLARK PLACE',
            'city': 'VICTORIA',
            'region': 'BC',
            'postalCode': ' ',
            'country': 'CA'
          },
          'type': 'SO'
        }
      ],
      'location': {
        'parkName': 'HIDDEN VALLEY TRAILER COURT',
        'pad': '20',
        'address': {
          'street': '940 BLANSHARD STREET',
          'city': 'VICTORIA',
          'region': 'BC',
          'postalCode': ' ',
          'country': 'CA'
        }
      },
      'description': {
        'manufacturer': 'STARLINE',
        'baseInformation': {
          'year': 2018,
          'make': 'WATSON IND. (ALTA)',
          'model': 'DUCHESS'
        },
        'sectionCount': 1,
        'sections': [
          {
            'serialNumber': '52D70556',
            'lengthFeet': 52,
            'lengthInches': 0,
            'widthFeet': 12,
            'widthInches': 0
          }
        ],
        'csaNumber': '786356',
        'csaStandard': 'Z240'
      },
      'notes': [
        {
          'documentType': 'CONV',
          'documentId': 'REG01234',
          'createDateTime': '1995-02-21T18:56:00+00:00',
          'remarks': '',
          'contactName': 'JOHNNY NUCLEO',
          'contactAddress': {
            'street': '940 BLANSHARD STREET',
            'city': 'VICTORIA',
            'region': 'BC',
            'postalCode': 'V8W 3E6',
            'country': 'CA'
          }
        }
      ]
    }
  ]
}

SEARCH_QUERY = {
  'type': 'MHR_NUMBER',
  'criteria': {
    'value': '003456'
  },
  'clientReferenceId': 'EX-00000402'
}

SEARCH_QUERY_RESULT = {
  'searchId': '1294371',
  'searchDateTime': '2020-05-14T21:16:32+00:00',
  'returnedResultsSize': 1,
  'totalResultsSize': 1,
  'maxResultsSize': 1000,
  'searchQuery': {
    'type': 'MHR_NUMBER',
    'criteria': {
      'value': '001234'
    },
    'clientReferenceId': 'EX-00000402'
  },
  'results': [
    {
      'createDateTime': '2020-02-21T18:56:20Z',
      'mhrNumber': '001234',
      'status': 'ACTIVE',
      'includeLienInfo': False,
      'homeLocation': 'PENTICTON',
      'organizationName': 'SAGE HILL INC.',
      'ownerName': {
        'first': 'James',
        'last': 'Smith'
      },
      'serialNumber': '52D70556',
      'baseInformation': {
        'year': 2018,
        'make': 'WATSON IND. (ALTA)',
        'model': 'DUCHESS'
      }
    }
  ]
}

SEARCH_SUMMARY = [
  {
    'mhrNumber': '001234',
    'createDateTime': '2020-02-21T18:56:20Z',
    'status': 'ACTIVE',
    'includeLienInfo': False,
    'homeLocation': 'PENTICTON',
    'ownerName': {
      'first': 'James',
      'last': 'Smith'
    },
    'serialNumber': '52D70556',
    'baseInformation': {
      'year': 2018,
      'make': 'WATSON IND. (ALTA)',
      'model': 'DUCHESS'
    }
  }
]

SECTION_INFORMATION = {
  'serialNumber': '52D70556',
  'lengthFeet': 52,
  'lengthInches': 0,
  'widthFeet': 12,
  'widthInches': 0
}