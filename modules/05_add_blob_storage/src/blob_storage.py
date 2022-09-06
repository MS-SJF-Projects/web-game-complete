import os
import uuid
from azure.storage.blob import BlobServiceClient
import logging

logging.getLogger('azure').setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

class BlobStorage:
    """
        Blob store to store secret words.
    """

    def __init__(self):
        connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING', '')
        self.client = BlobServiceClient.from_connection_string(connection_string)
        container_name = 'images-to-guess'
        self.container_client = self.client.get_container_client(container_name)
        try:
            self.container_client.create_container(timeout=1000)
        except Exception as exp: # pylint: disable=broad-except
            print("Exception trying to create container {}".format(exp))

    def upload_image(self, image_bytes) -> str:
        """Store an image in a blob and returns the name of the blob"""
        try:
            blob_name = str(uuid.uuid4()) + ".jpg"
            blob_client = self.container_client.get_blob_client(blob_name)
            blob_client.upload_blob(image_bytes)
        except Exception as exp:
            print("Exception trying to create blob {}".format(exp))
            raise
        return blob_name    

    def download_image(self, blob_name) -> bytes:
        """Download an image from a blob returning the content"""
        try:
            return self.container_client.download_blob(blob_name).readall()
        except Exception as exp:
            print("Exception trying to download blob {}".format(exp))
            raise
