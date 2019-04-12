Installation
============

Virtual environment
-------------------

First, let's set up a virtual environment.
We will setup a virtual environment through Conda, but you are free to use other environments, such as venv or pipenv, because they all have the same underlying structure.

You will need to install the minimal installation of conda: Miniconda, because I like respecting your computer storage space.
Visit website for windows/linux installation Miniconda <https://conda.io/miniconda.html>.

If you are using MacOS, you can install Conda easily with Homebrew Cask::

   brew cask miniconda

Then, you need to add miniconda (or anaconda) to your path by adding this line to your .bash_profile script in your home directory (may need to create new file)::

   vim ~/.bash_profile
   export PATH=/usr/local/miniconda3/bin:"$PATH"

Now, create a new virtual environement and load the environment::

   conda create -n narc
   source activate narc

Build and test
--------------

For a system-wide installation, go to the directory containing setup.py and run::

   sudo pip install .

or to install locally for just the current user, run::

   pip install --user .

To run tests using nose2, run::

   nose2

or::

   python setup.py tests
