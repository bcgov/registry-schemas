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
import copy

ADDRESS = {
    'street': 'delivery_address - address line one',
    'streetAdditional': 'line 2',
    'city': 'delivery_address city',
    'country': 'CA',
    'postalCode': 'H0H0H0',
    'region': 'BC'
}

AMENDMENT_STATEMENT = {
    'statementType': 'AMENDMENT_STATEMENT',
    'baseRegistrationNumber': '023001B',
    'clientReferenceId': 'A-00000402',
    'documentId': '1234567',
    'baseDebtor': {
        'businessName': 'DEBTOR 1 INC.'
    },
   'registeringParty': {
        'businessName': 'ABC SEARCHING COMPANY',
        'address': {
            'street': '222 SUMMER STREET',
            'city': 'VICTORIA',
            'region': 'BC',
            'country': 'CA',
            'postalCode': 'V8W 2V8'
        },
        'emailAddress': 'bsmith@abc-search.com'
    },
    'changeType': 'AM',
    'description': 'Court Order debtor removal.',
    'courtOrderInformation': {
        'courtName': 'Supreme Court of British Columbia.',
        'courtRegistry': 'KAMLOOPS',
        'fileNumber': 'BC123445',
        'orderDate': '2020-02-02',
        'effectOfOrder': 'Court Order to remove James Smith as debtor.'
    },
    'removeTrustIndenture': False,
    'addTrustIndenture': True,
    'deleteDebtors': [ 
        {
            'businessName': 'Brawn Window Cleaning Inc.',
            'address': {
                'street': '1234 Blanshard St',
                'city': 'Victoria',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V8S 3J5'
            },
            'partyId': 1321961
        } 
    ],
    'addDebtors': [
        {
            'businessName': 'Brown Window Cleaning Inc.',
            'address': {
                'street': '1234 Blanshard St',
                'city': 'Victoria',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V8S 3J5'
             },
            'emailAddress': 'csmith@bwc.com',
            'partyId': 1400094
        }
    ],
    'deleteSecuredParties': [
        {
            'businessName': 'BANK OF BRITISH COLUMBIA',
            'address': {
                'street': '3720 BEACON AVENUE',
                'city': 'SIDNEY',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V7R 1R7'
            },
            'partyId': 1321095
        }
    ],
    'addSecuredParties': [
        {
            'businessName': 'BANK OF BRITISH COLUMBIA',
            'address': {
                'street': '3721 BEACON AVENUE',
                'city': 'SIDNEY',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V7R 1R7'
            },
            'emailAddress': 'asmith@bobc.com',
            'partyId': 1400095
        }
    ],
    'deleteVehicleCollateral': [
        {
            'type': 'MV',
            'serialNumber': 'KNADM5A39E6904135',
            'year': 2014,
            'make': 'KIA',
            'model': 'RIO',
            'vehicleId': 974124
        }
    ],
    'addVehicleCollateral': [
        {
            'type': 'MV',
            'serialNumber': 'KM8J3CA46JU622994',
            'year': 2018,
            'make': 'HYUNDAI',
            'model': 'TUCSON',
            'vehicleId': 980000
        }
    ],
    'deleteGeneralCollateral': [
        {
            'description': 'Fridges and stoves. Proceeds: Accts Receivable.',
            'addedDateTime': '2019-02-02T21:08:32Z',
            'collateralId': 123435
        }        
    ],
    'addGeneralCollateral': [
        {
            'description': '1985 white Fender Stratocaster Guitar #1234',
            'addedDateTime': '2020-02-02T21:08:32Z',
            'collateralId': 126000
        }        
    ],
   'createDateTime': '2020-02-21T18:56:20Z',
    'amendmentRegistrationNumber': '10000301R',
    'payment': {
        'receipt': '/pay/api/v1/payment-requests/2199700/receipts',
        'invoiceId': '2199700'
    }
}

BASE_DEBTOR = {
    'personName': {
    'first': 'Michael',
    'middle': 'J',
    'last': 'Smith'
  }
}

CHANGE_STATEMENT = {
    'statementType': 'CHANGE_STATEMENT',
    'baseRegistrationNumber': '023001B',
    'clientReferenceId': 'A-00000402',
    'documentId': '1234567',
    'baseDebtor': {
        'businessName': 'DEBTOR 1 INC.'
    },
   'registeringParty': {
        'businessName': 'ABC SEARCHING COMPANY',
        'address': {
            'street': '222 SUMMER STREET',
            'city': 'VICTORIA',
            'region': 'BC',
            'country': 'CA',
            'postalCode': 'V8W 2V8'
        },
        'emailAddress': 'bsmith@abc-search.com'
    },
    'changeType': 'AC',
    'deleteDebtors': [ 
        {
            'businessName': 'Brawn Window Cleaning Inc.',
            'address': {
                'street': '1234 Blanshard St',
                'city': 'Victoria',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V8S 3J5'
            },
            'partyId': 1321961
        } 
    ],
    'addDebtors': [
        {
            'businessName': 'Brown Window Cleaning Inc.',
            'address': {
                'street': '1234 Blanshard St',
                'city': 'Victoria',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V8S 3J5'
             },
            'emailAddress': 'csmith@bwc.com',
            'partyId': 1400094
        }
    ],
    'deleteSecuredParties': [
        {
            'businessName': 'BANK OF BRITISH COLUMBIA',
            'address': {
                'street': '3720 BEACON AVENUE',
                'city': 'SIDNEY',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V7R 1R7'
            },
            'partyId': 1321095
        }
    ],
    'addSecuredParties': [
        {
            'businessName': 'BANK OF BRITISH COLUMBIA',
            'address': {
                'street': '3721 BEACON AVENUE',
                'city': 'SIDNEY',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V7R 1R7'
            },
            'emailAddress': 'asmith@bobc.com',
            'partyId': 1400095
        }
    ],
    'deleteVehicleCollateral': [
        {
            'type': 'MV',
            'serialNumber': 'KNADM5A39E6904135',
            'year': 2014,
            'make': 'KIA',
            'model': 'RIO',
            'vehicleId': 974124
        }
    ],
    'addVehicleCollateral': [
        {
            'type': 'MV',
            'serialNumber': 'KM8J3CA46JU622994',
            'year': 2018,
            'make': 'HYUNDAI',
            'model': 'TUCSON',
            'vehicleId': 980000
        }
    ],
    'deleteGeneralCollateral': [
        {
            'description': 'Fridges and stoves. Proceeds: Accts Receivable.',
            'addedDateTime': '2019-02-02T21:08:32Z',
            'collateralId': 123435
        }        
    ],
    'addGeneralCollateral': [
        {
            'description': '1985 white Fender Stratocaster Guitar #1234',
            'addedDateTime': '2020-02-02T21:08:32Z',
            'collateralId': 126000
        }        
    ],
   'createDateTime': '2020-02-21T18:56:20Z',
    'changeRegistrationNumber': '10000301R',
    'payment': {
        'receipt': '/pay/api/v1/payment-requests/2199700/receipts',
        'invoiceId': '2199700'
    }
}

CLIENT_PARTY = {
    'code': '5000009',
    'personName': {
        'first': 'Michael',
        'middle': 'J',
        'last': 'Smith'
    },
    'address': {
        'street': '3721 BEACON AVENUE',
        'city': 'SIDNEY',
        'region': 'BC',
        'country': 'CA',
        'postalCode': 'V7R 1R7'
    },
    'emailAddress': 'asmith@bobc.com',
    'contact': {
        'name': 'ROBERT JONES',
        'areaCode': '250',
        'phoneNumber': '7244404',
        'emailAddress': 'rbjones@bobc.com'
    }
}

COURT_ORDER = {
    'courtName': 'Supreme Court of British Columbia.',
    'courtRegistry': 'KAMLOOPS',
    'fileNumber': 'BC123445',
    'orderDate': '2020-02-02',
    'effectOfOrder': 'Court Order to remove James Smith as debtor.'
}

DISCHARGE_STATEMENT = {
    'statementType': 'DISCHARGE_STATEMENT',
    'baseRegistrationNumber': '023001B',
    'clientReferenceId': 'A-00000402',
    'documentId': '1234567',
    'baseDebtor': {
        'businessName': 'DEBTOR 1 INC.'
    },
   'registeringParty': {
        'businessName': 'ABC SEARCHING COMPANY',
        'address': {
            'street': '222 SUMMER STREET',
            'city': 'VICTORIA',
            'region': 'BC',
            'country': 'CA',
            'postalCode': 'V8W 2V8'
        },
        'emailAddress': 'bsmith@abc-search.com'
    },
    'createDateTime': '2020-02-21T18:56:20Z',
    'dischargeRegistrationNumber': '10000301',
    'payment': {
        'receipt': '/pay/api/v1/payment-requests/2199700/receipts',
        'invoiceId': '2199700'
    }
}

DRAFT_AMENDMENT_STATEMENT = {
  'type': 'AMENDMENT_STATEMENT',
  'amendmentStatement': {
    'baseRegistrationNumber': '023001B',
    'documentId': 'D0034003',
    'description': 'Court Order debtor removal.',
    'changeType': 'CO',
    'clientReferenceId': 'A-00000402',
    'baseDebtor': {
        'businessName': 'DEBTOR 1 INC.'
    },
    'registeringParty': {
      'businessName': 'ABC SEARCHING COMPANY',
      'address': {
        'street': '222 SUMMER STREET',
        'city': 'VICTORIA',
        'region': 'BC',
        'country': 'CA',
        'postalCode': 'V8W 2V8'
      },
      'emailAddress': 'bsmith@abc-search.com'
    },
    'courtOrderInformation': {
      'courtName': 'Supreme Court of British Columbia.',
      'courtRegistry': 'KAMLOOPS',
      'fileNumber': 'BC123445',
      'orderDate': '2020-02-02',
      'effectOfOrder': 'Court Order to remove James Smith as debtor.'
    },
    'deleteDebtors': [
      {
        'personName': {
          'first': 'James',
          'last': 'Smith'
        },
        'partyId': 1321961
      }
    ]
  },
  'createDateTime': '2020-02-21T18:56:20Z'
}

DRAFT_CHANGE_STATEMENT = {
  'type': 'CHANGE_STATEMENT',
  'changeStatement': {
    'baseRegistrationNumber': '023010B',
    'documentId': 'D0034003',
    'changeType': 'DT',
    'clientReferenceId': 'A-00000402',
    'baseDebtor': {
        'businessName': 'DEBTOR 1 INC.'
    },
    'registeringParty': {
      'businessName': 'ABC SEARCHING COMPANY',
      'address': {
        'street': '222 SUMMER STREET',
        'city': 'VICTORIA',
        'region': 'BC',
        'country': 'CA',
        'postalCode': 'V8W 2V8'
      },
      'emailAddress': 'bsmith@abc-search.com'
    },
    'deleteDebtors': [
      {
            'businessName': 'Brawn Window Cleaning Inc.',
            'partyId': 1321961
      }
    ],
    'addDebtors': [
      {
        'businessName': 'Brown Window Cleaning Inc.',
        'address': {
          'street': '1234 Blanshard St',
          'city': 'Victoria',
          'region': 'BC',
          'country': 'CA',
          'postalCode': 'V8S 3J5'
        },
        'emailAddress': 'csmith@bwc.com'
      }
    ]
  },
  'createDateTime': '2020-02-21T18:56:20Z',
  'lastUpdateDateTime': '2020-02-23T11:23:20Z'
}

DRAFT_FINANCING_STATEMENT = {
  'type': 'FINANCING_STATEMENT',
  'financingStatement': {
    'type': 'SA',
    'clientReferenceId': 'A-00000402',
    'registeringParty': {
      'businessName': 'ABC SEARCHING COMPANY',
      'address': {
        'street': '222 SUMMER STREET',
        'city': 'VICTORIA',
        'region': 'BC',
        'country': 'CA',
        'postalCode': 'V8W 2V8'
      },
      'emailAddress': 'bsmith@abc-search.com'
    },
    'securedParties': [
      {
        'businessName': 'BANK OF BRITISH COLUMBIA',
        'address': {
          'street': '3721 BEACON AVENUE',
          'city': 'SIDNEY',
          'region': 'BC',
          'country': 'CA',
          'postalCode': 'V7R 1R7'
        },
        'emailAddress': 'asmith@bobc.com'
      }
    ],
    'debtors': [
      {
        'businessName': 'Debtor 1 Inc.',
        'address': {
          'street': '721 Debtor Ave',
          'city': 'Victoria',
          'region': 'BC',
          'country': 'CA',
          'postalCode': 'A1A 1A1'
        },
        'birthDate': '1990-06-15',
        'emailAddress': 'dsmith@debtor1.com'
      }
    ],
    'vehicleCollateral': [
      {
        'type': 'MV',
        'serialNumber': 'KM8J3CA46JU622994',
        'year': 2018,
        'make': 'HYUNDAI',
        'model': 'TUCSON'
      }
    ],
    'lifeYears': 5
  }
}

DRAFT_SUMMARY = [
  {
    'type': 'FINANCING_STATEMENT',
    'documentId': 'B0008761',
    'registrationType': 'SA',
    'path': '/ppr/api/v1/drafts/B0008761',
    'createDateTime': '2020-02-21T18:56:20Z'
  },
  {
    'type': 'AMENDMENT_STATEMENT',
    'baseRegistrationNumber': '1000123',
    'documentId': 'B0008762',
    'registrationType': 'AM',
    'path': '/ppr/api/v1/drafts/B0008762',
    'createDateTime': '2020-02-22T14:13:20Z'
  },
  {
    'type': 'CHANGE_STATEMENT',
    'baseRegistrationNumber': '1000123',
    'documentId': 'B0008763',
    'registrationType': 'DT',
    'path': '/ppr/api/v1/drafts/B0008763',
    'createDateTime': '2020-02-23T10:05:20Z'
  }
]

FINANCING_STATEMENT = {
    'type': 'SA',
    'clientReferenceId': 'A-00000402',
    'documentId': '1234567',
    'registeringParty': {
        'businessName': 'ABC SEARCHING COMPANY',
        'address': {
            'street': '222 SUMMER STREET',
            'city': 'VICTORIA',
            'region': 'BC',
            'country': 'CA',
            'postalCode': 'V8W 2V8'
        },
        'emailAddress': 'bsmith@abc-search.com'
    },
    'securedParties': [
        {
            'businessName': 'BANK OF BRITISH COLUMBIA',
            'address': {
                'street': '3720 BEACON AVENUE',
                'city': 'SIDNEY',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V7R 1R7'
            },
            'partyId': 1321095
        }
    ],
    'debtors': [
        {
            'businessName': 'Brown Window Cleaning Inc.',
            'address': {
                'street': '1234 Blanshard St',
                'city': 'Victoria',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V8S 3J5'
             },
            'emailAddress': 'csmith@bwc.com',
            'partyId': 1400094
        }
    ],
    'vehicleCollateral': [
        {
            'type': 'MV',
            'serialNumber': 'KNADM5A39E6904135',
            'year': 2014,
            'make': 'KIA',
            'model': 'RIO',
            'vehicleId': 974124
        }
    ],
    'generalCollateral': [
        {
            'description': 'Fridges and stoves. Proceeds: Accts Receivable.',
            'addedDateTime': '2019-02-02T21:08:32Z',
            'collateralId': 123435
        }        
    ],
    'expiryDate': '2025-02-21',
    'lifeYears': 5,
    'trustIndenture': False,
    'lifeInfinite': False,
    'lienAmount': '12,000.00',
    'surrenderDate': '2021-01-31',
    'baseRegistrationNumber': '023001B',
    'createDateTime': '2020-02-21T18:56:20Z',
    'payment': {
        'receipt': '/pay/api/v1/payment-requests/2199700/receipts',
        'invoiceId': '2199700'
    }
}

FINANCING_STATEMENT_HISTORY = [
  {
    'financingStatement': {
      'type': 'SA',
      'clientReferenceId': 'A-00000402',
      'registeringParty': {
        'businessName': 'ABC SEARCHING COMPANY',
        'address': {
          'street': '222 SUMMER STREET',
          'city': 'VICTORIA',
          'region': 'BC',
          'country': 'CA',
          'postalCode': 'V8W 2V8'
        },
        'emailAddress': 'bsmith@abc-search.com'
      },
      'securedParties': [
        {
          'businessName': 'BANK OF BRITISH COLUMBIA',
          'address': {
            'street': '3721 BEACON AVENUE',
            'city': 'SIDNEY',
            'region': 'BC',
            'country': 'CA',
            'postalCode': 'V7R 1R7'
          },
          'emailAddress': 'asmith@bobc.com',
          'partyId': 1321064
        }
      ],
      'debtors': [
        {
          'businessName': 'Debtor 1 Inc.',
          'address': {
            'street': '721 Debtor Ave',
            'city': 'Victoria',
            'region': 'BC',
            'country': 'CA',
            'postalCode': 'A1A 1A1'
          },
          'birthDate': '1990-06-15',
          'emailAddress': 'dsmith@debtor1.com',
          'partyId': 1321065
        }
      ],
      'vehicleCollateral': [
        {
          'type': 'MV',
          'serialNumber': 'KM8J3CA46JU622994',
          'year': 2018,
          'make': 'HYUNDAI',
          'model': 'TUCSON',
          'vehicleId': 974123
        }
      ],
      'generalCollateral': [],
      'trustIndenture': False,
      'lifeYears': 2,
      'expiryDate': '2022-02-21',
      'baseRegistrationNumber': '023001B',
      'createDateTime': '2020-02-21T18:56:20Z',
      'payment': {
        'invoiceId': '2198743',
        'receipt': '/pay/api/v1/payment-requests/2198743/receipts'
      }
    },
    'changes': [
      {
        'statementType': 'AMENDMENT_STATEMENT',
        'baseRegistrationNumber': '023001B',
        'description': 'Amendment to correct spelling mistake in debtor name. Name changed from \'Brawn\' to \'Brown\'.',
        'changeType': 'AM',
        'clientReferenceId': 'A-00000403',
        'registeringParty': {
          'businessName': 'ABC SEARCHING COMPANY',
          'address': {
            'street': '222 SUMMER STREET',
            'city': 'VICTORIA',
            'region': 'BC',
            'country': 'CA',
            'postalCode': 'V8W 2V8'
          },
          'emailAddress': 'bsmith@abc-search.com'
        },
        'deleteDebtors': [
          {
            'businessName': 'Brawn Window Cleaning Inc.',
            'partyId': 1321065
          }
        ],
        'addDebtors': [
          {
            'businessName': 'Brown Window Cleaning Inc.',
            'address': {
              'street': '1234 Blanshard St',
              'city': 'Victoria',
              'region': 'BC',
              'country': 'CA',
              'postalCode': 'V8S 3J5'
            },
            'emailAddress': 'csmith@bwc.com',
            'partyId': 1325661
          }
        ],
        'createDateTime': '2020-02-28T08:30:20Z',
        'amendmentRegistrationNumber': '010001A',
        'payment': {
          'invoiceId': '2198744',
          'receipt': '/pay/api/v1/payment-requests/2198744/receipts'
        }
      },
      {
        'statementType': 'CHANGE_STATEMENT',
        'baseRegistrationNumber': '023001B',
        'changeType': 'ST',
        'clientReferenceId': 'A-00000404',
        'registeringParty': {
          'businessName': 'ABC SEARCHING COMPANY',
          'address': {
            'street': '222 SUMMER STREET',
            'city': 'VICTORIA',
            'region': 'BC',
            'country': 'CA',
            'postalCode': 'V8W 2V8'
          },
          'emailAddress': 'bsmith@abc-search.com'
        },
        'deleteSecuredParties': [
          {
            'businessName': 'Secured 1 Ltd',
            'address': {
              'street': '721 Pandora Ave',
              'city': 'Victoria',
              'region': 'BC',
              'country': 'CA',
              'postalCode': 'V8S 1V2'
            },
            'partyId': 1320122
          }
        ],
        'addSecuredParties': [
          {
            'businessName': 'BANK OF BRITISH COLUMBIA',
            'address': {
              'street': '3721 BEACON AVENUE',
              'city': 'SIDNEY',
              'region': 'BC',
              'country': 'CA',
              'postalCode': 'V7R 1R7'
            },
            'emailAddress': 'asmith@bobc.com',
            'partyId': 1321561
          }
        ],
        'createDateTime': '2020-03-02T13:02:20Z',
        'changeRegistrationNumber': '010001C',
        'payment': {
          'invoiceId': '2198745',
          'receipt': '/pay/api/v1/payment-requests/2198745/receipts'
        }
      },
      {
        'statementType': 'RENEWAL_STATEMENT',
        'baseRegistrationNumber': '023001B',
        'clientReferenceId': 'A-00000405',
        'registeringParty': {
          'businessName': 'ABC SEARCHING COMPANY',
          'address': {
            'street': '222 SUMMER STREET',
            'city': 'VICTORIA',
            'region': 'BC',
            'country': 'CA',
            'postalCode': 'V8V 4V6'
          },
          'emailAddress': 'bsmith@abc-search.com'
        },
        'courtOrderInformation': {
          'courtName': 'Supreme Court of British Columbia.',
          'courtRegistry': 'VICTORIA',
          'fileNumber': 'BC123495',
          'orderDate': '2020-02-21',
          'effectOfOrder': 'Court Order to renew Repairers Lien.'
        },
        'expiryDate': '2020-08-21',
        'createDateTime': '2020-02-21T18:56:20Z',
        'renewalRegistrationNumber': '010002R',
        'payment': {
          'receipt': '/pay/api/v1/payment-requests/2198743/receipts',
          'invoiceId': '2198743'
        }
      },
        {
            'statementType': 'DISCHARGE_STATEMENT',
            'baseRegistrationNumber': '023001B',
            'clientReferenceId': 'A-00000402',
            'documentId': '1234567',
            'registeringParty': {
                'businessName': 'ABC SEARCHING COMPANY',
                'address': {
                    'street': '222 SUMMER STREET',
                    'city': 'VICTORIA',
                    'region': 'BC',
                    'country': 'CA',
                    'postalCode': 'V8W 2V8'
                },
                'emailAddress': 'bsmith@abc-search.com'
            },
            'createDateTime': '2020-02-21T18:56:20Z',
            'dischargeRegistrationNumber': '10000301',
            'payment': {
                'receipt': '/pay/api/v1/payment-requests/2199700/receipts',
                'invoiceId': '2199700'
            }
        }
    ]
  }
]

GENERAL_COLLATERAL = {
    'description': 'Fridges and stoves. Proceeds: Accts Receivable.',
    'addedDateTime': '2020-02-02T21:08:32Z',
    'collateralId': 123435
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
  'birthDate': '1986-12-01',
  'partyId': 1321064
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

RENEWAL_STATEMENT = {
    'statementType': 'RENEWAL_STATEMENT',
    'baseRegistrationNumber': '023001B',
    'clientReferenceId': 'A-00000402',
    'baseDebtor': {
        'businessName': 'DEBTOR 1 INC.'
    },
   'registeringParty': {
        'businessName': 'ABC SEARCHING COMPANY',
        'address': {
            'street': '222 SUMMER STREET',
            'city': 'VICTORIA',
            'region': 'BC',
            'country': 'CA',
            'postalCode': 'V8W 2V8'
        },
        'emailAddress': 'bsmith@abc-search.com'
    },
    'expiryDate': '2025-02-21',
    'courtOrderInformation': {
        'courtName': 'Supreme Court of British Columbia.',
        'courtRegistry': 'KAMLOOPS',
        'fileNumber': 'BC123445',
        'orderDate': '2020-02-02',
        'effectOfOrder': 'Court Order to remove James Smith as debtor.'
    },
    'createDateTime': '2020-02-21T18:56:20Z',
    'renewalRegistrationNumber': '10000301R',
    'payment': {
        'receipt': '/pay/api/v1/payment-requests/2199700/receipts',
        'invoiceId': '2199700'
    }
}

SEARCH_QUERY = {
    'type': 'INDIVIDUAL_DEBTOR',
    'criteria': {
        'value': '123456B',
        'debtorName': {
            'first': 'James',
            'second': 'M.',
            'last': 'Smith',
            'business': 'ACME USED CARS LTD.'
        }
    },
    'clientReferenceId': 'A-00000402',
    'startDateTime': '2020-08-07T00:00:00Z',
    'endDateTime': '2020-08-08T00:00:00Z'
}

SEARCH_QUERY_RESULT = {
  'searchId': '1294376',
  'searchDateTime': '2020-10-15T21:08:32Z',
  'returnedResultsSize': 4,
  'totalResultsSize': 4,
  'maxResultsSize': 1000,
  'searchQuery': {
    'type': 'BUSINESS_DEBTOR',
    'criteria': {
      'debtorName': {
        'business': 'BROWN AUTOMOTIVE LTD.'
      }
    },
    'clientReferenceId': 'A-00000402'
  },
  'results': [
    {
      'matchType': 'EXACT',
      'baseRegistrationNumber': '013739B',
      'createDateTime': '2020-08-10T18:56:20Z',
      'registrationType': 'SA',
      'debtor': {
        'businessName': 'BROWN AUTOMOTIVE LTD.',
        'partyId': 1041115
      }
    },
    {
      'matchType': 'SIMILAR',
      'baseRegistrationNumber': '013600B',
      'createDateTime': '2020-08-03T10:12:20Z',
      'registrationType': 'SA',
      'debtor': {
        'businessName': 'BROWNS AUTOMOTIVE LTD.',
        'partyId': 1031115
      }
    },
    {
      'matchType': 'SIMILAR',
      'baseRegistrationNumber': '013699B',
      'createDateTime': '2020-08-08T10:12:20Z',
      'registrationType': 'SA',
      'debtor': {
        'businessName': 'BROWN AND BLACK AUTO LTD.',
        'partyId': 1021115
      }
    },
    {
      'matchType': 'SIMILAR',
      'baseRegistrationNumber': '013800B',
      'createDateTime': '2020-08-14T10:12:20Z',
      'registrationType': 'SA',
      'debtor': {
        'businessName': 'BROWNING AUTOMOTIVE LTD.',
        'partyId': 1011115
      }
    }
  ],
  'payment': {
    'receipt': '/pay/api/v1/payment-requests/2198748/receipts',
    'invoiceId': '2198748'
  }
}

SEARCH_SUMMARY = [
    {
        'matchType': 'EXACT',
        'registrationNumber': '013900B',
        'baseRegistrationNumber': '013739B',
        'createDateTime': '2020-08-10T18:56:20Z',
        'registrationType': 'SA'
    },
    {
        'matchType': 'SIMILAR',
        'baseRegistrationNumber': '013600B',
        'createDateTime': '2020-08-03T10:12:20Z',
        'registrationType': 'SA'
    },
    {
        'matchType': 'SIMILAR',
        'baseRegistrationNumber': '013699B',
        'createDateTime': '2020-08-08T10:12:20Z',
        'registrationType': 'SA',
        'vehicleCollateral': {
            'type': 'MV',
            'serialNumber': 'KM8J3CA46JU622994',
            'year': 2018,
            'make': 'HYUNDAI',
            'model': 'TUCSON'
        },
        'debtor': {
            'businessName': 'Brown Window Cleaning Inc.',
            'address': {
                'street': '1234 Blanshard St',
                'city': 'Victoria',
                'region': 'BC',
                'country': 'CA',
                'postalCode': 'V8S 3J5'
             },
            'emailAddress': 'csmith@bwc.com',
            'partyId': 1400094
        }
    }
]

VEHICLE_COLLATERAL = {
  'type': 'MV',
  'serialNumber': 'KM8J3CA46JU622994',
  'year': 2018,
  'make': 'HYUNDAI',
  'model': 'TUSCON',
  'vehicleId': 876114
}

