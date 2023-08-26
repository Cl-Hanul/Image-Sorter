from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

app.config['IMG_FOLDER'] = os.path.join('static','images')

@app.route('/')
def index():
    return render_template('YOUR INDEX HTML FILES')

@app.route('/gallery')
def gallery():
    return render_template("gallery.html",images=os.walk(app.config['IMG_FOLDER']))

app.run('0.0.0.0',port=5890,debug=True)