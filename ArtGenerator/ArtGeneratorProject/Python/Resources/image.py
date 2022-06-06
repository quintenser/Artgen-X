import json
from flask_restful import Resource
from Containers.image import ImageContainer
from ArtGenerator.art_generator import add_image_to_parents


class Image(Resource):

    def get(self):
        """Return a generated image base64 string

        Return:
            dict: image base64 string
        """

        image = ImageContainer.get_random_image()
        return image.json(), 200

    def post(self, id):
        image, generation_id = add_image_to_parents(id)
        return {'canvasData': json.dumps(image.json()), 'id': generation_id}, 200
