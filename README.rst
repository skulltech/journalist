journalist
==========

App to write journal digitally.

|PyPI version|

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

Writing journal
~~~~~~~~~~~~~~~

Journals are stored in the directory ``~/.journalist`` in the following
structure.

.. code:: console

    .journalist
    └── journalname
         └── YYYY
            └── MM
                └── YYYY-MM-DD-Day.md

For example, an example ``~/.Journalist`` directory may contain

.. code:: console

    sumit@HAL9000:pts/0->/home/sumit (0) 
    > tree .journalist 
    .journalist
    ├── personal
    │   ├── 2017
    │   │   └── 12
    │   │       └── 2017-12-28-Thu.md
    │   └── 2018
    │       └── 01
    └── technical
        ├── 2017
        │   └── 12
        │       ├── 2017-12-28-Thu.md
        │       └── 2017-12-29-Fri.md
        └── 2018
            └── 01
                └── 2018-01-03-Wed.md

    10 directories, 4 files

To write in a the journal *personal*, type in the following...

.. code:: console

    sumit at HAL9000 in ~
    $ python3 journalist.py write personal

-  If any journal named *personal* already exists, it will open up the
   relevant ``.md`` file corresponding to the system date (creating it
   if it doesn't exist).
-  If any journal named *personal* doesn't exist, it will prompt the
   user if they want to create a new journal. If they agree, it will do
   so and open the corresponding ``.md`` file as described above.

The *markdown* file will be opened in the editor mentioned in the
``config.yaml`` file (default is ``nano``). If you change it to
something else, make sure an file named ``filename.md`` can be opened
using that editor by typing ``editor filename.md`` in the terminal.

Viewing journal
~~~~~~~~~~~~~~~

.. code:: console

    sumit at HAL9000 in ~ 
    $ python3 journalist.py view personal 
    [*] Starting Journalist viewer webapp...
    [*] View this journal at http://127.0.0.1:5000/journalist?name=personal
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Opening the `URL <http://127.0.0.1:5000/journalist?name=personal>`__
http://127.0.0.1:5000/journalist?name=personal in the browser would show
us the journal entries rendered in HTML.

.. |PyPI version| image:: https://badge.fury.io/py/journalist.svg
   :target: https://badge.fury.io/py/journalist
