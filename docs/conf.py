# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ALIS: Algorithmic Library for Scalability'
copyright = '2022, AIM PhD in DS 2024'
author = 'AIM PhD in DS 2024'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # 'myst_parser', # For markdown integration
    # 'nbsphinx', # For notebook integration
    # 'IPython.sphinxext.ipython_console_highlighting', # For notebook code cell syntax highlights
    'sphinxcontrib.bibtex', # For bibtex referencing
    'numpydoc', # For numpy docstring format parsing
    'sphinx_copybutton', # Enable copy button for codes
    'myst_nb', # For notebook integration
    'sphinx.ext.githubpages', # For github pages deployment
]

# Myst parser extensions
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Set source suffix of documents
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
}

# Bibtex files
bibtex_bibfiles = ['references.bib']

# Execute notebooks upon building except for some
nbsphinx_execute = 'never'
jupyter_execute_notebooks = "auto"
execution_excludepatterns = [
    'link-analysis/*', 'social-network-graphs/*', 'stream-mining/*',
    'demo-minhash-lsh.ipynb', 'the-lsh-class.ipynb', 'minhashing.ipynb']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_theme_options = {
    'navigation_depth': 4
}

# Mathjax setting
myst_update_mathjax = False
mathjax3_config = {
    'TeX': {'equationNumbers': {'autoNumber': 'AMS', 'useLabelIds': True}},
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom-style.css']

# Numbered reference of figures
numfig = True

# Autosummary generation
numpydoc_show_class_members = False

# Generate autosummary pages
autosummary_generate = True

# Additional extensions
extensions.append('sphinx.ext.todo')
extensions.append('sphinx.ext.autodoc')
extensions.append('sphinx.ext.autosummary')
extensions.append('sphinx.ext.intersphinx')
extensions.append('sphinx.ext.mathjax')
extensions.append('sphinx.ext.viewcode')
extensions.append('sphinx.ext.graphviz')
