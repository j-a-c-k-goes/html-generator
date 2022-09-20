**************
HTML GENERATOR
**************
**Version September 2022**
 
Project Motivations
==========================================================
* Experiencing an increased volume in generation of .html and .css files.
* Noticing that copy and pasting not as effective due to increased volume of needed files.
* Seeking Exposure to command-line parsing.

Project Goals
==========================================================
* Generate desired files for faster development.
* Deliver more content-containers than shells. 
* Integrate workflow into design system.

How To Install
==========================================================
1. ``python3 --version`` 
	*check your version of python, use <3.0*
2. ``gh repo clone j-a-c-k-goes/html-generator``
3. ``cd html-generator``
4. You are ready to roll!

How To Use (HTML Example)
==================================================================
1. ``poetry shell`` 
	*Enters virtual environment (I am using Poetry)*
2. ``python html-file.py --file "file.html" --h1 "Hello" --destination "./output/"``
3. ``python html-file.py --help``

Notes On Flags (HTML Example)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``--file`` 
	expects a string, use the entire file's name (index.html, for example).

* ``--h1`` 
	expects a string (like a heading title). 
	
* ``--destination`` 
	expects the absolute path to where the file will live. 