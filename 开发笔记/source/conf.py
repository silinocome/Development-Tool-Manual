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
import os
import sys

sys.path.insert(0, os.path.abspath("./docs"))


# -- Project information -----------------------------------------------------

project = "trick&tool"
copyright = "2021, Natsu_Akatsuki"
author = "Natsu_Akatsuki"

# The full version, including alpha/beta/rc tags
release = "v0.0.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx_search.extension",
    "sphinxemoji.sphinxemoji",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx-prompt",
    "sphinx_copybutton",
    "sphinx_toggleprompt",
    "notfound.extension",
    "sphinx_last_updated_by_git",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "zh_CN"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["**/*.md"]

source_suffix = {
    ".rst": "restructuredtext",
    # ".txt": "markdown",
    # ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------

# 设置html主题
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# 配置构建html时导入的静态文件
html_static_path = ["_static", "pdf资料"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
html_extra_path = ["baidu_verify_code-7LJoOcUZFp.html"]

[extensions]
todo_include_todos=True
todo_emit_warnings=False

today_fmt = '%b %d %y at %H:%M'