Python Client for Managed Service for Apache Kafka API
======================================================

|preview| |pypi| |versions|

`Managed Service for Apache Kafka API`_: Manage Apache Kafka clusters and resources. 

- `Client Library Documentation`_
- `Product Documentation`_

.. |preview| image:: https://img.shields.io/badge/support-preview-orange.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-managedkafka-schemaregistry.svg
   :target: https://pypi.org/project/google-cloud-managedkafka-schemaregistry/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-managedkafka-schemaregistry.svg
   :target: https://pypi.org/project/google-cloud-managedkafka-schemaregistry/
.. _Managed Service for Apache Kafka API: https://cloud.google.com/managed-service-for-apache-kafka/docs
.. _Client Library Documentation: https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/summary_overview
.. _Product Documentation:  https://cloud.google.com/managed-service-for-apache-kafka/docs

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Managed Service for Apache Kafka API.`_
4. `Set up Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Managed Service for Apache Kafka API.:  https://cloud.google.com/managed-service-for-apache-kafka/docs
.. _Set up Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Installation
~~~~~~~~~~~~

Install this library in a virtual environment using `venv`_. `venv`_ is a tool that
creates isolated Python environments. These isolated environments can have separate
versions of Python packages, which allows you to isolate one project's dependencies
from the dependencies of other projects.

With `venv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`venv`: https://docs.python.org/3/library/venv.html


Code samples and snippets
~~~~~~~~~~~~~~~~~~~~~~~~~

Code samples and snippets live in the `samples/`_ folder.

.. _samples/: https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-managedkafka-schemaregistry/samples


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Our client libraries are compatible with all current `active`_ and `maintenance`_ versions of
Python.

Python >= 3.7

.. _active: https://devguide.python.org/devcycle/#in-development-main-branch
.. _maintenance: https://devguide.python.org/devcycle/#maintenance-branches

Unsupported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python <= 3.6

If you are using an `end-of-life`_
version of Python, we recommend that you update as soon as possible to an actively supported version.

.. _end-of-life: https://devguide.python.org/devcycle/#end-of-life-branches

Mac/Linux
^^^^^^^^^

.. code-block:: console

    python3 -m venv <your-env>
    source <your-env>/bin/activate
    pip install google-cloud-managedkafka-schemaregistry


Windows
^^^^^^^

.. code-block:: console

    py -m venv <your-env>
    .\<your-env>\Scripts\activate
    pip install google-cloud-managedkafka-schemaregistry

Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Managed Service for Apache Kafka API
   to see other available methods on the client.
-  Read the `Managed Service for Apache Kafka API Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `README`_ to see the full list of Cloud
   APIs that we cover.

.. _Managed Service for Apache Kafka API Product documentation:  https://cloud.google.com/managed-service-for-apache-kafka/docs
.. _README: https://github.com/googleapis/google-cloud-python/blob/main/README.rst

Logging
-------

This library uses the standard Python :code:`logging` functionality to log some RPC events that could be of interest for debugging and monitoring purposes.
Note the following:

#. Logs may contain sensitive information. Take care to **restrict access to the logs** if they are saved, whether it be on local storage or on Google Cloud Logging.
#. Google may refine the occurrence, level, and content of various log messages in this library without flagging such changes as breaking. **Do not depend on immutability of the logging events**.
#. By default, the logging events from this library are not handled. You must **explicitly configure log handling** using one of the mechanisms below.

Simple, environment-based configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable logging for this library without any changes in your code, set the :code:`GOOGLE_SDK_PYTHON_LOGGING_SCOPE` environment variable to a valid Google
logging scope. This configures handling of logging events (at level :code:`logging.DEBUG` or higher) from this library in a default manner, emitting the logged
messages in a structured format. It does not currently allow customizing the logging levels captured nor the handlers, formatters, etc. used for any logging
event.

A logging scope is a period-separated namespace that begins with :code:`google`, identifying the Python module or package to log.

- Valid logging scopes: :code:`google`, :code:`google.cloud.asset.v1`, :code:`google.api`, :code:`google.auth`, etc.
- Invalid logging scopes: :code:`foo`, :code:`123`, etc.

**NOTE**: If the logging scope is invalid, the library does not set up any logging handlers.

Environment-Based Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Enabling the default handler for all Google-based loggers

.. code-block:: console

    export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google

- Enabling the default handler for a specific Google module (for a client library called :code:`library_v1`):

.. code-block:: console

    export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google.cloud.library_v1


Advanced, code-based configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also configure a valid logging scope using Python's standard `logging` mechanism.

Code-Based Examples
^^^^^^^^^^^^^^^^^^^

- Configuring a handler for all Google-based loggers

.. code-block:: python

    import logging
    
    from google.cloud import library_v1
    
    base_logger = logging.getLogger("google")
    base_logger.addHandler(logging.StreamHandler())
    base_logger.setLevel(logging.DEBUG)

- Configuring a handler for a specific Google module (for a client library called :code:`library_v1`):

.. code-block:: python

    import logging
    
    from google.cloud import library_v1
    
    base_logger = logging.getLogger("google.cloud.library_v1")
    base_logger.addHandler(logging.StreamHandler())
    base_logger.setLevel(logging.DEBUG)

Logging details
~~~~~~~~~~~~~~~

#. Regardless of which of the mechanisms above you use to configure logging for this library, by default logging events are not propagated up to the root
   logger from the `google`-level logger. If you need the events to be propagated to the root logger, you must explicitly set
   :code:`logging.getLogger("google").propagate = True` in your code.
#. You can mix the different logging configurations above for different Google modules. For example, you may want use a code-based logging configuration for
   one library, but decide you need to also set up environment-based logging configuration for another library.

   #. If you attempt to use both code-based and environment-based configuration for the same module, the environment-based configuration will be ineffectual
      if the code -based configuration gets applied first.

#. The Google-specific logging configurations (default handlers for environment-based configuration; not propagating logging events to the root logger) get
   executed the first time *any* client library is instantiated in your application, and only if the affected loggers have not been previously configured.
   (This is the reason for 2.i. above.)
