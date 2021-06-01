# EpicEndpoints
An easy way to access Epic Games' endpoints without clutter.

## Installation
PyPI Page: https://pypi.org/project/EpicEndpoints/

## Usage
`pip install EpicEndpoints` <br>
<br>
`from EpicEndpoints import EpicEndpoints`

## Docs

### DeviceAuthHandler
Class: `DeviceAuthHandler` <br>
Properties: `access_token`<br>
Functions (data returned in dict format):<br>
- getLoginInfo()<br>
- deviceCodeData(device_code)<br>
- getDeviceAuthDetails(access_token, account_id)<br>

Example:
```python
from EpicEndpoints import EpicEndpoints
import asyncio

handler = EpicEndpoints.DeviceAuthHandler()
login = handler.getLoginInfo()
print(login['verification_uri_complete'])

await asyncio.sleep(10)

data = handler.deviceCodeData(login['device_code'])
print(data['account_id'])
device_auth_details = handler.getDeviceAuthDetails(data['access_token'],data['account_id'])
print(device_auth_details)

device = device_auth_details['deviceId']
account = device_auth_details['accountId']
secret = device_auth_details['secret']
```

### Other Functions: <br>
`getAccessToken(clientId, secret)`<br>
`params:` a valid client id and secret<br>
`returns:` an access token to access the other endpoints<br>

`getDisplayName(account_id, access_token)`<br>
`params:` an account id and a valid access token<br>
`returns:` the user's display name<br>
