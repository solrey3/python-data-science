# -*- coding: utf-8 -*-
 
#
# Imports
#
from flask import Flask, jsonify
 
app = Flask(__name__)
 
#
# Routes
#
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello World'})
 
@app.route('/test', methods=['GET'])
def test():
    return jsonify({'test': 'test'})
 
if __name__ == "__main__":
    app.run(debug=True) # remember to set debug to False