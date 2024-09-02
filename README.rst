Saltimbanque
============

Provides a simple Web API to convert web pages to PDF and PNG using WeasyPrint_.

.. _WeasyPrint: https://weasyprint.org/


Dependencies
------------

* Flask
* WeasyPrint


Install
-------

Ensure you have a complete Python 3 installation. On Debian / Ubuntu, run (as root)::

    apt install build-essential python3 python3-dev python3-venv

Then, to install Saltimbanque from PyPI, run (as root)::

    mkdir -p /opt/saltimbanque
    python3 -m venv /opt/saltimbanque/env
    /opt/saltimbanque/env/bin/pip install saltimbanque gunicorn

Alternatively, to install it from Git, run (as root)::

    mkdir -p /opt/saltimbanque
    git clone https://github.com/wanadev/saltimbanque.git /opt/saltimbanque/saltimbanque.git
    python3 -m venv /opt/saltimbanque/env
    /opt/saltimbanque/env/bin/pip install gunicorn
    /opt/saltimbanque/env/bin/pip install -e /opt/saltimbanque/saltimbanque.git

NOTE: If you need the export webpage to PNG, you should install an older WeasyPrint version::

    /opt/saltimbanque/env/bin/pip install weasyprint==52.5


Usage
-----

To run Saltimbanque::

    /opt/saltimbanque/env/bin/gunicorn -w 4 saltimbanque:app

By default it will listen to port 8000. To run it on an other port::

    /opt/saltimbanque/env/bin/gunicorn -w 4 -b 127.0.0.1:8888 saltimbanque:app

Important notes:

* It is recommanded to use supervisor or systemd to start the Saltimbanque server.
* You should also consider to setup a proxy server like Nginx in front of Gunicorn.

You can now open the Saltimbanque root route in your browser to access a demo web page:

* http://localhost:8000/


API
---

To build a PDF from a web page::

    http://localhost:8000/html-to-pdf/<string:base64_url>

To build a PNG from a web page::

    http://localhost:8000/html-to-png/<string:base64_url>

Where:

* ``base64_url`` is the URL of the HTML document, encoded in base64.


NOTE: ``html-to-png`` is no more available since WeasyPrint 53. You should install an older WeasyPrint version if you need this feature. For more information see https://www.courtbouillon.org/blog/00008-weasyprint-53-beta/ .


Contributing
------------

Questions
~~~~~~~~~

If you have any question, you can:

* `Open an issue <https://github.com/wanadev/saltimbanque/issues>`__ on GitHub
* `Ask on Discord <https://discord.gg/BmUkEdMuFp>`__


Bugs
~~~~

Please `open an issue <https://github.com/wanadev/saltimbanque/issues>`__ on GitHub with as much information as possible if you found a bug:

* Your operating system / Linux distribution (and its version)
* How you installed the software
* All the logs and message outputted by the software
* etc.


Pull requests
~~~~~~~~~~~~~

Please consider `filing a bug <https://github.com/wanadev/saltimbanque/issues>`__ before starting to work on a new feature; it will allow us to discuss the best way to do it. It is obviously unnecessary if you just want to fix a typo or small errors in the code.

Please note that your code must follow the coding style defined by the `pep8 <https://pep8.org>`__. `Black <https://black.readthedocs.io/en/stable>`_ and `Flake8 <https://flake8.pycqa.org/en/latest>`__ are used on this project to enforce the coding style.


Lint the code
~~~~~~~~~~~~~

You must install `Nox <https://nox.thea.codes/>`__ first::

    pip install nox

Then you can check for lint error::

    nox --session lint

You can also fix coding style errors automatically with::

    nox -s black_fix


Setup / Run Saltimbanque for dev
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install dependencies::

    python3 -m venv __env__
    __env__/bin/pip install -e ".[dev]"

Run::

    __env__/bin/flask run


Changelog
---------

* **[NEXT]** (changes on ``master``, but not released yet):

  * Nothing yet ;)

* **v1.2.0:**

  * Fixes deployment
  * Updates dependencies
  * Adds PNG raster function in addition to PDF

* **v1.1.1:** Fix encoding issue when decoding URLs
* **v1.1.0:** Encode URL in base64 to avoid issue when used with an Nginx front
* **v1.0.1:** Update deploy config
* **v1.0.0:** Initial release
