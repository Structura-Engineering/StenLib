# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "StenLib"
copyright = "2023, Structura-Engineering"
author = "Structura-Engineering"
release = "0.1.7"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "analytics_id": "",
    "analytics_anonymize_ip": False,
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    "vcs_pageview_mode": "",
    "style_nav_header_background": "#FFB000",
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}
html_static_path = ["_static"]
# html_css_files = ["css/custom.css"] # TODO: add custom css.(https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html)
# TODO: Fix bug in `make html` giving:
# WARNING: autodoc: failed to import module 'StenEnumUtils' from module 'StenLib'; the following exception was raised:
# No module named 'StenLib'
# WARNING: autodoc: failed to import module 'StenUtils' from module 'StenLib'; the following exception was raised:
# No module named 'StenLib'
# WARNING: autodoc: failed to import module 'StenLib'; the following exception was raised:
# No module named 'StenLib'
