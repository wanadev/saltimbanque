Saltimbanque
============

Provides an API to convert web pages to PDF.


Dependencies
------------

* Flask
* WeasyPrint


Run for development
-------------------

::

    pip install -e .
    python -m saltimbanque


Run for production
------------------

::

    pip install .
    pip install gunicorn
    gunicorn -w 4 saltimbanque:app


Configuration
-------------

Saltimbanque is configurable trough environment variables. Available configs:

* ``PORT`` (default: 5000 in dev mode, 8000 with gunicorn)


Usage
-----

::

    http://example.org/html-to-pdf/<path:url>

