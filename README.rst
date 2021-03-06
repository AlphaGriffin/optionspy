############################
Alpha Griffin Python Options
############################

Options for Python.

.. contents:: Table of Contents
   :depth: 2
   :local:



************
Introduction
************

This options class converts an easy to read YAML file into a python object.
Just add a config.yaml in the root directory, or point to the configuration file in the constructor.

General Use:
    Managing of mulitple sets of API keys, across multiple sites with easy.
**************
Python Library
**************

.. toctree::
   API Documentation <api/modules>


Dependencies
============

- Python 3
- *For building documentation (optional):* sphinx and sphinx_rtd_theme (``pip install sphinx sphinx_rtd_theme``)


Build Overview
==============

Both a Makefile and setup.py are provided and used. The setup.py uses Python's standard setuptools package and you can call this script directly to do the basic Python tasks such as creating a wheel, etc.

The most common project build tasks are all provided in the Makefile. To see the full list of project targets::

    make help

Sphinx is used to generate html documentation and man pages. All documentation (html as well as man pages) may be regenerated at any time with::

    make docs

Every so often, when new source class files are created or moved, you will want to regenerate the API documentation templates. These templates may be modified by hand so this task does not overwrite existing files; you'll need to remove any existing files from ``api/`` that you want recreated. Then generate the API templates and re-build all documentation as follows::

    make apidoc
    make docs

You can call ``make python`` if you need to rebuild the Python code (this target simply delegates to ``./setup.py build``).

Build all the common tasks (including documentation) as follows::

    make all

To clean up all the common generated files from your project folder::

    make clean


Installing
==========

For quick and painless install try::

    python3 -m pip install -U git+https://github.com/AlphaGriffin/optionspy

To install this project to the local system::

    make install

Note that you may need superuser permissions to perform the above step.


Using
=====

If you have already installed the project to the system then it's as simple as::

    from ag.options import FIXME

If you have not installed the project system-wide or you have some changes to try, you must add the project folder to Python's search path first::

    import sys, os
    sys.path.insert(0, os.path.abspath('/path/to/printpy'))
    from ag.options import FIXME


Examples
========

A simple Example usage::

    from ag.options import Options
    config = Options()
    email_addr = config.email_addr



*******
History
*******

All changes are tracked in the `CHANGELOG <CHANGELOG>`_ file.

.. include:: CHANGELOG
