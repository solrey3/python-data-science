# -*- coding: utf-8 -*-
 
#
# Imports
#
from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
 
app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)
 
#
# Routes
#
# @app.route('/', methods=['GET'])
# def hello_world():
#     return jsonify({'message': 'Hello World'})
 
# @app.route('/test', methods=['GET'])
# def test():
#     return jsonify({'test': 'test'})

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
 
if __name__ == "__main__":
    app.run(debug=True) # remember to set debug to False