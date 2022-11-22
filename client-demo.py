from __future__ import print_function
from pds.api_client.rest import ApiException
from pds.api_client import Configuration
from pds.api_client import ApiClient
from pds.api_client.apis.paths.collections import Collections
from pprint import pprint

# create an instance of the API class
configuration = Configuration()
#configuration.host = 'https://pds.nasa.gov/api/search/1.1'
#configuration.host = 'https://pds.nasa.gov/api/search-en-gamma/1.1'
configuration.host = 'http://localhost:8080'
api_client = ApiClient(configuration)


collections = Collections(api_client)

try:
    api_response = collections.get(
        query_params={
            'start': 0,
            'limit': 10,
            "fields": ['ops:Label_File_Info.ops:file_ref']
        },
        accept_content_types=('application/json',)
    ).body
    pprint(api_response.summary)

except ApiException as e:
    print("Exception when calling CollectionsApi->get_collection: %s\n" % e)