import requests
import json
import base64

class DeviceAuthHandler:
    
    def __init__(self) -> None:
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'authorization': "basic YjA3MGYyMDcyOWY4NDY5M2I1ZDYyMWM5MDRmYzViYzI6SEdAWEUmVEdDeEVKc2dUIyZfcDJdPWFSbyN+Pj0+K2M2UGhSKXpYUA==",
        }
        response = requests.request("POST","https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token", data="grant_type=client_credentials", headers=headers)
        self.access_token = json.loads(response.text)['access_token']
    
    def getLoginInfo(self):
        url2 = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/deviceAuthorization"

        querystring2 = {"prompt":"login"}

        payload2 = "prompt=promptType"
        headers2 = {
            'content-type': "application/x-www-form-urlencoded",
            'authorization': f"bearer {self.access_token}",
            }

        response2 = requests.request("POST", url2, data=payload2, headers=headers2, params=querystring2)

        return response2.json()

    def deviceCodeData(self, deviceCode):
        clientToken = "NTIyOWRjZDNhYzM4NDUyMDhiNDk2NjQ5MDkyZjI1MWI6ZTNiZDJkM2UtYmY4Yy00ODU3LTllN2QtZjNkOTQ3ZDIyMGM3"

        url3 = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"

        payload3 = f"grant_type=device_code&device_code={deviceCode}"
        headers3 = {
            'content-type': "application/x-www-form-urlencoded",
            'authorization': f"basic {clientToken}",
            }

        response3 = requests.request("POST", url3, data=payload3, headers=headers3)

        return response3.json()

    def getDeviceAuthDetails(self,access_token,account_id):
        url = f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{account_id}/deviceAuth"

        headers = {
            'content-type': "application/json",
            'authorization': f"bearer {access_token}",
            }

        response = requests.request("POST", url, headers=headers)

        return response.json()

def getDisplayName(account_id, access_token):

  url = "https://account-public-service-prod.ol.epicgames.com/account/api/public/account/"

  querystring2 = {"accountId":account_id}
  
  headers = {
        'content-type': "application/json",
        'authorization': f"bearer {access_token}",
        }

  response = requests.request("GET", url, headers=headers,params=querystring2)

  data = json.loads(response.text)
  print(data)
  return data[0]['displayName']

def getAccessToken(clientId, secret):
    id = clientId + ":" + secret
    clientToken = base64.b64encode(bytes(id, 'utf-8'))
    clientToken = clientToken.decode("utf-8")
    
    url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"

    payload = "grant_type=client_credentials"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': f"basic {clientToken}",
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    data = json.loads(response.text)

    access_token = data['access_token']
    expire = data['expires_in']

    return access_token

def getDeviceCode(access_token):
    url2 = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/deviceAuthorization"

    querystring2 = {"prompt":"login"}

    payload2 = "prompt=promptType"
    headers2 = {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': f"bearer {access_token}",
        }

    response2 = requests.request("POST", url2, data=payload2, headers=headers2, params=querystring2)

    data2 = json.loads(response2.text)
    print(data2)

    return data2

def deviceCodeData(deviceCode, clientId, secret):
    
    id = clientId + ":" + secret
    clientToken = base64.b64encode(bytes(id, 'utf-8'))
    clientToken = clientToken.decode("utf-8")

    url3 = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"

    payload3 = f"grant_type=device_code&device_code={deviceCode}"
    headers3 = {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': f"basic {clientToken}",
        }

    response3 = requests.request("POST", url3, data=payload3, headers=headers3)

    data3 = json.loads(response3.text)

    return data3

def getDeviceAuth(access_token,account_id):
  url = f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{account_id}/deviceAuth"

  headers = {
      'content-type': "application/json",
      'authorization': f"bearer {access_token}",
      }

  response = requests.request("POST", url, headers=headers)

  data = json.loads(response.text)

  return data