Developer Notes
===============

If you're a developer or maintainer of this package, this document's for you.
This tells you how to generate and maintain the PDS API client.

Automatically generates a python client library from OpenApi specification of the `PDS federated API`_.

.. warning:: The link to the PDS federated API may be offline and/or not found.


Requisites
----------

• code generator https://github.com/OpenAPITools/openapi-generator
• python 3.7
  

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

First, install OpenAPI Generator, then run::

    openapi-generator generate -g python -i swagger.json --package-name pds.api_client --additional-properties=packageVersion=X.Y.Z.
    cp .gitignore-orig .gitignore

Replace ``X.Y.Z`` with the version of the package you're creating. The second
step is necessary because the OpenAPI generator blithely clobbers our
precious ``.gitignore`` file.

.. note:: Use ``openapi-generator`` version 5.2.1 or newer in order to work
   around a bug in the generator.

Note that there still may be a bug in the generator, even at version 5.2.1. If
that's the case, you can try a patched version by `Thomas Loubrieu`_ as
follows::

    cd /tmp
    git clone https://github.com/tloubrieu-jpl/openapi-generator.git
    cd /tmp/openapi-generator
    ./mvnw -Dmaven.test.skip=true clean package

Then instead of using ``openapi-generator`` as above, do this instead::

    java -jar /tmp/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate -g python-legacy -i swagger.json --package-name pds.api_client --additional-properties=packageVersion=X.Y.Z

again, replacing ``X.Y.Z``. Note that Thomas has reported_ this issue and made
a `pull request`_, but they remain open as of this writing (2021-09-22).


Installation
~~~~~~~~~~~~

Do the following commands in a Python virtual environment::

    pip install --requirement requirements.txt
    python setup.py install


Testing
~~~~~~~

To test it, try the virtual environment's Python::

    python client-demo.py


PyPI Publication
~~~~~~~~~~~~~~~~

Try::

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
.. _`PDS federated API`: https://app.swaggerhub.com/apis/PDS_APIs/pds_federated_api/0.0#/info
.. _`Thomas Loubrieu`: https://github.com/tloubrieu-jpl
.. _reported: https://github.com/OpenAPITools/openapi-generator/issues/10005
.. _`pull request`: https://github.com/OpenAPITools/openapi-generator/pull/10004
