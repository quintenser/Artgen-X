from flask import request
import json
from FileModels.defaultConfig import DefaultConfig
from ImageDataClasses.image import Image
from ImageDataClasses.line import Line
from ImageDataClasses.square import Square
from ImageDataClasses.circle import Circle
from ImageDataClasses.triangle import Triangle


class FileManager():
    @classmethod
    def updateDefaultConfigFile(self, jsonData):
        """Update the default starting values with given data.

        Args:
            jsonData (dictonary): a file with json data

        Returns:
            bool : is data updated
        """
        config = DefaultConfig(jsonData['imageWidth'], jsonData['imageHeight'],
                               jsonData['circleAmount'], jsonData['squareAmount'], jsonData['lineAmount'], jsonData['triangleAmount'], jsonData['generations_until_algorithm_is_used'], jsonData['small_mutation_chance'], jsonData['big_mutation_chance'], jsonData['max_parents'])
        return self.writeJsonFile("defaultConfig", config.json())

    @classmethod
    def readDefaultConfig(self):
        """Read the default values

        Returns:
            DefaultConfig: class containing the default values
        """
        file = self.readJsonFile("defaultConfig")
        return DefaultConfig(file['imageWidth'], file['imageHeight'], file['circleAmount'], file['squareAmount'], file['lineAmount'], file['triangleAmount'], file['generations_until_algorithm_is_used'], file['small_mutation_chance'], file['big_mutation_chance'], file['max_parents'])

    @classmethod
    def readImageProperties(self, id):
        """Read the properties of the given image by id

        Args:
            id (int): the id of the image that needs te be read

        Returns:
            Image: class containing all the properties of a previous created image
        """
        file = self.readJsonFile(f"image_{id}_properties")

        # Create all Line objects
        lines = []
        for line in file['lines']:
            color = tuple(line['color'])
            vertices = line['vertices']
            positions = []
            for position in vertices:
                positions.append(tuple(position))
            lines.append(Line(positions, color))

        # Create all Square objects
        squares = []
        for square in file['squares']:
            color = tuple(square['color'])
            pos = tuple(square['position'])
            squares.append(Square(square['width'], square['height'], pos, color))

        # Create all Circle objects
        circles = []
        for circle in file['circles']:
            color = tuple(circle['color'])
            pos = tuple(circle['position'])
            circles.append(Circle(circle['width'], circle['height'], pos, color))

        # Create all Triangle objects
        triangles = []
        for triangle in file['triangles']:
            color = tuple(triangle['color'])
            pos = tuple(triangle['position'])
            triangles.append(Triangle(triangle['width'], triangle['height'], pos, color))

        # Load the background color
        background_color = tuple(file['background_color'])
        return Image(file['imageWidth'], file['imageHeight'], background_color, lines, squares, circles, triangles)

    @classmethod
    def writeJsonFile(self, fileName, jsonData):
        """Write a file with given json data

        Args:
            fileName (string): file name
            jsonData (dictonary): json data

        Returns:
            bool: is writing the json successfull
        """
        with open(f'{fileName}.json', 'w') as f:
            json.dump(jsonData, f)
        return True

    @classmethod
    def readJsonFile(self, fileName):
        """Read json file by name

        Args:
            fileName (string): name of the file

        Returns:
            dictonary: dictonary with the data
        """
        with open(f'{fileName}.json') as f:
            return json.load(f)
