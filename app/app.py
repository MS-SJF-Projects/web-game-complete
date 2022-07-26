from flask import Flask, Response, flash, render_template, request, redirect, session
import os
from .inmemory_image_store import InMemoryImageStore

app_version = '0.0.1'

app = Flask(__name__)
app.secret_key = "f3cfe9ed8fae309f02079dbf"
app.image_store = InMemoryImageStore()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/guess')
def guess():
    img_id = app.image_store.get_random_id()
    if img_id is None:
        flash("no images uploaded yet")
        return redirect("/")

    session['selection'] = img_id

    return render_template('guess.html')

@app.route('/guess_image_display')
def guess_image():
    (content_type, img_bytes), session['secret'] = app.image_store.get_image_by_id(session['selection'])
    return Response(img_bytes, mimetype=content_type)

@app.route('/result_guess', methods = ['POST'])
def result_guess():
    result = request.form
    return render_template('result_guess.html', result  = result)

def secure_filename(path):
    return path.replace("/","_").replace(".","_").replace("\\","_").replace(" ","_")

@app.route('/upload_image', methods = ['GET','POST'])
def upload_image():
    result = request.form

    if request.method == "GET":
        return render_template('upload_image.html', result = result)


    file = request.files['image']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected files')
        return redirect(request.url)
    app.image_store.store_image((file.content_type, file.stream.read()), request.form['secret'])
    flash("file uploaded with a secret " + request.form['secret'])
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run(debug = True)