from flask import Flask, render_template, abort, request, redirect, url_for, jsonify, Blueprint
import os
import json
import re
from admin import admin_bp
from index import index_bp
from album import album_bp
import global_variables
import secrets

app = Flask(__name__, static_folder='photo')
app.secret_key = secrets.token_hex(16)

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(album_bp, url_prefix='/album')
app.register_blueprint(index_bp)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=16001)


