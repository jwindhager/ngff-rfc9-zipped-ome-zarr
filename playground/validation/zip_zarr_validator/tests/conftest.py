import pytest


def pytest_addoption(parser):
    parser.addoption("--uri", action="store")

@pytest.fixture(scope='class')
def uri(request):
    return request.config.option.uri
