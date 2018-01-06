# Copyright 2016 Centrify Corporation
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

import requests
import json
import ConfigParser
import sys

# This Python script connects to Centrify 's Identity Service
#/Security/StartAuthentication	Starts a user authentication session.

# reading variables from config file
config = ConfigParser.ConfigParser()
config.read(sys.argv[1])

# Connect to Cloud Service Tenant
tenant = config.get('Properties', 'c_tenant')
tpsswd = config.get('Properties', 'tpsswd')
c_user = config.get('Properties', 'c_user')
tenant_id = config.get('Properties','tenant_id')
bearer_token = config.get('Properties','bearer_token')
verify = True

url = 'https://%s/cssintegration/mfalogin/' % tenant

headers = {
  'X-CENTRIFY-NATIVE-CLIENT': '1',
  'Content-Type': 'application/json',
  'X-CFY-SRC': 'CSS',
 'Authorization': 'Bearer %s' % bearer_token
}

r = requests.post(url, json = {
    "device_type": "Windows Client",
    "entity_name": "preempt.dev\\ROMANBLACHMAC5B",
    "entity_type": "Server Login",
    "session_id": "N/A",
    "source_host": "127.0.0.1",
    "type_id": "DirectAuthorize - Windows",
    "version": "2.0"
}, headers = headers, verify = verify) 

r.raise_for_status
responseObject = r.json()

print '****************************************************************'
print ' '
print url
print ' '
print '****************************************************************'
print ' '
print 'Sending HTTPS POST Request for /Security/StartAuthentication '
print ' '
print '****************************************************************'
print ' '
print 'JSON Response: '
print ' '
print responseObject

print ' '
print ' '
print ' '
print ' '

#EOF
