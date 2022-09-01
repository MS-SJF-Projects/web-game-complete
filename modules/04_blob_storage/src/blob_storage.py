import random
from socket import timeout
from typing import Optional
import os, pickle
from azure.storage.blob import BlobServiceClient, __version__


class BlobStorage:
    """
        Blob store to store secret words.
    """

    def __init__(self):
        connection_string = os.environ.get('AZURE_STORAGE_CONNECTION_STRING', '')
        print("connection string", connection_string)
        self.client = BlobServiceClient.from_connection_string(connection_string)
        print("client", self.client)
        self.container_client = self.client.get_container_client('secret-words')
        print("container client", self.container_client)
        try:
            print("try to get blob")
            self.container_client.create_container(timeout=5)
        except Exception as exp:
            print("Exception: {}".format(exp))
        try:
            self.blob_client = self.container_client.get_blob_client('secret-words')
            self.storage = pickle.loads(self.blob_client.download_blob().readall())
        except Exception as exp:
            print("Exception: {}".format(exp))
            self.storage = []
        
    def add_word(self, secret_word: str) -> None:
        """ Store a secret word."""
        self.storage.append(secret_word)
        # save it in blob storage
        self.blob_client.upload_blob(pickle.dumps(self.storage), overwrite = True)

    def get_all_words(self) -> list[str]:
        """ Get all words saved so far. """
        return self.storage

    def get_random_word_index(self) -> Optional[int]:
        """ Get an index of a random secret word."""
        if len(self.storage) == 0:
            return None  # no words in storage - nothing to return
        return random.randint(0, len(self.storage) - 1)

    def get_word_by_index(self, index: int) -> Optional[str]:
        """
        Given the index in the storage, return the secret word by this index.
        """
        if not (0 <= index < len(self.storage)):
            return None  # index out of range - nothing to return
        return self.storage[index]

    def delete_word(self, secret_word: str) -> None:
        """ Delete a secret word from the storage."""
        self.storage.remove(secret_word)
        # save it in blob storage
        self.blob_client.upload_blob(pickle.dumps(self.storage), overwrite = True)