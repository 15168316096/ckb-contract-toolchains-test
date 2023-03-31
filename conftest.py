import pytest


@pytest.fixture(scope="session")
def setup():
    pass


@pytest.fixture(scope="function")
def teardown():
    pass
