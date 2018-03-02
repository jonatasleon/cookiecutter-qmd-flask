import pytest
from {{cookiecutter.project_core_dir}} import create_app


@pytest.fixture
def app():
    return create_app()
