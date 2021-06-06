# EpicEndpoints
An easy way to access Epic Games' endpoints without clutter.

## Installation
PyPI Page: https://pypi.org/project/EpicEndpoints/

## Usage
```bash
pip install EpicEndpoints
``` 
```python
from EpicEndpoints import EpicEndpoints
```

## Docs

### SimpleDeviceAuthHandler
Class: `SimpleDeviceAuthHandler` <br>
Properties: `access_token`, `device_code`<br>
Functions:<br>
- login() - returns a login url
- device_auth() - returns a dict with display name, device id, account id, and secret

Example:
```python
from EpicEndpoints import EpicEndpoints
import json

handler = EpicEndpoints.SimpleDeviceAuthHandler()

url = handler.login() # Generates a new url to be used in device auth (this MUST be created before using device_auth())
print("Click here: " + url) 
device_auth_details = handler.device_auth() # A dict of device auths is created automatically when the user clicks "confirm"

# Example to store device auths in a json file
data = json.dumps(device_auth_details, sort_keys=False, indent=4)
with open('device_auths.json', 'w') as fp:
    json.dump(data, fp)
```

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
device_auth_details = handler.getDeviceAuthDetails(data['access_token'],data['account_id'])

device = device_auth_details['deviceId']
account = device_auth_details['accountId']
secret = device_auth_details['secret']
```

### Other Functions <br>
`getAccessToken(clientId, secret)`<br>
**params:** a valid client id and secret<br>
**returns:** an access token to access the other endpoints<br>

`getDisplayName(account_id, access_token)`<br>
**params:** an account id and a valid access token<br>
**returns:** the user's display name<br>

## Credits
MixV2 - [EpicResearch](https://github.com/MixV2/EpicResearch) (Data on Endpoints)<br>
AtomicXYZ <br>

