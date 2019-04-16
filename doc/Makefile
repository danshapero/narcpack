# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help clean Makefile

html: Makefile source/index.rst
	sphinx-apidoc --force --separate --maxdepth=1 --module-first --output-dir source ../narcpack
	rm source/modules.rst
	sed -i 's/narcpack package/API reference/g' source/narcpack.rst
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	rm -rf build source/narcpack*
