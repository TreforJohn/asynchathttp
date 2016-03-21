asynchathttp server
===================

this is a clone of the python 'httpserver.py' file from shuckc/printerface and developed to create the asynchronous http server for a secure bridge.

Following to be updated: #######

* `asynchathttpserver.py` simple http server using asynchat

    $ wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz
    $ tar -xvf setuptools-1.4.2.tar.gz
    $ cd setuptools-1.4.2
    $ python2.7 setup.py install

    $ easy_install mako
    $ easy_install reportlab==2.7

Unit tests

    $ python -m unittest discover --pattern=*.py

Uses python asyncore/smtp, bootstrap web framework
