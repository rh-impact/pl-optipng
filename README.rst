pl-optipng
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-optipng?sort=semver
    :target: https://hub.docker.com/r/fnndsc/pl-optipng

.. image:: https://img.shields.io/github/license/fnndsc/pl-optipng
    :target: https://github.com/FNNDSC/pl-optipng/blob/master/LICENSE


.. contents:: Table of Contents


Abstract
--------

A plugin to recompresses Portable Network Graphics (PNG) image files to a smaller size. This program also converts external formats (BMP, GIF, PNM and TIFF) to optimized PNG, and performs PNG integrity checks and corrections.


Description
-----------


``optipng`` is a *ChRIS ds-type* application that takes in ... as ... files
and produces ...


Usage
-----

.. code::

    docker run --rm fnndsc/pl-optipng optipng
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [--version]
        <inputDir> <outputDir>


Arguments
~~~~~~~~~

.. code::

    [-h] [--help]
    If specified, show help message and exit.
    
    [--json]
    If specified, show json representation of app and exit.
    
    [--man]
    If specified, print (this) man page and exit.

    [--meta]
    If specified, print plugin meta data and exit.
    
    [--savejson <DIR>] 
    If specified, save json representation file to DIR and exit. 
    
    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.
    
    [--version]
    If specified, print version number and exit. 


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-optipng optipng --man

Run
~~~

You need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                             \
        -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
        fnndsc/pl-optipng optipng                        \
        /incoming /outgoing

Follow steps below to reduce the size of a png file or any other external formats mentioned above into a optimized png
----------------------------------------------------------------------------------------------------------------------
- clone repo ``https://github.com/rh-impact/pl-optipng`` by running the command ``git clone https://github.com/rh-impact/pl-optipng``
- Now ``cd`` to the cloned repo
- create a directory called ``in`` inside the repo
- create another directory called ``out`` inside the repo
- In the ``in`` directory download any ``.png`` files and note down their sizes
- Now build the ``Dockerfile`` inside the directory by running the command ``docker build -t local/pl-optipng .``
- With out using the interactive shell you could run the command below to see the size of png file reduced

.. code:: bash

   docker run --privileged --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing localhost/local/pl-optipng optipng /incoming /outgoing

- If you would like to use the interactive shell run the commands below to see the size of png file reduced

.. code:: bash

   - docker run --privileged --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing -it localhost/local/pl-optipng /bin/bash
   - /usr/bin/optipng --help
   - /usr/bin/optipng -dir <outputdir> -- <absolutepath of input png file> (or)
   - /usr/bin/optipng <absolutepath of png file>



Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-optipng .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-optipng nose2

Sample Outputs
--------------

.. code:: bash

   Processing: Sample-png-image-20mb.png
     5891x2271 pixels, 4x8 bits/pixel, RGB+alpha
     Reducing image to 3x8 bits/pixel, RGB
     Input IDAT size = 21134274 bytes
     Input file size = 21141605 bytes
     Trying:
      zc = 9  zm = 8  zs = 0  f = 5		IDAT size = 17612792
      zc = 9  zm = 8  zs = 1  f = 5		IDAT size = 17248219
                               
    Selecting parameters:
     zc = 9  zm = 8  zs = 1  f = 5		IDAT size = 17248219
    Output IDAT size = 17248219 bytes (3886055 bytes decrease)
    Output file size = 17251686 bytes (3889919 bytes = 18.40% decrease)

Examples
--------

Put some examples here!


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
