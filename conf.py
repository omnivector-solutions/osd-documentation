# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Omnivector Slurm Distribution'
copyright = '2021, Omnivector Solutions'
author = 'Omnivector Solutions'
repo_url = 'https://github.com/omnivector-solutions/osd-documentation/'

master_doc = 'index'

smartquotes = False

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.githubpages',
    'sphinxcontrib.httpdomain',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', 'venv']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_theme_options = {'repository_url' : repo_url,
                      'use_repository_button': True,
                      'use_issues_button': True}

# Add omnilogo to the website
html_logo = 'images/logo.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


# -- Preprocessing steps -----------------------------------------------------
import shutil
shutil.copyfile('../slurm-charms/CHANGELOG', 'changelog.rst')
