#
# class aws_tests:
#
#     def test_upload_to_s3(self):
#         result = upload_to_s3(LOCAL_FILE_PATH, AWS_BUCKET_NAME, S3_FILE_KEY, AWS_REGION)
#
#         # Check if the upload was successful
#         assert result == True
#
#     def test_download_from_s3(self):
#         # Perform the download
#         result = download_from_s3(AWS_BUCKET_NAME, S3_FILE_KEY, LOCAL_FILE_PATH, AWS_REGION)
#
#         # Check if the download was successful
#         assert result == True
#
#     def test_delete_from_s3(self):
#         # Perform the delete
#         result = delete_from_s3(AWS_BUCKET_NAME, S3_FILE_KEY, AWS_REGION)
#
#         # Check if the delete was successful
#         assert result == True