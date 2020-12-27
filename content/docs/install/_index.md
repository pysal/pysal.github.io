---
title: Install
---

PySAL offers several options for installation. The PySAL meta-package can be
used to install all the packages in the ecosystem. Alternatively, users
can select individual packages for installation.


## Installing the PySAL meta-package
If you want to explore the full potential of PySAL, the PySAL
meta-package comprised of all the individual packages can be
installed in a variety of ways.

### Installing PySAL via Conda
   
    conda install --channel conda-forge pysal
   
### Install PySAL via pip

    pip install pysal

## Installing individual packages

Each individual package in the PySAL ecosystem can also installed individually
via pip or from source.  Take `giddy` as an example:

### Installing via pip

Since giddy has been [released](http://pypi.python.org/pypi/giddy) on
the Python Package Index, users could download the distribution file and
install it manually or from the command line using \`pip\`:

    pip install giddy

Alternatively, grab the source distribution (.tar.gz) and decompress it
to your selected destination. Open a command shell and navigate to the
decompressed giddy folder. Type:

    python setup.py install

### Installing from the source
Those who are interested in contributing to developing `giddy` or want
to explore the newest features can checkout `giddy` using **git**:

    git clone https://github.com/pysal/giddy.git

Open a command shell and navigate to the cloned pysal directory. Type:

    python setup.py install

Keep up to date with pysal development by 'pulling' the latest changes:

    git pull
