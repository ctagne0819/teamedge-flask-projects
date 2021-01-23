from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests

app = Flask(__name__)
json_info = ''
movies_path = os.path.join(app.static_folder, 'data', 'movies.json')
with open(movies_path, 'r') as raw_json:
    json_info = json.load(raw_json) 

@app.route('/')
def about():
    return '<p>Flask Server is running.</p>'

@app.route('/api/v1/albums', methods=['GET'])
def albums_json():
    albums_info = os.path.join(app.static_folder, 'data', 'albums.json')
    with open(albums_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info)

# @app.route('/api/v1/movies', methods=['GET'])
# def movies_json():
#     movies_info = os.path.join(app.static_folder, 'data', 'movies.json')
#     with open(movies_info, 'r') as json_data:
#         json_info = json.load(json_data)
#         return jsonify(json_info)

@app.route('/api/v1/movies')
def all_movies():
    return jsonify(json_info)

@app.route('/api/v1/movies/search_title', methods=['GET'])
def search_title():

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
