from flask import Flask, render_template

app = Flask(__name__)

APP_VERSION = '0.0.1'


@app.context_processor
def inject_app_version():
    return dict(app_version=APP_VERSION)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/home_without_base')
def home_without_base():
    return render_template('home_without_base.html')


@app.route('/guess')
def guess():
    return render_template('guess.html')


@app.route('/upload_image')
def upload_image():
    return render_template('upload_image.html', app_version=APP_VERSION)
