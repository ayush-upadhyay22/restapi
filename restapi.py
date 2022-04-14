from urllib import response
from flask import Flask,jsonify, request
from sqlalchemy import true




app=Flask("ayush")

@app.route("/")
def home():
    return "welcome to Flask"

app.run(debug=true)

