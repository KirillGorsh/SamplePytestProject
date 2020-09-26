import pytest


@pytest.fixture(scope='session')
def my_cool_fixture():
    print("********* This is the fixture to run first *********")
    yield my_cool_fixture
    print("********* This is the TEARDOWN steps after each of your scope *******************")