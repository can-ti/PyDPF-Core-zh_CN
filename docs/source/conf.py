from datetime import datetime
import os

import pyvista
import numpy as np
import sys 

from ansys.dpf.core import __version__


# Manage errors
pyvista.set_error_output_file('errors.txt')
# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True
# Preferred plotting style for documentation
# pyvista.set_plot_theme('document')
pyvista.rcParams['window_size'] = np.array([1024, 768]) * 2
# Save figures in specified directory
pyvista.FIGURE_PATH = os.path.join(os.path.abspath('./images/'), 'auto-generated/')
if not os.path.exists(pyvista.FIGURE_PATH):
    os.makedirs(pyvista.FIGURE_PATH)

pyvista.BUILDING_GALLERY = True


# -- Project information -----------------------------------------------------

project = 'PyANSYS DPF'
copyright = f'{datetime.now().year}, ANSYS'
author = 'ANSYS Developers'

# The short X.Y version
version = __version__

# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx_gallery.gen_gallery',
              'sphinx.ext.todo',
              'sphinx.ext.napoleon',
              'pydata_sphinx_theme',
              'nbsphinx',
]

autosummary_generate = True


# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Sphinx Gallery Options
from sphinx_gallery.sorting import FileNameSortKey

sphinx_gallery_conf = {
    # convert rst to md for ipynb
    'pypandoc': True,
    # path to your examples scripts
    "examples_dirs": ["../../examples/","../../examples_notebooks/" ],
    # path where to save gallery generated examples
    "gallery_dirs": ["examples"],
    # Patter to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": None,    
    "image_scrapers": ('pyvista', 'matplotlib'),
    # 'first_notebook_cell': ("%matplotlib inline\n"
    #                         "from pyvista import set_plot_theme\n"
    #                         "set_plot_theme('document')"),
}

autodoc_member_order = 'bysource'
# process_examples = True

# autoclass_content = 'both'
# autodata_content = 'call'

# import subprocess as spr
# spr.call([sys.executable] +
         # ('-m ipykernel install --user --name python3 '
          # '--display-name python3').split())
# spr.call([sys.executable, '-m', 'bash_kernel.install'])

# example_gallery_config = dict()


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = 'pydata_sphinx_theme'
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# zerovm-sphinx-theme

html_logo = '_static/pyansys-logo-black-cropped.png'


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "github_url": "https://github.com/pyansys/DPF-Core",
    # "show_toc_level": 1,
    # "show_prev_next": False
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/ansys.css']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_sidebars = {
    "testing": []
}



# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyansysdoc'


# -- Options for LaTeX output ------------------------------------------------

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
    (master_doc, 'pyansys.tex', 'PyAnsys DPF-Core Documentation',
     f'{author}', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pyansys', 'PyAnsys DPF-Core Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pyansys', 'PyAnsys DPF-Core Documentation',
     author, 'pyansys', '',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
