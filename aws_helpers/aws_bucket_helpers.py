import boto3
import time


def create_bucket(bucket_name, region='us-east-1'):
    s3 = boto3.client('s3', region_name=region)
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully in region '{region}'")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def upload_file_to_bucket(bucket_name, file_path, object_key):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, object_key)
        print(f"File '{file_path}' uploaded to '{bucket_name}' with key '{object_key}'")
    except Exception as e:
        print(f"Error uploading file: {e}")


def delete_file(bucket_name, object_key):
    s3 = boto3.client('s3')

    try:
        s3.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"File with key '{object_key}' deleted from '{bucket_name}'")
    except Exception as e:
        print(f"Error deleting file: {e}")


def delete_bucket(bucket_name):
    s3 = boto3.client('s3')

    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully")
    except Exception as e:
        print(f"Error deleting bucket: {e}")

def check_upload_performance(bucket_name, file_path, object_key, region='us-east-1'):
    s3 = boto3.client('s3', region_name=region)

    start_time = time.time()
    upload_file_to_bucket(bucket_name, file_path, object_key)
    end_time = time.time()

    upload_time = end_time - start_time
    print(f"Upload time: {upload_time:.2f} seconds")


def delete_bucket(bucket_name, region='us-east-1'):
    try:
        # Create an S3 client
        s3 = boto3.client('s3', region_name=region)

        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)

        print(f"Bucket '{bucket_name}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
# delete_bucket('your_bucket_name', region='your_region')


def delete_bucket_new(bucket_name, region='us-east-1'):
    try:
        s3 = boto3.client('s3', region_name=region)
        objects = s3.list_objects_v2(Bucket=bucket_name)['Contents']

        # Delete each object in the bucket
        for obj in objects:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)

        print(f"Bucket '{bucket_name}' and its contents deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
# delete_bucket_with_data('your_bucket_name', region='your_region')


# Example usage:
# delete_bucket('your_bucket_name', region='your_region')


bucket_name = 'bucketzjj'
create_bucket(bucket_name, 'us-east-1')
time.sleep(50)
upload_file_to_bucket(bucket_name, '/Users/apple/PycharmProjects/storage_automated_tests/sample_files/small_file.txt', 'small_file.txt')
time.sleep(40)
delete_file(bucket_name, 'small_file.txt')
check_upload_performance(bucket_name, 'file_to_upload_s3.txt', 'file_to_upload_s3.txt')
# delete_bucket('my-s3-bucket')

delete_bucket_new(bucket_name, 'us-east-1')



