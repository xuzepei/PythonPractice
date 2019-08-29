
#sudo pip install Pillow

#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from array import *
import json
import os

def showBuckets():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)


def openBucket():
    # Imports the Google Cloud client library
    from google.cloud import storage

    # Instantiates a client
    storage_client = storage.Client()

    # The name for the new bucket
    bucket_name = 'color0001-a80ed.appspot.com'

    # get bucket
    try:
        bucket = storage_client.get_bucket(bucket_name)
    except google.cloud.exceptions.NoFound:
        print("Sorry, that bucket does not exist!")

    print(bucket)

    """Uploads a file to the bucket."""
    
    source_file_name = "aaaaa.json"
    destination_blob_name = "ios/test/" + source_file_name

    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
            source_file_name,
            destination_blob_name))


openBucket()




