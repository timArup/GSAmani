from dataclasses import dataclass
import string
import requests
import json
import msal
import appdirs
import os
import atexit
import jsons
from enum import Enum
from typing import List, Tuple, Optional, Any, Dict

# Utilities

def test():
    print('arupcomputepy has installed correctly')

# Connection to AC

class Connection:

    clientName = 'arupcomputepy'
    timeout = None
    root = 'https://compute.arup.digital/api' # e.g. if you want to use dev change to 'https://arupcompute-dev.azurewebsites.net/api'

    def __init__(self, jobnumber):
        self.jobnumber = self.valid_jn(jobnumber)
        self.useModeEnvVarClientSecretFallbackInteractive()

    def getAccessToken(self):
        am = self.authentication_mode

        if am == AuthenticationMode.device:
            return AcquireNewAccessTokenDeviceFlow()
        elif am == AuthenticationMode.interactive:
            return AcquireNewAccessTokenInteractiveFlow()
        elif am == AuthenticationMode.client_secret:
            return AcquireNewAccessTokenClientSecretFlow(self.clientId, self.clientSecret)
        elif am == AuthenticationMode.env_var_client_secret:
            return AcquireNewAccessTokenEnvVarClientSecretFlow(self.clientIdEnvVar, self.clientSecretEnvVar)
        elif am == AuthenticationMode.env_var_client_secret_fallback_interactive:
            return AcquireNewAccessTokenEnvVarClientSecretFallbackInteractive(self.clientIdEnvVar, self.clientSecretEnvVar)
        else:
            raise Exception(f'Authentication mode not supported: {am}')

    def useModeDevice(self):
        self.authentication_mode = AuthenticationMode.device

    def useModeInteractive(self):
        self.authentication_mode = AuthenticationMode.interactive
    
    def useModeClientSecret(self, clientId, clientSecret):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.authentication_mode = AuthenticationMode.client_secret

    def useModeEnvVarClientSecret(self, clientIdEnvVar="COMPUTE_CLIENTID", clientSecretEnvVar="COMPUTE_CLIENTSECRET"):
        self.clientIdEnvVar = clientIdEnvVar
        self.clientSecretEnvVar = clientSecretEnvVar
        self.authentication_mode = AuthenticationMode.env_var_client_secret

    def useModeEnvVarClientSecretFallbackInteractive(self, clientIdEnvVar="COMPUTE_CLIENTID", clientSecretEnvVar="COMPUTE_CLIENTSECRET"):
        self.clientIdEnvVar = clientIdEnvVar
        self.clientSecretEnvVar = clientSecretEnvVar
        self.authentication_mode = AuthenticationMode.env_var_client_secret_fallback_interactive

    def valid_jn(self, jn):
        if(jn == None):
            raise Exception('Job number cannot be None')

        jn = jn.replace('-','')

        if(not jn.isdigit()):
            raise Exception('Job number must only consist of digits, no letters or special characters allowed')

        if(len(jn) < 8 or len(jn) > 8):
            raise Exception('Job number must be in 8-digit format i.e. 12345678')

        junk = ['00000000', '12345678', '12345600', '99999999']
        if(jn in junk):
           raise Exception('Must be a real job number')

        return jn[:8]

class AuthenticationMode(Enum):
    device = 1,
    interactive = 2,
    client_secret = 3,
    env_var_client_secret = 4,
    env_var_client_secret_fallback_interactive = 5

# API objects

@dataclass
class ArupComputeResultItem:
    value: Any
    symbol: str
    description: Optional[str]

class ArupComputeResult:
    remarks: Optional[List[str]]
    warnings: Optional[List[str]]
    errors: Optional[List[str]]
    arupComputeReport: Optional[str]
    arupComputeReport_HTML: Optional[str]
    arupComputeResultItems: List[ArupComputeResultItem]

    arupComputeResultItemsDict: Optional[Dict[str,Any]]
    def createResultDict(self):
        try:
            self.arupComputeResultItemsDict
        except:
            self.arupComputeResultItemsDict = {}
            for acri in self.arupComputeResultItems:
                self.arupComputeResultItemsDict[acri.symbol] = acri.value

    def __getitem__(self, key):
        self.createResultDict()
        return self.arupComputeResultItemsDict[key]

    def availableResults(self):
        self.createResultDict()
        return list(self.arupComputeResultItemsDict.keys())

    def valid(self):
        
        # all optional / lists, so can deserialise nonsense
        # do a validity check that at least one of the required properties has been set
        # performed in likelihood order for early return
        if(
            hasattr(self, 'arupComputeResultItems') and len(self.arupComputeResultItems) > 0
            or hasattr(self, 'arupComputeReport_HTML')
            or hasattr(self, 'errors') and len(self.errors) > 0
            or hasattr(self, 'warnings') and len(self.warnings) > 0
            or hasattr(self, 'remarks') and len(self.remarks) > 0
            or hasattr(self, 'arupComputeReport')
        ):
            return True

        return False

# API endpoints

def MakeCalculationRequest(connection: Connection, calcID: int, isBatch: bool, variables=None, resultType="mini"):
    '''
    Sends calculation(s) to the ArupCompute server for execution and returns the result.

    First time running will require the creation of an Azure access token. This will be guided via the console. Alternatively execute the 'AcquireAccessToken' function.

    :param calcID: calculation identifier, find using the ArupCompute web interface NOTE this is pegged to a specific library version and will NOT automatically be updated to take benefit from bugfixes
    :param jobNumber: jobNumber this calculation is associated with
    :param isBatch: is this a batch calculation (multiple calculations in one request)?
    :param variables: Dictionary of variables to feed key = variable name, value = value to run (names and formatting as per ArupCompute URL). All required data types can be handled.
    :param useArupProxy: try and use False initially, otherwise True may be required
    :param timeout: how long to wait for a server response before failing
    :param client: defaults to 'arupcomputepy' but if developing your own application utilising this library please override this
    :param clientId: required as part of the client secret flow, obtained from Azure App Registration
    :param clientSecret: the client secret associated with your app registration
    :param resultType: either "full" - everything that the library provides, "simple" - limited to ArupComputeResult (results, reports, messages), or "mini" - just results. Defaults to "mini".
    
    :return: server response as JSON
    '''

    checkResultType = ['full','mini','simple']
    if (resultType not in checkResultType):
        raise Exception(f"Entered result type '{resultType}', but only 'full', 'simple', or 'mini' keyword arguments are allowed")

    endpoint = f'calcrecords?calcId={calcID}&jobNumber={connection.jobnumber}&client={connection.clientName}&isBatch={isBatch}&resultType={resultType}'
    
    content = MakeGenericRequest(connection, endpoint, body=variables) 
    try:
        if(isBatch):
            acrs = jsons.loads(content['output'], List[ArupComputeResult])
            for acr in acrs:
                if(acr.valid() == False): # is this annoying if just one item fails?
                    raise Exception('ArupComputeResult was not valid, reverting to pure JSON')
            return acrs
        else:
            acr = jsons.loads(content['output'], ArupComputeResult)
            if(acr.valid()):
                return acr
            else:
                raise Exception('ArupComputeResult was not valid, reverting to pure JSON')
    except Exception as e:
        return json.loads(content['output'])

def MakeGenericRequest(connection: Connection, endpoint: string, body=None):
    '''
    Sends a generic API request to ArupCompute. For API documentation look here https://arupcompute-dev.azurewebsites.net/api/docs/index.html

    :param endpoint: everything after https://compute.arup.digital/api, for example if you want to hit https://compute.arup.digital/api/CalcRecords just pass in 'CalcRecords'
    :param body: if you are hitting a POST endpoint put the payload here in JSON format
    :param accessToken: ArupCompute access token, use helper methods in arupcomputepy to obtain this (e.g. AcquireNewAccessTokenDeviceFlow, AcquireNewAccessTokenClientSecretFlow)
    :param timeout: how long to wait for a server response before failing
    :param useArupProxy: whether to use the Arup proxy servers or not (may be required where porous networking is not enabled)
    '''
    
    token = connection.getAccessToken()
    headers = {'Authorization': f'Bearer {token}'}

    url = connection.root + '/' + endpoint

    if(body):
        r = requests.post(url, json=body, headers=headers, timeout=connection.timeout)
    else:
        r = requests.get(url, headers=headers, timeout=connection.timeout)

    try:
        r.raise_for_status() # check for failed responses e.g. 400
    except requests.exceptions.HTTPError as e:
        if r.text:
            raise requests.exceptions.HTTPError('ArupCompute error: {} HTTP error: {}'.format(r.text, str(e)))
        else:
           raise e

    if '<title>Sign in to your account</title>'.encode('utf-8') in r.content:
        raise SystemError('Connection has been unsuccessful, check authentication and / or proxy requirements. If unsuccessful raise an issue at https://gitlab.arup.com/arupcompute/arupcomputepy/issues')

    content = json.loads(r.content)
    return content

# Dealing with access tokens

def SerializeCache(token_cache, cache):
    open(token_cache, "w").write(cache.serialize())

def AcquireNewAccessTokenDeviceFlow(refreshToken=None, verbose=False):
    return PublicClientApplicationFlow("device_flow", refreshToken, verbose)

def AcquireNewAccessTokenInteractiveFlow(refreshToken=None, verbose=False):
    return PublicClientApplicationFlow("interactive", refreshToken, verbose)


def PublicClientApplicationFlow(mode, refreshToken=None, verbose=False):

    tenant = '4ae48b41-0137-4599-8661-fc641fe77bea'
    clientId = '765d8aec-a87c-4d7d-be95-b3456ef8b732'
    authority_url = 'https://login.microsoftonline.com/' + tenant
    scopes = ["api://df8247c5-9e83-4409-9946-6daf9722271a/access_as_user"]

    # Cache implementation: https://msal-python.readthedocs.io/en/latest/index.html?highlight=PublicClientApplication#tokencache
    userDataDir = appdirs.user_data_dir('Compute','Arup')
    token_cache = os.path.join(userDataDir,'TokenCachePy.msalcache.bin')
    
    if not os.path.exists(userDataDir):
        os.makedirs(userDataDir)

    result = None
    cache = msal.SerializableTokenCache()
    if os.path.exists(token_cache):
        cache.deserialize(open(token_cache, "r").read())

    atexit.register(lambda: SerializeCache(token_cache, cache)
        # Hint: The following optional line persists only when state changed
        if cache.has_state_changed else None
        )

    app = msal.PublicClientApplication(clientId, authority=authority_url, token_cache=cache)
    accounts = app.get_accounts()
    if accounts:
        # If so, you could then somehow display these accounts and let end user choose
        # Assuming the end user chose this one
        chosen = accounts[0]
        if verbose:
            print("Using default account: " + chosen["username"])
        # Now let's try to find a token in cache for this account
        result = app.acquire_token_silent(scopes, account=chosen)

    if not result:
        if(mode == "device_flow"):
            # So no suitable token exists in cache. Let's get a new one from AAD.
            flow = app.initiate_device_flow(scopes=scopes)
            print(flow["message"])
            # Ideally you should wait here, in order to save some unnecessary polling
            # input("Press Enter after you successfully login from another device...")
            result = app.acquire_token_by_device_flow(flow)  # By default it will block
        else:
            result = app.acquire_token_interactive(scopes=scopes)

    if "access_token" in result:
        if cache.has_state_changed:
            SerializeCache(token_cache, cache)
        return result['access_token']
    else:
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))  # You may need this when reporting a bug

def AcquireNewAccessTokenClientSecretFlow(clientId, clientSecret):

    # https://github.com/AzureAD/microsoft-authentication-library-for-python/blob/dev/sample/confidential_client_secret_sample.py
    
    tenant = '4ae48b41-0137-4599-8661-fc641fe77bea'
    authority_url = 'https://login.microsoftonline.com/' + tenant
    scopes = ['api://df8247c5-9e83-4409-9946-6daf9722271a/.default']

    app = msal.ConfidentialClientApplication(clientId, authority=authority_url, client_credential=clientSecret)

    result = None

    result = app.acquire_token_silent(scopes, account=None)

    if not result:
        result = app.acquire_token_for_client(scopes=scopes)
    
    if "access_token" in result:
        return result['access_token']
    else:
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))  # You may need this when reporting a bug

def AcquireNewAccessTokenEnvVarClientSecretFlow(clientIdEnvVar="COMPUTE_CLIENTID", clientSecretEnvVar="COMPUTE_CLIENTSECRET"):
    id = os.getenv(clientIdEnvVar)
    secret = os.getenv(clientSecretEnvVar)

    return AcquireNewAccessTokenClientSecretFlow(id, secret)

def AcquireNewAccessTokenEnvVarClientSecretFallbackInteractive(clientIdEnvVar="COMPUTE_CLIENTID", clientSecretEnvVar="COMPUTE_CLIENTSECRET"):
    id = os.getenv(clientIdEnvVar)
    secret = os.getenv(clientSecretEnvVar)

    if((id == None) or (secret == None)):
        return AcquireNewAccessTokenInteractiveFlow()
    else:
        return AcquireNewAccessTokenClientSecretFlow(id, secret)