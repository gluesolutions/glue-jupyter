#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# glue-jupyter documentation build configuration file, created by
# sphinx-quickstart on Wed May 30 10:41:52 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'nbsphinx', 'numpydoc',
              'sphinx_automodapi.automodapi',
              'sphinx_automodapi.smart_resolver']

numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.ipynb']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'glue-jupyter'
copyright = '2018, Maarten A. Breddels'
author = 'Maarten A. Breddels'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.1'
# The full version, including alpha/beta/rc tags.
release = '0.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'glue-jupyterdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'glue-jupyter.tex', 'glue-jupyter Documentation',
     'Maarten A. Breddels', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'glue-jupyter', 'glue-jupyter Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'glue-jupyter', 'glue-jupyter Documentation',
     author, 'glue-jupyter', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_cache_limit = 10     # days to keep the cached inventories
intersphinx_mapping = {
    # 'sphinx': ('https://www.sphinx-doc.org/en/latest/', None),
    'python': ('https://docs.python.org/3.11', None),
    # 'matplotlib': ('https://matplotlib.org', None),
    # 'numpy': ('https://docs.scipy.org/doc/numpy', None),
    # 'astropy': ('http://docs.astropy.org/en/stable/', None),
    'echo': ('https://echo.readthedocs.io/en/latest/', None),
    'ipywidgets': ('https://ipywidgets.readthedocs.io/en/stable/', None),
    'traitlets': ('https://traitlets.readthedocs.io/en/stable/', None),
    'glue': ('http://docs.glueviz.org/en/latest/', None),
}

default_role = 'obj'
nitpicky = True
nitpick_ignore = [('py:class', 'ipywidgets.widgets.widget_box.Box'),
                  ('py:class', 'ipywidgets.widgets.widget_box.VBox'),
                  ('py:class', 'ipywidgets.widgets.widget.Widget'),
                  ('py:class', 'ipywidgets.widgets.widget.LoggingHasTraits'),
                  ('py:class', 'ipywidgets.widgets.domwidget.DOMWidget'),
                  ('py:class', 'ipywidgets.widgets.widget_core.CoreWidget'),
                  ('py:class', 'ipyvuetify.VuetifyTemplate.VuetifyTemplate'),
                  ('py:class', 'traitlets.traitlets.HasTraits'),
                  ('py:class', 'traitlets.traitlets.HasDescriptors'),
                  ('py:class', 'echo.core.HasCallbackProperties'),
                  ('py:class', 'glue.viewers.image.layer_artist.ImageLayerArtist'),
                  ('py:class', 'glue.viewers.image.layer_artist.BaseImageLayerArtist'),
                  ('py:class', 'glue_vispy_viewers.volume.layer_state.VolumeLayerState'),
                  ('py:class', 'glue_vispy_viewers.common.layer_state.VispyLayerState')]

automodapi_inheritance_diagram = False
