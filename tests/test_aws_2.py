import pytest
from aws_helpers.aws_bucket_helpers import create_bucket, upload_file_to_bucket
from helpers.general_helpers import create_random_name, create_custom_file

@pytest.fixture(scope='module')
def setup():
    print('setting up, creating bucket')
    # create a bucket name that is unique to honor AWS bucket name policy
    # then create a bucket
    # bucket_name = create_random_name('bucket')
    # create_bucket(bucket_name)
    # yield bucket_name  # Provide the bucket name as a fixture value
    # # Teardown code can be added here if necessary


def test_upload_file_to_bucket(setup):
    print('test test_upload_file_to_bucket')
    # Use the fixture value returned from setup fixture
    bucket_name = setup
    # Add your test logic here


def test_aaa(setup):
    print('test two')
    # Use the fixture value returned from setup fixture
    bucket_name = setup
    # Add your test logic here


def test_three(setup):
    print('test three')
    # Use the fixture value returned from setup fixture
    bucket_name = setup
    # Add your test logic here


@pytest.fixture(scope='module')
def teardown():
    print('ending all tests')
    # Teardown code can be added here if necessary
