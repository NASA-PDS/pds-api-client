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

Then, install OpenAPI Generator (e.g. on macos with brew, see https://github.com/OpenAPITools/openapi-generator#1---installation), and run::

    rm -fr pds test
    openapi-generator generate -g python -i preprocessed-swagger.json --package-name pds.api_client --additional-properties=packageVersion=X.Y.Z.
    cp .gitignore-orig .gitignore

Replace ``X.Y.Z`` with the version of the package you're creating. The second
step is necessary because the OpenAPI generator blithely clobbers our
precious ``.gitignore`` file.

.. note:: Since a bug fix is needed for nested packages, we should now use the master branch of openapi-generator after commit 22fcdcc0b2c6ce824ad06767837c1a3975d63c0c. git clone the repository and `mvn clean install` with java 1.8.
Then launch the generation of code, for example::

    java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar generate -i /Users/loubrieu/PycharmProjects/pds-api-client/swagger.yaml -g python -o /Users/loubrieu/PycharmProjects/pds-api-client/ --package-name pds.api_client --additional-properties=packageVersion=1.2.0



Installation
~~~~~~~~~~~~

Do the following commands in a Python virtual environment::

    pip install --requirement requirements.txt
    python setup.py install


Testing
~~~~~~~

For testing you need an Registry API local server deployed on http://localhost:8080

Use the docker compose deployment, see https://nasa-pds.github.io/registry/install/docker-compose.html


To test it, try the virtual environment's Python::

    python client-demo.py

    python setup.py test


Note that you need an API server to test on.

PyPI Publication
~~~~~~~~~~~~~~~~

Try::

    pip install wheel
    python setup.py sdist bdist_wheel
    twine upload --repository testpypi dist/*


Documentation Generation
~~~~~~~~~~~~~~~~~~~~~~~~

Again, using the Python virtual environment::

    pip install sphinx sphinx-rtd-theme
    sphinx-apidoc -o docs/source/api pds
    sphinx-build docs/source docs/build
    cp -r docs/build/ /tmp/

This will produce copious warnings which you should just ignore for now. Then
publish on GitHub as follows::

    git checkout gh-pages
    cp -R /tmp/html/* . 

and don't forget to commit and push.


.. References:
.. _`PDS API`: https://nasa-pds.github.io/pds-api/specifications.html
