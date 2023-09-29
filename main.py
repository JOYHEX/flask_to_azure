#insert python code 
from flask import Flask, jsonify, session, request

app = Flask(__name__)


@app.route("/hello")
def data(object_name):
    return "No data found !!"

if __name__=='__main__':
    app.run()