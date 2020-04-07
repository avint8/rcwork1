from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import alg
import keys
import os



app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = '0'
    response.headers["Pragma"] = "no-cache"
    return response
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt', methods = ['GET', 'POST'])
def enc():
    f=0
    key=0
    if request.method == 'POST':
        call ='e'
        f = 1
        img = request.files['image']

        img.save('static/'+'img.tiff')
        key = keys.enc()
        alg.encrypt()
        
    return render_template('encrypt.html',f=f , key=key)    

@app.route('/decrypt', methods = ['GET', 'POST'])
def dec():
    f=0
    if request.method == 'POST':
        f = 1
        call = 'd'
        img = request.files['image']
        dkey = request.form['key']


        img.save('static/'+'enimg.tiff')

        keys.dec(dkey)
        alg.decrypt()

    return render_template('decrypt.html',f=f)   




if __name__ == '__main__':
   app.run(threaded=Tree, port= 5000)