Quickstart for the PDS API Python Client
========================================

This document can get you up to speed with the Python client to the PDS API.


Prerequisites
-------------

Python 3 (tested with 3.9).

Issues with SSL certificate verification seen with python 3.9.

If it occurs to you, try:

    pip install --upgrade certifi

However, we have not been able to solve that with conda python 3.9.


Installation
------------

To install the latest stable version of this package, run::

    pip install pds.api-client

The package releases match with the `Search API specification <https://nasa-pds.github.io/pds-api/specifications.html>`_, as follows:

.. list-table:: client implementation vs api specification versions
   :widths: 25 25
   :header-rows: 1

   * - pds.api-client
     - pds search api specification
   * - 1.5.X
     - 1.4
   * - 1.4.X
     - 1.3
   * - 1.3.X
     - 1.1.1
   * - 1.2.X
     - 1.1.Y
   * - 1.1.X
     - 1.0
   * - 0.8.Y
     - 0.4

To install a specific version of this package, run, for example::

    pip install pds.api-client==1.4.0


You can also include it as a dependency in another package, for example, in
your ``install_requires``.

.. warning:: If you use this package as a dependency, you **cannot** use
   ``pds`` as a top-level namespace package in your own software. Just use
   ``pds2`` or anything else. This is a `documented bug`_.


Create an API Connection
------------------------

.. code-block:: python

   from __future__ import print_function
   from pds.api_client.rest import ApiException
   from pds.api_client import Configuration
   from pds.api_client import ApiClient


   # create an instance of the API class
   configuration = Configuration()
   configuration.host = 'https://pds.nasa.gov/api/search/1'
   api_client = ApiClient(configuration)


Request One End Point
---------------------

There are multiple API end points which accessible through modules defined in :doc:`/api/pds.api_client.api`

For Collections for example:

.. code-block:: python

    from pds.api_client.api.by_product_classes_api import ByProductClassesApi
    from pprint import pprint

    classes = ByProductClassesApi(api_client)

    api_response = classes.class_list(
        'collections',
        start=0,
        limit=20,
        fields=['ops:Label_File_Info.ops:file_ref']
    )
    pprint(api_response.summary.to_dict())



Reference Documentation
-----------------------

See `client_api <../api/pds.api_client.api.html>`_

.. References:
.. _`documented bug`: https://github.com/NASA-PDS/pds-api-client/issues/7
