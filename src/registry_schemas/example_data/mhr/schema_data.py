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
  'engineerName': ' Dave Smith ENG. LTD.',
  'rebuiltRemarks': 'Rebuilt comments',
  'otherRemarks': 'Other comments'
}

DRAFT_SUMMARY = [
  {
    'draftNumber': '150234',
    'registrationType': 'MHREG',
    'registrationDescription': 'REGISTER NEW UNIT',
    'path': '/mhr/api/v1/drafts/00000234',
    'createDateTime': '2020-02-21T18:56:20+00:00',
    'lastUpdateDateTime': '2022-02-21T18:56:20+00:00',
    'registeringName': 'Michael Smith',
    'clientReferenceId': 'D-100001020',
    'submittingParty': 'JOHN SMITH NOTARY PUBLIC',
    'outOfDate': False
  },
  {
    'draftNumber': '150234',
    'mhrNumber': '125234',
    'registrationType': 'TRANS',
    'registrationDescription': 'SALE OR GIFT',
    'path': '/mhr/api/v1/drafts/00000191',
    'createDateTime': '2022-11-23T22:58:46+00:00',
    'lastUpdateDateTime': '2022-11-30T18:22:22+00:00',
    'registeringName': 'Michael Smith',
    'clientReferenceId': 'D-100001005',
    'submittingParty': 'JOHN SMITH NOTARY PUBLIC',
    'outOfDate': False
  }
]

DRAFT_TRANSFER = {
  'draftNumber': '150234',
  'type': 'TRANS',
  'outOfDate': False,
  'registration': {
    'draftNumber': '150234',
    'mhrNumber': '125234',
    'clientReferenceId': 'EX-TRANS-001',
    'submittingParty': {
      'businessName': 'ABC SEARCHING COMPANY',
      'address': {
        'street': '222 SUMMER STREET',
        'city': 'VICTORIA',
        'region': 'BC',
        'country': 'CA',
        'postalCode': 'V8W 2V8'
      },
      'emailAddress': 'bsmith@abc-search.com',
      'phoneNumber': '6041234567',
      'phoneExtension': '546'
    },
    'deleteOwnerGroups': [
      {
        'groupId': 1,
        'owners': [
          {
            'individualName': {
              'first': 'Jane',
              'last': 'Smith'
            },
            'address': {
              'street': '3122B LYNNLARK PLACE',
              'city': 'VICTORIA',
              'region': 'BC',
              'postalCode': ' ',
              'country': 'CA'
            },
            'phoneNumber': '6041234567',
            'ownerId': 1
          }
        ],
        'type': 'SOLE'
      }
    ],
    'addOwnerGroups': [
      {
        'groupId': 2,
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
            'phoneNumber': '6041234567',
            'ownerId': 2
          }
        ],
        'type': 'SOLE',
        'status': 'ACTIVE'
      }
    ]
  },
  'createDateTime': '2020-02-21T18:56:20+00:00',
  'lastUpdateDateTime': '2020-02-21T18:56:20+00:00'
}

EXEMPTION = {
  'mhrNumber': '062245',
  'documentId': '10104489',
  'documentRegistrationNumber': '00416355',
  'documentDescription': 'RESIDENTIAL EXEMPTION',
  'registrationType': 'EXEMPTION_RES',
  'clientReferenceId': 'EX-EXEMPTION-001',
  'createDateTime': '2022-10-21T19:46:45+00:00',
  'attentionReference': '15671-003 SHELLEY',
  'submittingParty': {
    'personName': {
      'first': 'JOHN',
      'middle': 'B',
      'last': 'SMITH'
    },
    'address': {
      'street': '222 SUMMER STREET',
      'city': 'VICTORIA',
      'region': 'BC',
      'country': 'CA',
      'postalCode': 'V8W 2V8'
    },
    'emailAddress': 'jbsmith@gmail.com',
    'phoneNumber': '2504930122',
    'phoneExtension': ''
  },
  'note': {
    'documentType': 'EXRS',
    'remarks': 'HOME IS TO BE USED AS A STORAGE SHED'
  },
  'payment': {
    'receipt': '/pay/api/v1/payment-requests/2277900/receipts',
    'invoiceId': '2277900'
  }
}

LOCATION = {
  'locationType': 'MH_PARK',
  'status': 'ACTIVE',
  'parkName': 'HIDDEN VALLEY TRAILER COURT',
  'pad': '20',
  'address': {
    'street': '940 BLANSHARD STREET',
    'city': 'VICTORIA',
    'region': 'BC',
    'postalCode': ' ',
    'country': 'CA'
  },
  'leaveProvince': False,
  'pidNumber': '011625490',
  'taxCertificate': True,
  'taxExpiryDate': '2022-05-21T07:59:59+00:00',
  'dealerName': 'NOR-TEC DESIGN GROUP LTD.',
  'exceptionPlan': 'EXCEPT PART INCLUDED IN PLAN 7152',
  'additionalDescription': 'SPALLUMCHEEN INDIAN RESERVE NO. 2',
  'legalDescription': 'PARCEL C (O3806) OF LOT 10 DISTRICT LOT 9778 CARIBOO DISTRICT PLAN 2289',
  'lot': '3',
  'parcel': 'A (69860M)',
  'block': '14',
  'districtLot': '4913',
  'partOf': 'NE 1/4',
  'section': '34',
  'township': '84',
  'range': '35',
  'meridian': 'W6M',
  'landDistrict': 'CARIBOU',
  'plan': '71177'
}

MANUFACTURER_INFO = {
  'bcolAccountNumber': '378521',
  'dealerName': 'CHAMPION CANADA INTERNATIONAL ULC - MODULINE INDUSTRIES',
  'submittingParty': {
    'businessName': 'CHAMPION CANADA INTERNATIONAL ULC',
    'address': {
      'street': 'PO BOX 190 STATION MAIN',
      'city': 'PENTICTON',
      'region': 'BC',
      'postalCode': 'V2A 6J9',
      'country': 'CA'
    },
    'phoneNumber': '2507701067'
  },
  'owner': {
    'businessName': 'CHAMPION CANADA INTERNATIONAL ULC',
    'address': {
      'street': '3122B LYNNLARK PLACE',
      'city': 'PENTICTON',
      'region': 'BC',
      'postalCode': 'V2A 5X5',
      'country': 'CA'
    },
    'phoneNumber': '6044620279'
  },
  'manufacturerName': 'MODULINE INDUSTRIES - PENTICTON'
}

NOTE = {
  'documentType': 'CONV',
  'documentId': 'REG01234',
  'documentRegistrationNumber': '00402332',
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
  'ownerId': 1,
  'organizationName': 'SAGE HILL INC.',
  'address': {
    'street': '3122B LYNNLARK PLACE',
    'city': 'VICTORIA',
    'region': 'BC',
    'postalCode': 'V8S 4I6',
    'country': 'CA'
  },
  'type': 'SOLE',
  'partyType': 'OWNER_BUS',
  'phoneNumber': '6041234567',
  'status': 'EXEMPT',
  'suffix': 'EXECUTOR OF THE WILL OF JUDITH ANN JANZEN, DECEASED'
}

OWNER_GROUP = {
  'groupId': 1,
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
        'postalCode': 'V8S 4I6',
        'country': 'CA'
      },
      'phoneNumber': '6041234567',
      'ownerId': 1
    }
  ],
  'type': 'COMMON',
  'interest': 'UNDIVIDED 4/5',
  'interestNumerator': 4,
  'interestDenominator': 5,
  'status': 'ACTIVE',
  'tenancySpecified': True
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
  'documentId': '42800656',
  'documentRegistrationNumber': '00442217',
  'documentDescription': 'REGISTER NEW UNIT',
  'registrationType': 'MHREG',
  'status': 'ACTIVE',
  'clientReferenceId': 'EX-MH001234',
  'declaredValue': 120000,
  'attentionReference': 'GWB14768.100',
  'ownLand': False,
  'submittingParty': {
    'businessName': 'ABC SEARCHING COMPANY',
    'address': {
      'street': '222 SUMMER STREET',
      'city': 'VICTORIA',
      'region': 'BC',
      'country': 'CA',
      'postalCode': 'V8W 2V8'
    },
    'emailAddress': 'bsmith@abc-search.com',
    'phoneNumber': '6041234567',
    'phoneExtension': '546'
  },
  'ownerGroups': [
    {
      'groupId': 1,
      'owners': [
        {
          'individualName': {
            'first': 'Jane',
            'last': 'Smith'
          },
          'address': {
            'street': '3122B LYNNLARK PLACE',
            'city': 'VICTORIA',
            'region': 'BC',
            'postalCode': ' ',
            'country': 'CA'
          },
          'phoneNumber': '6041234567',
          'ownerId': 1
        }
      ],
      'type': 'COMMON',
      'interest': 'UNDIVIDED 4/5',
      'interestNumerator': 4,
      'interestDenominator': 5,
      'status': 'ACTIVE',
      'tenancySpecified': True
    }, {
      'groupId': 2,
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
          'phoneNumber': '6041234567',
          'ownerId': 2
        }
      ],
      'type': 'COMMON',
      'interest': 'UNDIVIDED 1/5',
      'interestNumerator': 1,
      'interestDenominator': 5,
      'status': 'ACTIVE',
      'tenancySpecified': True
    }
  ],
  'location': {
    'locationType': 'OTHER',
    'status': 'ACTIVE',
    'parkName': 'HIDDEN VALLEY TRAILER COURT',
    'pad': '20',
    'address': {
      'street': '940 BLANSHARD STREET',
      'city': 'VICTORIA',
      'region': 'BC',
      'postalCode': ' ',
      'country': 'CA'
    },
    'leaveProvince': False,
    'pidNumber': '011625490',
    'taxCertificate': True,
    'taxExpiryDate': '2022-05-21T07:59:59+00:00',
    'dealerName': 'NOR-TEC DESIGN GROUP LTD.'
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

REGISTRATION_MANUFACTURER = {
  'submittingParty': {
    'businessName': 'REAL ENGINEERED HOMES INC',
    'address': {
      'street': '1704 GOVERNMENT ST.',
      'city': 'PENTICTON',
      'region': 'BC',
      'postalCode': 'V2A 7A1',
      'country': 'CA'
    },
    'phoneNumber': '2507701067'
  },
  'ownerGroups': [
    {
      'groupId': 1,
      'owners': [
        {
          'businessName': 'REAL ENGINEERED HOMES INC',
          'partyType': 'OWNER_BUS',
          'address': {
            'street': '1704 GOVERNMENT ST.',
            'city': 'PENTICTON',
            'region': 'BC',
            'postalCode': 'V2A 7A1',
            'country': 'CA'
          }
        }
      ],
      'type': 'SOLE'
    }
  ],
  'location': {
    'locationType': 'MANUFACTURER',
    'dealerName': 'REAL ENGINEERED HOMES INC',
    'address': {
      'street': '1704 GOVERNMENT ST.',
      'city': 'PENTICTON',
      'region': 'BC',
      'postalCode': 'V2A 7A1',
      'country': 'CA'
    },
    'leaveProvince': False
  },
  'description': {
    'manufacturer': 'REAL ENGINEERED HOMES INC',
  }
}


REGISTRATION_SUMMARY = [
  {
    'mhrNumber': '002000',
    'registrationDescription': 'REGISTER NEW UNIT',
    'registrationType': 'MHREG',
    'documentId': '10200000',
    'documentRegistrationNumber': '00442217',
    'username': 'Michael Scott',
    'statusType': 'ACTIVE',
    'clientReferenceId': 'T-0000001',
    'path': '/mhr/api/v1/registrations/002000',
    'createDateTime': '2021-06-03T22:58:45+00:00',
    'submittingParty': 'Bank of British Columbia',
    'ownerNames': 'GRAEME THOMAS CUNNINGHAM, NEIL MARTIN FOLEY',
    'inUserList': False,
    'lienRegistrationType': 'SA'
  }
]

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
      'documentId': '42800656',
      'status': 'ACTIVE',
      'clientReferenceId': 'EX-MH001234',
      'declaredValue': 120000,
      'ownerGroups': [
        {
          'groupId': 1,
          'owners': [
            {
              'individualName': {
                'first': 'Jane',
                'last': 'Smith'
              },
              'address': {
                'street': '3122B LYNNLARK PLACE',
                'city': 'VICTORIA',
                'region': 'BC',
                'postalCode': ' ',
                'country': 'CA'
              },
              'phoneNumber': '6041234567'
            }
          ],
          'type': 'COMMON',
          'interest': 'UNDIVIDED 4/5',
          'interestNumerator': 4,
          'status': 'ACTIVE',
          'tenancySpecified': True
        }, {
          'groupId': 2,
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
              'phoneNumber': '6041234567'
            }
          ],
          'type': 'COMMON',
          'interest': 'UNDIVIDED 1/5',
          'interestNumerator': 1,
          'status': 'ACTIVE',
          'tenancySpecified': True
        }
      ],
      'location': {
        'locationType': 'OTHER',
        'parkName': 'HIDDEN VALLEY TRAILER COURT',
        'pad': '20',
        'address': {
          'street': '940 BLANSHARD STREET',
          'city': 'VICTORIA',
          'region': 'BC',
          'postalCode': ' ',
          'country': 'CA'
        },
        'leaveProvince': False,
        'pidNumber': '011625490',
        'taxCertificate': True,
        'taxExpiryDate': '2022-05-21T07:59:59+00:00',
        'dealerName': 'NOR-TEC DESIGN GROUP LTD.'
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
          'documentType': 'EXRS',
          'documentId': '80035947',
          'documentRegistrationNumber': '00402332',
          'createDateTime': '1995-02-21T18:56:00+00:00',
          'remarks': 'HOME IS TO BE USED AS A STORAGE SHED',
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
      'ownerStatus': 'ACTIVE',
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
    'activeCount': 1,
    'exemptCount': 0,
    'historicalCount': 0,
    'homeLocation': 'PENTICTON',
    'ownerName': {
      'first': 'James',
      'last': 'Smith'
    },
    'ownerStatus': 'ACTIVE',
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

TRANSFER = {
  'mhrNumber': '125234',
  'documentId': '10104535',
  'documentRegistrationNumber': '00443671',
  'documentDescription': 'SALE OR GIFT',
  'registrationType': 'TRANS',
  'clientReferenceId': 'EX-TRANS-001',
  'attentionReference': 'GWB14768.100',
  'submittingParty': {
    'businessName': 'ABC SEARCHING COMPANY',
    'address': {
      'street': '222 SUMMER STREET',
      'city': 'VICTORIA',
      'region': 'BC',
      'country': 'CA',
      'postalCode': 'V8W 2V8'
    },
    'emailAddress': 'bsmith@abc-search.com',
    'phoneNumber': '6041234567',
    'phoneExtension': '546'
  },
  'deleteOwnerGroups': [
    {
      'groupId': 1,
      'owners': [
        {
          'individualName': {
            'first': 'Jane',
            'last': 'Smith'
          },
          'address': {
            'street': '3122B LYNNLARK PLACE',
            'city': 'VICTORIA',
            'region': 'BC',
            'postalCode': ' ',
            'country': 'CA'
          },
          'phoneNumber': '6041234567',
          'ownerId': 1
        }
      ],
      'type': 'SOLE'
    }
  ],
  'addOwnerGroups': [
    {
      'groupId': 2,
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
          'phoneNumber': '6041234567',
          'ownerId': 2
        }
      ],
      'type': 'SOLE',
      'status': 'ACTIVE'
    }
  ],
  'declaredValue': 78766,
  'consideration': '$78766.00',
  'transferDate': '2022-10-04T20:29:36+00:00',
  'ownLand': False,
  'createDateTime': '2020-02-21T18:56:20+00:00',
  'payment': {
    'receipt': '/pay/api/v1/payment-requests/2199900/receipts',
    'invoiceId': '2199900'
  }
}

PERMIT = {
  'mhrNumber': '101036',
  'documentId': '80035947',
  'documentDescription': 'TRANSPORT PERMIT',
  'documentRegistrationNumber': '00402332',
  'registrationType': 'PERMIT',
  'clientReferenceId': 'EX-TP001234',
  'createDateTime': '2022-10-21T18:56:00+00:00',
  'note': {
    'documentType': 'REG_103',
    'documentId': '80035947',
    'documentRegistrationNumber': '00402332',
    'remarks': 'test',
    'expiryDate': '2022-11-21T08:00:00+00:00'
  },
  'submittingParty': {
    'businessName': 'BOB PATERSON HOMES INC.',
    'address': {
      'street': '1200 S. MACKENZIE AVE.',
      'city': 'WILLIAMS LAKE',
      'region': 'BC',
      'country': 'CA',
      'postalCode': 'V2G 3Y1'
    },
    'phoneNumber': '6044620279',
    'emailAddress': 'bphomes@bphomes.com'
  },
  'owner': {
    'organizationName': 'BOB PATERSON HOMES INC.',
    'address': {
      'street': '1200 S. MACKENZIE AVE.',
      'city': 'WILLIAMS LAKE',
      'region': 'BC',
      'country': 'CA',
      'postalCode': 'V2G 3Y1'
    },
    'phoneNumber': '6044620279'
  },
  'existingLocation': {
    'locationType': 'MANUFACTURER',
    'address': {
      'street': '1200 S. MACKENZIE AVE.',
      'city': 'WILLIAMS LAKE',
      'region': 'BC',
      'country': 'CA',
      'postalCode': 'V2G 3Y1'
    },
    'leaveProvince': False,
    'taxCertificate': False,
    'dealerName': 'CHAMPION CANADA INTERNATIONAL ULC - MODULINE INDUSTRIES'
  },
  'newLocation': {
    'locationType': 'STRATA',
    'address': {
      'street': '7612 LUDLOM RD.',
      'city': 'DEKA LAKE',
      'region': 'BC',
      'country': 'CA',
      'postalCode': ''
    },
    'leaveProvince': False,
    'pidNumber': '007351119',
    'taxCertificate': True,
    'taxExpiryDate': '2024-01-31T08:00:00+00:00'
  },
  'landStatusConfirmation': True,
  'payment': {
    'receipt': '/pay/api/v1/payment-requests/2198744/receipts',
    'invoiceId': '2198744'
  }
}
