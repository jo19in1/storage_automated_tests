import pytest
from aws_helpers.aws_bucket_helpers import create_bucket, upload_file_to_bucket
from helpers.general_helpers import create_random_name, create_custom_file


@pytest.fixture()
def setup():
    print('setting up, creating bucket')
    #create a bucket name that is unique to honor aws bucket name policy
    #then create a bucket
    create_bucket(create_random_name('bucket'))


def test_upload_file_to_bucket():
    print('test test_upload_file_to_bucket')

    # upload_file_to_bucket()
    # create_custom_file('filler.txt', 20)


def test_aaa():
    print('test two')


def test_three():
    print('test three')



@pytest.fixture()
def teardown():
    print('ending all tests')
