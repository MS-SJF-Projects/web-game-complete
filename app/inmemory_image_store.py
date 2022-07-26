import random

class InMemoryImageStore:
    """
        InMemory store to store images.
    """
    images = []

    def store_image(self, image_content: bytes, image_description: str):
        """ Store an image and description."""
        self.images.append((image_content, image_description))

    def get_random_id(self):
        """ Get a random image."""
        return random.randint(0, len(self.images) - 1) if self.images else None

    def get_image_by_id(self, id):
        return self.images[id]