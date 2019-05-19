from flask import Flask, request, render_template, redirect
from threading import Thread
import time
import random
app = Flask(__name__)
spi = {"VACA": "cit1"}
@app.route('/')
def index():
    global spi
    page = render_template('main.html', a=spi)
    return page
@app.route('/create', methods=['GET'])
def create_html():
    page = render_template('create.html')
    return page

@app.route('/create', methods=['POST'])
def create():
    global spi
    spi[request.form.get("author")] = request.form.get("cit")
    return redirect('/')

app.run(debug=True, port=8089)
