# EpicEndpoints
An easy way to access Epic Games' endpoints without clutter.

## Installation
PyPI Page: https://pypi.org/project/EpicEndpoints/

## Usage
`pip install EpicEndpoints` <br>
<br>
`from EpicEndpoints import EpicEndpoints`

## Docs

Functions: <br>
`getAccessToken(clientId, secret)`<br>
`params:` a valid client id and secret
`returns:` an access token to access the other endpoints

`getDisplayName(account_id, access_token)`<br>
`params:` an account id and a valid access token<br>
`returns:` the user's display name<br>

`getDeviceCode(access_token)`
`params:` a valid access token<br>
`returns:` auth data (in dict format) which includes a device code and an associated verification uri<br>

`deviceCodeData(deviceCode, clientId, secret)`
`params:` a valid device code, client id, and secret<br>
`returns:` auth data (in dict format) including a device id, account id, and secret for the user that used the `verification uri` from before
