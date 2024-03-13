Developer Notes
===============

If you're a developer or maintainer of this package, this document's for you.
This tells you how to generate and maintain the PDS API client.

Automatically generates a python client library from OpenApi specification of the `PDS API`_.

.. warning:: The link to the PDS federated API may be offline and/or not found.


Requisites
----------

• code generator https://github.com/OpenAPITools/openapi-generator
• python 3.9
  

Procedure
---------

The following procedure describes how to generate the client.


Get Repository Updates
~~~~~~~~~~~~~~~~~~~~~~

First time::

    git clone https://github.com/NASA-PDS/pds-api-client.git

Then::

    git pull


Generate the Library
~~~~~~~~~~~~~~~~~~~~
First make sure the swagger.yaml file is up to date. It contains the OpenAPI specification of the API for which we want to generate the client code.
The reference OpenAPI specifications for PDS can be found on `PDS API`_.

Then, install OpenAPI Generator 6.5.0 (e.g. on macos with brew, see https://github.com/OpenAPITools/openapi-generator#1---installation), and run::

    pip install pyyaml
    python src/pds/api_client/preprocess_openapi.py /Users/loubrieu/PycharmProjects/pds-api/specs/PDS_APIs-search-1.1.1-swagger.yaml --version 1.3.0

Manual step, add lines in the setup.py file:

    from setuptools import find_namespace_packages

    packages=find_namespace_packages(where='src/', exclude=["test", "tests"]),
    package_dir={"": "src"},


Installation & Testing
~~~~~~~~~~~~~~~~~~~~~~~
For integration testing you need an Registry API local server deployed on http://localhost:8080

Use the docker compose deployment, see https://nasa-pds.github.io/registry/install/docker-compose.html

Do the following commands in a Python virtual environment::

    tox


Run demo
~~~~~~~~~

    python src/pds/api_client/demo/client-demo.py


PyPI Publication
~~~~~~~~~~~~~~~~

Try::

    pip install wheel
    python setup.py sdist bdist_wheel
    pip install twine
    twine upload --repository testpypi dist/*


Documentation Generation
~~~~~~~~~~~~~~~~~~~~~~~~

Again, using the Python virtual environment::

    pip install sphinx sphinx-rtd-theme
    sphinx-apidoc --separate --implicit-namespace -f -o docs/source/api pds
    sphinx-build docs/source docs/build
    cp -r docs/build/ /tmp/

This will produce copious warnings which you should just ignore for now. Then
publish on GitHub as follows::

    git checkout gh-pages
    cp -R /tmp/html/* . 

and don't forget to commit and push.


.. References:
.. _`PDS API`: https://nasa-pds.github.io/pds-api/specifications.html
