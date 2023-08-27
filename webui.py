from flask import Flask, request, render_template, url_for
import os

from thumb import thumb
from json import load

app = Flask(__name__)

app.config['IMG_FOLDER'] = os.path.join('static','images')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    image_name = request.args.get('_fragment')
    print(image_name)
    return render_template("gallery.html",images=os.walk(app.config['IMG_FOLDER']),thumb=thumb)

app.run('0.0.0.0',port=5890,debug=True)