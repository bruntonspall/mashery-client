Mashery API Python Helper
=========================


This is at it's simplest a helper for using the mashery API.
It contains a module, mashery.py that provides an Api class that can represent a Mashery endpoint, and a helper method call_api_httplib which uses httplib to make a request and return the response.

It also contains a cmd.py which is a command line utility for making arbitrary queries of the mashery API.

Usage
-----

The cmd.py library should require python 2.6 and greater I think (json and httplib), and is used from the command line as

`python cmd.py test.echo here is some parameters that can be echoed`

`python cmd.py application.fetch 12345`

The cmd.py automatically attempts to convert ints so as to not fail params that require ints, but doesn't handle any other complex types
