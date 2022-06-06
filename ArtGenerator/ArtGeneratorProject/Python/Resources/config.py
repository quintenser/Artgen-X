from flask import request
from flask_restful import Resource
from fileManager import FileManager


class Config(Resource):

    def post(self):
        """Update the config of the art generator

        Return:
            status
        """

        jsonData = request.json
        if FileManager.updateDefaultConfigFile(jsonData):
            return {"configStatus": "Success"}, 200
        else:
            return {"configStatus": "Failed"}, 500
