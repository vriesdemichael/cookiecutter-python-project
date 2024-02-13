import pytest
from {{ cookiecutter.package_folder_name }}.example import example_var_for_tests

@pytest.fixture()
def example_fixture():
    return example_var_for_tests