# test_sample.py

import pytest

@pytest.fixture(scope='session')
def setup():
    print('\n setting up, creating bucket**********')


def test_method_one(setup):
    print("\n This is test method one@@")

def test_method_two(setup):
    print("\n This is test method two@@@")
