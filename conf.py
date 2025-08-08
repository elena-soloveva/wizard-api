# Configuration file for
# Wizard API
# build with Sphinx

import os
import sys
import time
import subprocess

# ==============================================================================
# Path setup
# ==============================================================================

# Add project-specific directories to sys.path
sys.path.insert(0, os.path.abspath('source/'))
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

# ==============================================================================
# General configuration
# ==============================================================================

# List of enabled Sphinx extensions
extensions = [
  'hoverxref.extension',
  'myst_parser',
  'sphinx_design',
  'sphinx.ext.duration',
  'sphinx.ext.autodoc',
  'sphinx.ext.autosectionlabel',
  'sphinx.ext.autosummary',
  'sphinx.ext.intersphinx',
  'sphinx.ext.viewcode',
  'sphinx_markdown_tables',
  'versionwarning.extension',
  'sphinx_copybutton',
  'sphinxcontrib.video',
]

# ==============================================================================
# MyST parser configuration
# ==============================================================================

# List of enabled MyST extensions
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Maximum heading level for generating anchor links (H1 to H7)
myst_heading_anchors = 7

# ==============================================================================
# autosectionlabel configuration
# ==============================================================================

# Prefix section labels with the document name to avoid label conflicts
autosectionlabel_prefix_document = True

# Maximum depth of section headers to automatically label (None = unlimited)
autosectionlabel_maxdepth = None

# ==============================================================================
# hoverxref configuration
# ==============================================================================

# Enable tooltips for glossary terms and other inline roles
hoverxref_roles = ['term']

# ==============================================================================
# Warning and error handling
# ==============================================================================

# Suppress duplicate label warnings
suppress_warnings = ['autosectionlabel.*']

# ==============================================================================
# Templates and sources
# ==============================================================================

# Paths to custom templates
templates_path = ['_templates']

# Supported source file extensions
source_suffix = ['.rst', '.md']

# Root document name
master_doc = 'index'

# Patterns to exclude from source scanning
exclude_patterns = []

# ==============================================================================
# Project information
# ==============================================================================

project = u'Wizard API Documentation'
copyright = 'Gaijin Entertainment %s' % time.strftime('%Y')
author = u'Gaijin Entertainment'
version = u'0.1.0'

# ==============================================================================
# Language and localization
# ==============================================================================

language = 'en'

# ==============================================================================
# Output and formatting configuration
# ==============================================================================

# Pygments style for syntax highlighting
pygments_style = 'sphinx'

# Include TODO and todoList entries in output
todo_include_todos = True

# Optional: formatting and indexing behavior
# today = ''
# today_fmt = '%B %d, %Y'
# source_encoding = 'utf-8-sig'
# default_role = None
# add_function_parentheses = True
# add_module_names = True
# show_authors = False
# modindex_common_prefix = []
# keep_warnings = False

# ==============================================================================
# Build timer
# ==============================================================================

# Adds timing info: prints build duration in seconds on finish
def setup(app):
    start_time = time.time()

    def report_build_time(app, exception):
        duration = time.time() - start_time
        print(f"\nBuild finished in {duration:.2f} seconds.")

    app.connect('build-finished', report_build_time)

# ==============================================================================
# HTML output configuration
# ==============================================================================

# Theme to use for HTML and HTML Help pages
html_theme = 'sphinx_rtd_theme'

# Theme-specific customization options
html_theme_options = {
    'navigation_depth': -1,
}

# HTML title (defaults to "<project> v<release> documentation")
html_title = ''

# Logo image shown at the top of the sidebar
html_logo = '_static/_images/logo.png'

# Favicon image for the docs (should be .ico, 16x16 or 32x32 px)
html_favicon = '_static/_images/favicon.ico'

# Paths with custom static files (CSS, images, etc.)
html_static_path = ['_static']

# Additional CSS files to include
html_css_files = [
    'custom.css',
]

# Format for 'Last updated on:' timestamp on each page
html_last_updated_fmt = '%b %d, %Y'

# Show "Created using Sphinx" footer. Default: True
html_show_sphinx = False

# Base name for HTML help builder output files
htmlhelp_basename = 'wizard_api_docs'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# Extra files copied to root (e.g. robots.txt)
#html_extra_path = []

# Enable SmartyPants for typographic quotes and dashes
# html_use_smartypants = True

# Custom sidebar templates
# html_sidebars = {}

# Additional pages rendered from templates
# html_additional_pages = {}

# Generate module index. Default: True
# html_domain_indices = True

# Generate general index. Default: True
# html_use_index = True

# Split index into pages per letter. Default: False
# html_split_index = False

# Show links to source files on pages. Default: True
# html_show_sourcelink = True

# Show copyright info in footer. Default: True
# html_show_copyright = True

# Enable OpenSearch description file (provide base URL)
# html_use_opensearch = ''

# File suffix for HTML files. Default: None
# html_file_suffix = None

# Language for HTML search index. Default: 'en'
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# ==============================================================================
# LaTeX output configuration
# ==============================================================================

# Use XeLaTeX engine for better Unicode and font support
latex_engine = 'xelatex'

# Define the document parameters
latex_title = 'Wizard API Documentation'  # Document title
latex_documents = [(
    'index',                # Root source file
    'wizard-api-docs.tex',         # Output .tex filename
    'latex_title',          # Title
    'Gaijin Entertainment', # Author
    'manual',               # Document type: 'manual' = book-style with chapters
    )]

# General parameters
latex_logo = '_static/_images/logo.png' # Logo to display on the title page of the PDF

latex_elements = {
    'pointsize': '10pt',         # Default font size
    'papersize': 'a4paper',      # Default paper size
    'maxlistdepth': '20',        # Number of nested levels
    'figure_align': 'H',         # Default figure alignment
    'tocdepth': '2',             # TOC depth

    'preamble': r'''
    \setcounter{secnumdepth}{2}
    \setcounter{tocdepth}{2}
    \usepackage{graphicx}
    \usepackage[svgnames]{xcolor}
    \definecolor{darkbgr}{rgb}{0.102, 0.110, 0.118}
    \definecolor{mdarkbgr}{rgb}{0.204, 0.192, 0.192}
    \usepackage{hyperref}
    \hypersetup{
      colorlinks=true,
      linkcolor=DarkBlue,
      filecolor=DarkBlue,
      urlcolor=DarkBlue,
    }
    \usepackage{tikz}
    \usetikzlibrary{shadows}
    \newcommand{\cnum}[1]{%
      \tikz[baseline=-0.6ex]{
        \node[
          shape=circle,
          draw=none,
          fill=yellow,
          text=black,
          minimum size=1.3em,
          inner sep=0pt,
          text centered,
          drop shadow={shadow xshift=1pt, shadow yshift=-1pt, opacity=0.3}
        ] (char) {\scalebox{0.9}{\textbf{#1}}};
      }%
    }
    ''',

    'fontpkg': r'''
    \setmainfont{FreeSans}
    \setsansfont{FreeSans}
    \setmonofont{FreeMono}
    ''',

    # Title page
    'maketitle': r'''
    \begin{titlepage}
    \begin{tikzpicture}[remember picture, overlay, shift={(current page.south west)}]
    \fill[mdarkbgr] (0,0) rectangle (5cm,\paperheight);
    \end{tikzpicture}
    \begin{tikzpicture}[remember picture, overlay, shift={(current page.south west)}]
    \fill[darkbgr] (0,\paperheight - 10cm) rectangle (\paperwidth, \paperheight - 5cm);
    \node[anchor=south east, font=\bfseries\Huge, text=white] at (\paperwidth - 1cm, \paperheight - 8cm) {Wizard API Documentation};
    \node[anchor=south east, font=\bfseries\large, text=darkbgr] at (\paperwidth - 1cm, \paperheight - 11.5cm) {Gaijin Entertainment};
    \node[anchor=north west] at (0.8cm, \paperheight - 5.3cm) {\includegraphics[width=3cm]{logo}};
    \end{tikzpicture}
    \end{titlepage}
    ''',
}

# ==============================================================================
# Manual page output configuration
# ==============================================================================

# One entry per manual page.
# Format: (source start file, name, description, authors, manual section).
# Used when building Unix man pages via `sphinx-build -b man`.
man_pages = [
    (master_doc, 'Wizard API Docs', u'Wizard API Documentation',
    [author], 1)
]

# If true, show raw URL addresses after external links (not usually needed).
# man_show_urls = False

# ==============================================================================
# Texinfo output configuration
# ==============================================================================

# Configuration for Texinfo output (used for GNU info manuals).
# Format: (start file, target name, title, author, menu entry, description, category).
texinfo_documents = [
    (master_doc, 'Wizard API Docs', u'Wizard API Docs',
     author, 'Wizard API', 'Modules and Libraries', 'Manuals',
     'Miscellaneous'),
]

# Append additional documents as appendices to all Texinfo manuals.
# texinfo_appendices = []

# If false, no module index is generated in the output.
# texinfo_domain_indices = True

# How to display URLs: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, suppress the creation of the @detailmenu in the top node.
# texinfo_no_detailmenu = False

# ==============================================================================
# Reserved setup hook (currently unused)
# ==============================================================================

# This setup function can be used to customize the Sphinx app initialization,
# e.g., to set the source directory or add custom CSS files directly.
# At the moment, it is commented out because these settings are handled elsewhere.
# Uncomment and adjust if needed for advanced customization.

# def setup(app):
#    # Add custom CSS file to all HTML pages
#    app.add_css_file('custom.css')

# ==============================================================================
# Inline syntax highlighting roles (rst_prolog)
# ==============================================================================

# Defines global inline roles for syntax highlighting in reStructuredText.
# These can be used as :cpp:`std::vector` or :sq:`foo()` inside the text.
rst_prolog = """
.. role:: sq(code)
   :language: sq

.. role:: cpp(code)
   :language: cpp
"""

# ==============================================================================
# Custom inline roles
# ==============================================================================

from docutils import nodes
from docutils.parsers.rst import roles

# ------------------------------------------------------------------------------
# Role `:cnum:` for formatting numbers differently depending on output builder
#
# - In LaTeX output (e.g., PDF), wraps the number in a custom LaTeX command \cnum{...}
# - In HTML output, wraps the number in a <span> with class "cnum"
#
# Usage examples:
#   :cnum:`42` in reStructuredText
#   {cnum}`42` in MyST Markdown
#
# This allows consistent styling or formatting of numeric values across formats.
# ------------------------------------------------------------------------------
def cnum_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    builder = inliner.document.settings.env.app.builder.name

    if builder == 'latex':
        # LaTeX: use \cnum{...}
        latex = rf'\cnum{{{text}}}'
        node = nodes.raw('', latex, format='latex')
    else:
        # HTML: use <span class="cnum">...</span>
        node = nodes.inline(text, text, classes=['cnum'])

    return [node], []

roles.register_local_role('cnum', cnum_role)

# ------------------------------------------------------------------------------
# Factory function to create badge roles
#
# These roles render colored inline badges in HTML output.
# Usage example in Markdown/RST:
#   {bdg-red}`ERROR`
#   :bdg-green:`SUCCESS`
#
# Each badge wraps text in a <span> with CSS classes for color styling.
# ------------------------------------------------------------------------------
def make_bdg_role(color_class):
    def bdg_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        builder = inliner.document.settings.env.app.builder.name

        node = nodes.inline(text, text, classes=['bdg', color_class])

        return [node], []
    return bdg_role

bdg_colors = {
    'bdg-blue': 'bdg-blue',
    'bdg-green': 'bdg-green',
    'bdg-grey': 'bdg-grey',
    'bdg-orange': 'bdg-orange',
    'bdg-purple': 'bdg-purple',
    'bdg-red': 'bdg-red',
    'bdg-yellow': 'bdg-yellow',
}

for role_name, css_class in bdg_colors.items():
    roles.register_local_role(role_name, make_bdg_role(css_class))

