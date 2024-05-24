# dns-data
The DNS Data is a BloxOne DDI service providing primary authoritative zone support. DNS Data is authoritative for all DNS resource records and is acting as a primary DNS server. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.   

The `dns_data` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

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

In your own code, to use this library to connect and interact with dns-data,
you can run the following:

```python

import dns_data
from dns_data.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://csp.infoblox.com/api/ddi/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = dns_data.Configuration(
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
with dns_data.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dns_data.RecordApi(api_client)
    body = dns_data.Record() # Record | 
    inherit = 'inherit_example' # str | This parameter is used for getting inheritance_sources. (optional)

    try:
        # Create the DNS resource record.
        api_response = api_instance.create(body, inherit=inherit)
        print("The response of RecordApi->create:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecordApi->create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://csp.infoblox.com/api/ddi/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RecordApi* | [**create**](dns_data/docs/RecordApi.md#create) | **POST** /dns/record | Create the DNS resource record.
*RecordApi* | [**delete**](dns_data/docs/RecordApi.md#delete) | **DELETE** /dns/record/{id} | Move the DNS resource record to recycle bin.
*RecordApi* | [**list**](dns_data/docs/RecordApi.md#list) | **GET** /dns/record | Retrieve DNS resource records.
*RecordApi* | [**read**](dns_data/docs/RecordApi.md#read) | **GET** /dns/record/{id} | Retrieve the DNS resource record.
*RecordApi* | [**soa_serial_increment**](dns_data/docs/RecordApi.md#soa_serial_increment) | **POST** /dns/record/{id}/serial_increment | Increment serial number for the SOA record.
*RecordApi* | [**update**](dns_data/docs/RecordApi.md#update) | **PATCH** /dns/record/{id} | Update the DNS resource record.


## Documentation For Models

 - [CreateRecordResponse](dns_data/docs/CreateRecordResponse.md)
 - [Inheritance2InheritedUInt32](dns_data/docs/Inheritance2InheritedUInt32.md)
 - [ListRecordResponse](dns_data/docs/ListRecordResponse.md)
 - [ProtobufFieldMask](dns_data/docs/ProtobufFieldMask.md)
 - [ReadRecordResponse](dns_data/docs/ReadRecordResponse.md)
 - [Record](dns_data/docs/Record.md)
 - [RecordInheritance](dns_data/docs/RecordInheritance.md)
 - [SOASerialIncrementRequest](dns_data/docs/SOASerialIncrementRequest.md)
 - [SOASerialIncrementResponse](dns_data/docs/SOASerialIncrementResponse.md)
 - [UpdateRecordResponse](dns_data/docs/UpdateRecordResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



