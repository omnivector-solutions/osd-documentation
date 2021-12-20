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
    'sphinxcontrib.spelling',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', 'venv']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'rainbow_dash'


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

# spell checker configurations
spelling_lang = 'en_us'
spelling_show_suggestions = True
spelling_word_list_filename = 'new_words_spell_checker.txt'
spelling_exclude_patterns = ['changelog.rst']


# -- Preprocessing steps -----------------------------------------------------
import shutil
shutil.copyfile('../slurm-charms/CHANGELOG', 'changelog.rst')


# generate page for configurations and actions for all charms
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates"))
descripts = {"slurmd": "The Slurm compute node.",
             "slurmdbd": "The Slurm database node.",
             "slurmctld": "The central management charm.",
             "slurmrestd": "Interface to Slurm via a REST API."}

def parse_description(description: str):
    """Parse action/config description to translate to rst.

    Add paragraph breaks, translate "notes" and "examples" to rst syntax."""

    description = description.replace('\n', '\n\n')
    description = description.replace('Note: ', '.. note::\n\n   ')

    example_str = 'Example Usage:\n\n.. code-block:: bash\n\n   '
    description = description.replace('Example usage: ', example_str)

    # rst code blocks have two backticks
    description = description.replace('`', '``')

    return description

def parse_config(configs: dict):
    for config in configs['options']:
        descript = configs['options'][config]['description']
        if descript:
            configs['options'][config]['description'] = parse_description(descript)

    return configs

def parse_action(actions: dict):
    for action in actions:
        # action description
        descript = actions[action]['description']
        if descript:
            actions[action]['description'] = parse_description(descript)

        # parameters descriptions
        if actions[action].get('params'):
            for param in actions[action]['params']:
                descript = actions[action]['params'][param]['description']
                descript = parse_description(descript)
                actions[action]['params'][param]['description'] = descript

    return actions

for charm in descripts.keys():
    data = dict()
    data["charm"] = charm
    data["charm_description"] = descripts[charm]

    config_file = Path(f'../slurm-charms/charm-{charm}/config.yaml')
    if config_file.exists():
        configs = yaml.safe_load(config_file.read_text())
        data.update(parse_config(configs))

    action_file = Path(f'../slurm-charms/charm-{charm}/actions.yaml')
    if action_file.exists():
        actions = parse_action(yaml.safe_load(action_file.read_text()))
        data.update({'actions': actions})

    template = environment.get_template("configs_and_actions.tmpl")
    Path(f"configuration/{charm}.rst").write_text(template.render(data))
