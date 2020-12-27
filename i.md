Installation
============

The installation of PySAL could be done in different manners:

-   Installing the PySAL Legacy is introduced in PySAL-Legacy.
-   A one-shot solution to the installation of all the PySAL packages is
    to install the PySAL Metapackage, which is introduced in
    PySAL-Metapackage.
-   For installing individual packages, such as esda and spreg, see
    PySAL-Individual below.

Installing the PySAL Legacy
---------------------------

<h3>Installing via pip</h3>
The PySAL Legacy is [available](http://pypi.python.org/pypi/pysal) on
the Python Package Index, which means it can be downloaded and installed
manually or from the command line using pip, as follows:

    pip install pysal

Alternatively, grab the source distribution (.tar.gz) and decompress it
to your selected destination. Open a command shell and navigate to the
decompressed pysal folder. Type:

    python setup.py install

Installing the PySAL Metapackage
--------------------------------

If you want to explore the full potential of PySAL, the PySAL
Metapackage comprised of all the individual packages should be
installed.

Installing individual packages
------------------------------

Each individual package could be installed by itself via pip or from
source. However, it should be noted that some packages rely on others as
dependencies. For example, `giddy` has `esda`, `mapclassify` and
`libpysal` as dependencies, which means that the installation of `giddy`
will automatically install `esda`, `mapclassify` and `libpysal` if your
machine does not have these three packages pre-installed. Take `giddy`
as an example:

<h3>Installing via pip</h3>
Since giddy has been [released](http://pypi.python.org/pypi/giddy) on
the Python Package Index, users could download the distribution file and
install it manually or from the command line using \`pip\`:

    pip install giddy

Alternatively, grab the source distribution (.tar.gz) and decompress it
to your selected destination. Open a command shell and navigate to the
decompressed giddy folder. Type:

    python setup.py install

<h3>Installing from the source</h3>
Those who are interested in contributing to developing `giddy` or want
to explore the newest features can checkout `giddy` using **git**:

    git clone https://github.com/pysal/giddy.git

Open a command shell and navigate to the cloned pysal directory. Type:

    python setup.py install

Keep up to date with pysal development by 'pulling' the latest changes:

    git pull
