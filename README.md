# pylocal
Build Python Packages Without Publishing

This repository is based on a tutorial by Max Reynolds

https://towardsdatascience.com/building-a-python-package-without-publishing-e2d36c4686cd


## introduction
The purpose is to establish a simple example of how to write python modules to be installed locally. Local packages can be useful for code organization and re-use, allowing you to simply import a module without having to navigate to its directory or re-write code. 

The file structure is important

<pre>
pylocal/
    image_pkg/
              __init__.py
              image_edits.py
              ui.py
    setup.py
</pre>


## build and install the 'examplepackage' module
As defined in setup.py, the name of the module is 'examplepackage'. To install this package in a virtual environment, first create and activate the virtual environment. Here we assume that local environments are established using 'venv' under C:\Python\venv under Windows, but this is up to the user to define.


<pre>
C:\Python\Python38\python -m venv C:\Python\venv\py38Test
C:\Python\venv\py38Test\Scripts\activate
pip install wheel
pip install .
</pre>
