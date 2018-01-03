journalist
==========

App to write journal digitally.

Features
--------

-  Write your journal using *Markdown* in your favorite text-editor.
-  Stores written journals in a comprehensive directory structure.
-  View the journals (*Markdown* rendered in *HTML*) in browser.

Installation
============

Install it using ``pip``

.. code:: console

    pip install journalist

Usage
=====

.. code:: console

    sumit at HAL9000 in ~ 
    $ python3 journalist.py -h
    usage: journalist.py [-h] {write,view} name

    positional arguments:
      {write,view}  Task to do
      name          The name of the journal

    optional arguments:
      -h, --help    show this help message and exit

Usage Examples
--------------

Writing in a journal named *"Personal"*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: console

    sumit at HAL9000 in ~
    $ python3 journalist.py write personal

Viewing the *"Personal"* journal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: console

    sumit at HAL9000 in ~ 
    $ python3 journalist.py view personal 
    [*] Starting Journalist viewer webapp...
    [*] View this journal at http://127.0.0.1:5000/journalist?name=personal
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Opening the URL http://127.0.0.1:5000/journalist?name=personal in the
browser would show us the journal entries rendered in HTML.
