Quickstart for the PDS API Python Client
========================================

This document can get you up to speed with the Python client to the PDS API.


Prerequisites
-------------

Python 3 (tested with 3.7).


Installation
------------

To install this package, run::

    pip install pds.api-client


You can also include it as a dependency in another package, for example, in
your ``install_requires``.

.. warning:: If you use this package a a dependency, you **cannot** use
   ``pds`` as a top-level namespace package in your own software. Just use
   ``pds2`` or anything else. This is a `documented bug`_.


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


Reference Documentation
-----------------------

See `client_api <../api/pds.api_client.html>`_


.. References:
.. _`documented bug`: https://github.com/NASA-PDS/pds-api-client/issues/7