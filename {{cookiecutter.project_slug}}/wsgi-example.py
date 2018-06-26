import sys

# Declare absolute path to project
path = '/path/to/project'

# Declare absolute path to configuration file
cfg_file = '/path/to/config.cfg'

if path not in sys.path:
    sys.path.append(path)

from {{cookiecutter.project_slug}} import create_app

# It's necessary have an object application
application = create_app(cfg_file=cfg_file)
