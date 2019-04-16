# Find all files that end in `.ipynb` in the examples directory and sort them
EXAMPLE_FILES=$(shell find ../examples -not -path '*/\.*' -type f -name '*\.ipynb' | sort)
examples: $(patsubst ../examples/%.ipynb,source/narcpack.examples.%.rst,$(EXAMPLE_FILES))

# For each demo, execute it with a longer timeout, convert it to restructured
# text, and save the result in the `source` directory with `narcpack.examples.`
# prepended to the name.
source/narcpack.examples.%.rst: ../examples/%.ipynb
	jupyter nbconvert --to rst \
			  --execute --ExecutePreprocess.timeout=24000 \
			  --output-dir=./source --output=`basename $@` $<

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help clean Makefile

html: Makefile examples source/index.rst
	sphinx-apidoc --force --separate --maxdepth=1 --module-first --output-dir source ../narcpack
	rm source/modules.rst
	sed -i 's/narcpack package/API reference/g' source/narcpack.rst
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	rm -rf build source/narcpack*
