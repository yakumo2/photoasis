from flask import Flask, render_template, abort, request, redirect, url_for, jsonify, Blueprint
import os
import json
import re
import folder_action
import global_variables

index_bp = Blueprint('index_bp', __name__)

# Route for index page
@index_bp.route('/')
def index():
	print("index executed")
	#albums = get_albums()
	albums = folder_action.get_sorted_folders()
	filtered_albums = [album for album in albums if album.get('display', True)]
	return render_template('index.html', albums=filtered_albums, path=global_variables.path)

# Helper function to get list of albums
'''
def get_albums():
    import os
    albums = []
    for root, dirs, files in os.walk('photo'):
        albums.extend(dirs)
        break  # only top-level directories
    print("get list of albums")
    return albums
'''
