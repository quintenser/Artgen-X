from flask_restful import Resource
from ArtGenerator.art_generator import generate_art
import base64
import io


class ImageContainer(Resource):

    def __init__(self, id, base64String):
        """ImageModel constructor

        Args:
            imageId (int): image id
            imageString (string): image base64 string
        """
        self.imageId = id
        self.base64String = str(base64String)

    @classmethod
    def get_random_image(self):
        """Return a ImageModel containing a id and base64 string

        Return:
            ImageContainer
        """
        image, id = generate_art()
        in_memory = io.BytesIO()
        image.save(in_memory, format="PNG")
        return ImageContainer(id, base64.b64encode(in_memory.getvalue()))

    def json(self):
        """Return a JSON version of the current object

        Return:
            dict: the object
        """
        return self.__dict__
