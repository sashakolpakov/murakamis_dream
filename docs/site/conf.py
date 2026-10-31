"""Sphinx reading companion for the authored long-twist manuscript."""
project = 'Long-twist volume limits'
author = ''
copyright = '2026'
extensions = ['sphinx.ext.mathjax']
root_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ['manuscript.css']
html_title = 'Long-twist volume limits — manuscript companion'
html_theme_options = {'description': 'Exact sources, geometry, and full filling periods', 'fixed_sidebar': False,
                      'page_width': '1120px', 'sidebar_width': '240px'}
html_sidebars = {'**': ['about.html', 'navigation.html', 'searchbox.html']}
html_show_sourcelink = True
html_show_sphinx = True
mathjax3_config = {'tex': {'macros': {'Vol': r'\operatorname{Vol}'}}}
