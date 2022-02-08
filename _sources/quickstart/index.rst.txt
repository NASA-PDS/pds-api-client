Quickstart for the PDS API Python Client
========================================

This document can get you up to speed with the Python client to the PDS API.


Prerequisites
-------------

Python 3 (tested with 3.7).

Issues with SSL certificate verification seen with python 3.9.

If it occurs to you, try:

    pip install --upgrade certifi

However, we have not been able to solve that with conda python 3.9.




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

- `CollectionsApi <../api/pds.api_client.api.html#module-pds.api_client.api.collections_api>`_

- `BundleApi <../api/pds.api_client.api.html#module-pds.api_client.api.bundles_apii>`_

- `ProductApi <../api/pds.api_client.api.html#module-pds.api_client.api.products_api>`_ (for all products)


For collections for example:

.. code-block:: python

    from pds.api_client.api.collections_api import CollectionsApi
    from pprint import pprint

    collections = CollectionsApi(api_client)

    try:
        api_response = collections.get_collection(start=0, limit=20)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)


Reference Documentation
-----------------------

See `client_api <../api/pds.api_client.html>`_


.. References:
.. _`documented bug`: https://github.com/NASA-PDS/pds-api-client/issues/7