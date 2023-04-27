#!/bin/python

from flask import Flask, render_template
import requests
import json


def api_response():
    from flask import jsonfy
    if request.method == 'POST':
        return jsonfy(**request.json)

app = Flask(__name__)

def get_meme():
    #Uncomment these two lines and comment out the other url line if you want to use a specific meme subreddt
    sr = "/wholesomememes"
    url = "<https://preview.redd.it/...f2cdfbcc3070bc6061a97418>" + sr
    #url = "<https://meme-api.herokuapp.com/gimme>"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host="0.0.0.0", port=5000)
