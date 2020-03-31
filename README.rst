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

::

    http://example.org/html-to-png/<path:url>


Changelog
---------

* **1.2.0:**

  * Fixes deployment
  * Updates dependencies
  * Adds PNG raster function in addition to PDF

* **1.1.1:** Fix encoding issue when decoding URLs
* **1.1.0:** Encode URL in base64 to avoid issue when used with an Nginx front
* **1.0.1:** Update deploy config
* **1.0.0:** Initial release
