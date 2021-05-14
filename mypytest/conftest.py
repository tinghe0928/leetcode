import pytest
def pytest_configure(config):
    config.addinivalue_line("markers", "hello: This is just for hello")

@pytest.fixture(scope='module')
def print_line():
    print("this is print")
    yield
    print("this is end ! ")
