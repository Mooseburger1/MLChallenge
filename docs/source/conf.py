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

# Standard Packages
import os
import sys

# import sphinx_rtd_theme
# import stanford_theme
import sphinx_audeering_theme


workspace_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(os.path.join(workspace_dir, os.path.basename(workspace_dir)))

# Custom Packages


# -- Project information -----------------------------------------------------

project = "MLChallenge"
copyright = "2020,"
author = "Trieu Phat Luu"
master_doc = "index"
version = "0.1.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# Add napoleon to the extensions list
extensions = [
    "sphinxcontrib.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
]

todo_include_todos = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
# ref. https://help.farbox.com/pygments.html
pygments_style = "fruity"
# pygments_style = "monokai"
# pygments_style = "colorful"
# pygments_style = "vs"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "alabaster"
# html_theme = "sphinx_rtd_theme"
# html_theme = "stanford_theme"
# html_theme_path = [stanford_theme.get_html_theme_path()]
html_theme = "sphinx_audeering_theme"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_context = {
    "display_github": True,
    "github_host": "github.com",
    "github_user": "Mooseburger1",  # Username
    "github_repo": "MLChallenge",  # Repo name
    "github_version": "master",  # Branch
    "conf_py_path": "/docs/",  # Path in the checkout to the docs root
}
html_themes_options = {
    "footer_links": False,
    "display_version": True,
    "logo_only": False,
}
html_favicon = "_static/images/untitled.ico"
html_logo = "_static/images/untitled.jpg"
