from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests

@app.route('/')
def about():
    return '<p>Flask server is running.</p>'

@app.route('/nasa')
def nasa_image(): 
    today = str(date.today())
    response = requests.get