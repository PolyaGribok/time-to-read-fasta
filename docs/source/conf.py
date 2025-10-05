import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'FASTA Reader'
copyright = '2025, Polya Gribok'
author = 'Polya Gribok'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

master_doc = 'index'
todo_include_todos = True