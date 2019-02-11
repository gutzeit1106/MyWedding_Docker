import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import glob
import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images/upload/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif','jpeg','heic'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def route():
    return render_template('index.html') 

@app.route("/index")
def index():
    return render_template('index.html', title='Welcome to Our Wedding') 

@app.route("/about")
def about():
    return render_template('about.html', title='Story') 

@app.route("/gallery")
def gallery():
    img_list = sorted(glob.glob("./static/images/upload/*"))
    imgs = sorted(os.listdir("./static/images/upload/"))
    print(imgs)
    return render_template('gallery.html', title='Gallery', galleryImages=img_list,imgs=imgs) 

@app.route("/upload")
def upload():
    print(img_list)
    return render_template('upload.html') 

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        img_file = request.files['img_file']
        if img_file and allowed_file(img_file.filename):
            now = datetime.datetime.now()
            filename = 'g{0:%Y%m%d%H%M%S}_'.format(now) + secure_filename(img_file.filename)
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_url = '/uploads/' + filename
            img_list = sorted(glob.glob("./static/images/upload/*"))
            imgs = sorted(glob.glob("./static/images/upload/"))
            #print(img_list)
            return redirect(url_for('gallery'))
            #return render_template('gallery.html', title='Gallery', galleryImages=img_list) 
        else:
            return ''' <p>アップロードした写真は許可されていない拡張子です。（許可されている拡張子:'png', 'jpg', 'gif'）<br>アップロードファイル:''' + img_file.filename +'''</p> '''
    else:
        return redirect(url_for('gallery'))

@app.route('/delete/<filename>')
def delete_file(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('gallery'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)