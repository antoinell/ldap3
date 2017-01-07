"""
"""

# Created on 2016.08.31
#
# Author: Giovanni Cannata
#
# Copyright 2013, 2014, 2015, 2016 Giovanni Cannata
#
# This file is part of ldap3.
#
# ldap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ldap3 in the COPYING and COPYING.LESSER files.
# If not, see <http://www.gnu.org/licenses/>.

from sys import stdin, getdefaultencoding

from .. import ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, NO_ATTRIBUTES
from ..core.exceptions import LDAPConfigurationParameterError

# checks
_CLASSES_EXCLUDED_FROM_CHECK = ['subschema']
_ATTRIBUTES_EXCLUDED_FROM_CHECK = [ALL_ATTRIBUTES,
                                   ALL_OPERATIONAL_ATTRIBUTES,
                                   NO_ATTRIBUTES,
                                   'ldapSyntaxes',
                                   'matchingRules',
                                   'matchingRuleUse',
                                   'dITContentRules',
                                   'dITStructureRules',
                                   'nameForms',
                                   'altServer',
                                   'namingContexts',
                                   'supportedControl',
                                   'supportedExtension',
                                   'supportedFeatures',
                                   'supportedCapabilities',
                                   'supportedLdapVersion',
                                   'supportedSASLMechanisms',
                                   'vendorName',
                                   'vendorVersion',
                                   'subschemaSubentry',
                                   'ACL']
_UTF8_ENCODED_SYNTAXES = ['1.2.840.113556.1.4.904',  # DN String [MICROSOFT]
                          '1.2.840.113556.1.4.1362',  # String (Case) [MICROSOFT]
                          '1.3.6.1.4.1.1466.115.121.1.12',  # DN String [RFC4517]
                          '1.3.6.1.4.1.1466.115.121.1.15',  # Directory String [RFC4517]
                          '1.3.6.1.4.1.1466.115.121.1.41',  # Postal Address) [RFC4517]
                          '1.3.6.1.4.1.1466.115.121.1.58',  # Substring Assertion [RFC4517]
                          '2.16.840.1.113719.1.1.5.1.6',  # Case Ignore List [NOVELL]
                          '2.16.840.1.113719.1.1.5.1.14',  # Tagged String [NOVELL]
                          '2.16.840.1.113719.1.1.5.1.15',  # Tagged Name and String [NOVELL]
                          '2.16.840.1.113719.1.1.5.1.23',  # Tagged Name [NOVELL]
                          '2.16.840.1.113719.1.1.5.1.25']  # Typed Name [NOVELL]

_UTF8_ENCODED_TYPES = []

_CASE_INSENSITIVE_ATTRIBUTE_NAMES = True
_CASE_INSENSITIVE_SCHEMA_NAMES = True

# abstraction layer
_ABSTRACTION_OPERATIONAL_ATTRIBUTE_PREFIX = 'OA_'

# communication
_POOLING_LOOP_TIMEOUT = 10  # number of seconds to wait before restarting a cycle to find an active server in the pool

_RESPONSE_SLEEPTIME = 0.05  # seconds to wait while waiting for a response in asynchronous strategies
_RESPONSE_WAITING_TIMEOUT = 20  # waiting timeout for receiving a response in asynchronous strategies
_SOCKET_SIZE = 4096  # socket byte size
_CHECK_AVAILABILITY_TIMEOUT = 2.5  # default timeout for socket connect when checking availability
_RESET_AVAILABILITY_TIMEOUT = 5  # default timeout for resetting the availability status when checking candidate addresses
_RESTARTABLE_SLEEPTIME = 2  # time to wait in a restartable strategy before retrying the request
_RESTARTABLE_TRIES = 30  # number of times to retry in a restartable strategy before giving up. Set to True for unlimited retries
_REUSABLE_THREADED_POOL_SIZE = 10
_REUSABLE_THREADED_LIFETIME = 3600  # 1 hour
_DEFAULT_THREADED_POOL_NAME = 'REUSABLE_DEFAULT_POOL'
_ADDRESS_INFO_REFRESH_TIME = 300  # seconds to wait before refreshing address info from dns

if stdin and stdin.encoding:
    _DEFAULT_ENCODING = stdin.encoding
elif getdefaultencoding():
    _DEFAULT_ENCODING = getdefaultencoding()
else:
    _DEFAULT_ENCODING = 'utf-8'


def get_config_parameter(parameter):
    if parameter == 'CASE_INSENSITIVE_ATTRIBUTE_NAMES':
        return _CASE_INSENSITIVE_ATTRIBUTE_NAMES
    elif parameter == 'CASE_INSENSITIVE_SCHEMA_NAMES':
        return _CASE_INSENSITIVE_SCHEMA_NAMES
    elif parameter == 'ABSTRACTION_OPERATIONAL_ATTRIBUTE_PREFIX':
        return _ABSTRACTION_OPERATIONAL_ATTRIBUTE_PREFIX
    elif parameter == 'POOLING_LOOP_TIMEOUT':
        return _POOLING_LOOP_TIMEOUT
    elif parameter == 'RESPONSE_SLEEPTIME':
        return _RESPONSE_SLEEPTIME
    elif parameter == 'RESPONSE_WAITING_TIMEOUT':
        return _RESPONSE_WAITING_TIMEOUT
    elif parameter == 'SOCKET_SIZE':
        return _SOCKET_SIZE
    elif parameter == 'CHECK_AVAILABILITY_TIMEOUT':
        return _CHECK_AVAILABILITY_TIMEOUT
    elif parameter == 'RESTARTABLE_SLEEPTIME':
        return _RESTARTABLE_SLEEPTIME
    elif parameter == 'RESTARTABLE_TRIES':
        return _RESTARTABLE_TRIES
    elif parameter == 'REUSABLE_THREADED_POOL_SIZE':
        return _REUSABLE_THREADED_POOL_SIZE
    elif parameter == 'REUSABLE_THREADED_LIFETIME':
        return _REUSABLE_THREADED_LIFETIME
    elif parameter == 'DEFAULT_THREADED_POOL_NAME':
        return _DEFAULT_THREADED_POOL_NAME
    elif parameter == 'ADDRESS_INFO_REFRESH_TIME':
        return _ADDRESS_INFO_REFRESH_TIME
    elif parameter == 'RESET_AVAILABILITY_TIMEOUT':
        return _RESET_AVAILABILITY_TIMEOUT
    elif parameter == 'DEFAULT_ENCODING':
        return _DEFAULT_ENCODING
    elif parameter == 'CLASSES_EXCLUDED_FROM_CHECK':
        return _CLASSES_EXCLUDED_FROM_CHECK
    elif parameter == 'ATTRIBUTES_EXCLUDED_FROM_CHECK':
        return _ATTRIBUTES_EXCLUDED_FROM_CHECK
    elif parameter == 'UTF8_ENCODED_SYNTAXES':
        return _UTF8_ENCODED_SYNTAXES
    elif parameter == 'UTF8_ENCODED_TYPES':
        return _UTF8_ENCODED_TYPES
    raise LDAPConfigurationParameterError('configuration parameter %s not valid' % parameter)


def set_config_parameter(parameter, value):
    if parameter == 'CASE_INSENSITIVE_ATTRIBUTE_NAMES':
        global _CASE_INSENSITIVE_ATTRIBUTE_NAMES
        _CASE_INSENSITIVE_ATTRIBUTE_NAMES = value
    elif parameter == 'CASE_INSENSITIVE_SCHEMA_NAMES':
        global _CASE_INSENSITIVE_SCHEMA_NAMES
        _CASE_INSENSITIVE_SCHEMA_NAMES = value
    elif parameter == 'ABSTRACTION_OPERATIONAL_ATTRIBUTE_PREFIX':
        global _ABSTRACTION_OPERATIONAL_ATTRIBUTE_PREFIX
        _ABSTRACTION_OPERATIONAL_ATTRIBUTE_PREFIX = value
    elif parameter == 'POOLING_LOOP_TIMEOUT':
        global _POOLING_LOOP_TIMEOUT
        _POOLING_LOOP_TIMEOUT = value
    elif parameter == 'RESPONSE_SLEEPTIME':
        global _RESPONSE_SLEEPTIME
        _RESPONSE_SLEEPTIME = value
    elif parameter == 'RESPONSE_WAITING_TIMEOUT':
        global _RESPONSE_WAITING_TIMEOUT
        _RESPONSE_WAITING_TIMEOUT = value
    elif parameter == 'SOCKET_SIZE':
        global _SOCKET_SIZE
        _SOCKET_SIZE = value
    elif parameter == 'CHECK_AVAILABILITY_TIMEOUT':
        global _CHECK_AVAILABILITY_TIMEOUT
        _CHECK_AVAILABILITY_TIMEOUT = value
    elif parameter == 'RESTARTABLE_SLEEPTIME':
        global _RESTARTABLE_SLEEPTIME
        _RESTARTABLE_SLEEPTIME = value
    elif parameter == 'RESTARTABLE_TRIES':
        global _RESTARTABLE_TRIES
        _RESTARTABLE_TRIES = value
    elif parameter == 'REUSABLE_THREADED_POOL_SIZE':
        global _REUSABLE_THREADED_POOL_SIZE
        _REUSABLE_THREADED_POOL_SIZE = value
    elif parameter == 'REUSABLE_THREADED_LIFETIME':
        global _REUSABLE_THREADED_LIFETIME
        _REUSABLE_THREADED_LIFETIME = value
    elif parameter == 'DEFAULT_THREADED_POOL_NAME':
        global _DEFAULT_THREADED_POOL_NAME
        _DEFAULT_THREADED_POOL_NAME = value
    elif parameter == 'ADDRESS_INFO_REFRESH_TIME':
        global _ADDRESS_INFO_REFRESH_TIME
        _ADDRESS_INFO_REFRESH_TIME = value
    elif parameter == 'RESET_AVAILABILITY_TIMEOUT':
        global _RESET_AVAILABILITY_TIMEOUT
        _RESET_AVAILABILITY_TIMEOUT = value
    elif parameter == 'DEFAULT_ENCODING':
        global _DEFAULT_ENCODING
        _DEFAULT_ENCODING = value
    elif parameter == 'CLASSES_EXCLUDED_FROM_CHECK':
        global _CLASSES_EXCLUDED_FROM_CHECK
        _CLASSES_EXCLUDED_FROM_CHECK = value
    elif parameter == 'ATTRIBUTES_EXCLUDED_FROM_CHECK':
        global _ATTRIBUTES_EXCLUDED_FROM_CHECK
        _ATTRIBUTES_EXCLUDED_FROM_CHECK = value
    elif parameter == 'UTF8_ENCODED_SYNTAXES':
        global _UTF8_ENCODED_SYNTAXES
        _UTF8_ENCODED_SYNTAXES = value
    elif parameter == 'UTF8_ENCODED_TYPES':
        global _UTF8_ENCODED_TYPES
        _UTF8_ENCODED_TYPES = value
    else:
        raise LDAPConfigurationParameterError('unable to set configuration parameter %s' % parameter)
