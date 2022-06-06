import os
from flask import Flask
from flask_restful import Api
from Resources.image import Image
from Resources.config import Config
from ArtGenerator.art_generator import reset_generation

app = Flask(__name__)
# Create a new API
api = Api(app, prefix=os.getenv("API_PREFIX"))


@app.route('/')
def index():
    return "<h1>SDL Art Generator</h1>", 200


@app.route('/api/status')
def status():
    return "active", 200


@app.route('/api/reset')
def reset():
    return f'Art generator reset = {reset_generation()}', 200


api.add_resource(Image, *["/<int:id>/image", "/image"])
api.add_resource(Config, "/config")

if __name__ == "__main__":
    app.run(debug=True)
