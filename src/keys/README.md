# keys
The DDI Keys application is a BloxOne DDI service for managing TSIG keys and GSS-TSIG (Kerberos) keys which are used by other BloxOne DDI applications. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.   

The `keys` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 0.1.0
- Generator version: 7.5.0
- Build package: com.infoblox.codegen.BloxonePythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3
* python-dateutil
* pydantic

## Getting Started

In your own code, to use this library to connect and interact with keys,
you can run the following:

```python

import keys
from keys.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = keys.Configuration(
    host = "http://csp.infoblox.com/api/ddi/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with keys.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = keys.GenerateTsigApi(api_client)
    algorithm = 'algorithm_example' # str | The TSIG key algorithm.  Valid values are: * _hmac_sha256_ * _hmac_sha1_ * _hmac_sha224_ * _hmac_sha384_ * _hmac_sha512_  Defaults to _hmac_sha256_. (optional)

    try:
        # Generate TSIG key with a random secret.
        api_response = api_instance.generate_tsig(algorithm=algorithm)
        print("The response of GenerateTsigApi->generate_tsig:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenerateTsigApi->generate_tsig: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GenerateTsigApi* | [**generate_tsig**](keys/docs/GenerateTsigApi.md#generate_tsig) | **GET** /keys/generate_tsig | Generate TSIG key with a random secret.
*KerberosApi* | [**delete**](keys/docs/KerberosApi.md#delete) | **DELETE** /keys/kerberos/{id} | Delete the Kerberos key.
*KerberosApi* | [**list**](keys/docs/KerberosApi.md#list) | **GET** /keys/kerberos | Retrieve Kerberos keys.
*KerberosApi* | [**read**](keys/docs/KerberosApi.md#read) | **GET** /keys/kerberos/{id} | Retrieve the Kerberos key.
*KerberosApi* | [**update**](keys/docs/KerberosApi.md#update) | **PATCH** /keys/kerberos/{id} | Update the Kerberos key.
*TsigApi* | [**create**](keys/docs/TsigApi.md#create) | **POST** /keys/tsig | Create the TSIG key.
*TsigApi* | [**delete**](keys/docs/TsigApi.md#delete) | **DELETE** /keys/tsig/{id} | Delete the TSIG key.
*TsigApi* | [**list**](keys/docs/TsigApi.md#list) | **GET** /keys/tsig | Retrieve TSIG keys.
*TsigApi* | [**read**](keys/docs/TsigApi.md#read) | **GET** /keys/tsig/{id} | Retrieve the TSIG key.
*TsigApi* | [**update**](keys/docs/TsigApi.md#update) | **PATCH** /keys/tsig/{id} | Update the TSIG key.
*UploadApi* | [**upload**](keys/docs/UploadApi.md#upload) | **POST** /keys/upload | Upload content to the keys service.


## Documentation For Models

 - [CreateTSIGKeyResponse](keys/docs/CreateTSIGKeyResponse.md)
 - [DdiuploadResponse](keys/docs/DdiuploadResponse.md)
 - [GenerateTSIGResponse](keys/docs/GenerateTSIGResponse.md)
 - [GenerateTSIGResult](keys/docs/GenerateTSIGResult.md)
 - [KerberosKey](keys/docs/KerberosKey.md)
 - [KerberosKeys](keys/docs/KerberosKeys.md)
 - [ListKerberosKeyResponse](keys/docs/ListKerberosKeyResponse.md)
 - [ListTSIGKeyResponse](keys/docs/ListTSIGKeyResponse.md)
 - [ProtobufFieldMask](keys/docs/ProtobufFieldMask.md)
 - [ReadKerberosKeyResponse](keys/docs/ReadKerberosKeyResponse.md)
 - [ReadTSIGKeyResponse](keys/docs/ReadTSIGKeyResponse.md)
 - [TSIGKey](keys/docs/TSIGKey.md)
 - [UpdateKerberosKeyResponse](keys/docs/UpdateKerberosKeyResponse.md)
 - [UpdateTSIGKeyResponse](keys/docs/UpdateTSIGKeyResponse.md)
 - [UploadContentType](keys/docs/UploadContentType.md)
 - [UploadRequest](keys/docs/UploadRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



