
#sudo pip install Pillow

#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from array import *
import json
import os
from google.cloud import storage, exceptions
import sys
import argparse
import oss2


def showBuckets():
    
    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

# Upload file to Firebase Storage
def uploadFileToFirebaseStorage(filename):
    
    print(">>>>>>>>>uploadFile to FirebaseStorage: ", filename)

    # Instantiates a client
    storage_client = storage.Client()

    # The name for the new bucket
    bucket_name = 'color0001-a80ed.appspot.com'

    # get bucket
    try:
        bucket = storage_client.get_bucket(bucket_name)
    except exceptions.NotFound:
        print(">>>>>>>>>Exceptions: that bucket is not found!")
        return
    
    if _MODE == 'test':
        destination_blob_name = "ios/test/" + filename
    elif _MODE == 'pro':
        destination_blob_name = "ios/" + filename

    print(">>>>>>>>>Will upload file to " + destination_blob_name)
    #return


    blob = bucket.blob(destination_blob_name)
    # try:
    #     blob.delete()
    # except exceptions.NotFound:
    #     print(">>>>>>>>>Exceptions: that blob is not found!")

    try:
        blob.upload_from_filename(filename)
    except:
        print(">>>>>>>>>Exceptions: uploading " + filename + " failed!")
        return

    print('>>>>>>>>>File {} uploaded to {}.'.format(
            filename,
            destination_blob_name))

# Upload file to Aliyun OSS
def uploadFileToAliyun(filename):
    
    print(">>>>>>>>>uploadFile to Aliyun: ", filename)

    # get auth
    auth = oss2.Auth('', '')

    # get bucket
    try:
        bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', 'color0001')
    except:
        print(">>>>>>>>>Exceptions: that bucket is not found!")
        return

    if _MODE == 'test':
        destination_blob_name = "ios/test/" + filename
    elif _MODE == 'pro':
        destination_blob_name = "ios/" + filename

    #delete file
    # try:
    #     bucket.delete_object("ios/test/aaaaa.json")
    # except:
    #     print(">>>>>>>>>Exceptions: Deleting file failed!")

    print(">>>>>>>>>Will upload file to " + destination_blob_name)
    #return

    filepath = os.path.abspath(filename)
    #print(">>>>>>>>>filepath " + filepath)

    # <yourLocalFile>由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt
    try:
        bucket.put_object_from_file(destination_blob_name, filepath)
    except:
        print(">>>>>>>>>Exceptions: uploading " + filename + " failed!")
        return

    print('>>>>>>>>>File {} uploaded to {}.'.format(
            filename,
            destination_blob_name))

# Read json file
def readConfig(filename):
    with open(filename) as configFile:

        data = json.load(configFile)
        items = data['all']

        index = 0
        for item in items:
            name = item["name"]

            if len(name) > 0:
                zip_filename = name + '.zip'
                if os.path.exists(zip_filename):
                    uploadFileToFirebaseStorage(zip_filename)
                    uploadFileToAliyun(zip_filename)
                else:
                    print("The file does not exist: " + zip_filename)

            index = index + 1

            if index >= 5:
                break

    uploadFileToFirebaseStorage(filename)
    uploadFileToAliyun(filename)


_MODE = 'test'
_CONFIG_FILENAME = 'items.json'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(usage="It's a tip.", description="help info.")
    parser.add_argument("-m", "--mode", choices=['test', 'pro'], default="test", help="Input mode, test or production")
    #parser.add_argument("-mode", type=string, required=True, help="Input ")
    #parser.add_argument("-l", "--log", default=False, action="store_true", help="active log info.")
 
    args = parser.parse_args()
    print(">>>>>>>>>upload.py --mode {0}".format(args.mode))
    _MODE = args.mode
    readConfig(_CONFIG_FILENAME)



