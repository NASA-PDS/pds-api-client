========================================
Quickstart for the PDS API python client
========================================

Prerequisites
-------------

python 3 (tested with 3.7).


Install
-------


    pip install pds.api-client


Create an api connection
------------------------

.. code-block:: python

   from __future__ import print_function
   from pds.api_client.rest import ApiException
   from pds.api_client import Configuration
   from pds.api_client import ApiClient

   configuration = Configuration()
   configuration.host = 'http://pds-gamma.jpl.nasa.gov/api/' # use demo api server
   api_client = ApiClient(configuration)


Request one end point
---------------------

There are different API end points:

- `CollectionsApi <./api/api_client.api.html#module-api_client.api.bundles_api>`_

- `BundleApi <.//api/api_client.api.html#module-api_client.api.collections_api>`_

- `ProductApi <./api/api_client.api.html#module-api_client.api.products_api>`_ (for all products)


For collections for example:

.. code-block:: python

   from pds.api_client import CollectionsApi
   from pprint import pprint

   collections = CollectionsApi(api_client)

   try:
       api_response = collections.get_collection(q="", start=0, limit=20)
       pprint(api_response)
   except ApiException as e:
       print("Exception when calling CollectionsApi->get_collection: %s\n" % e)


Reference documentation
-----------------------

See `client_api <./api/api_client.api.html>`_
