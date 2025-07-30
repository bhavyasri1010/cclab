from flask import Flask
import os

App = Flask(__name__)

@App.route("/")
def hello():
    return "hello world"

if __name__=="__main__":
    port=int(os.environ.get("PORT" ,5000))
    App.run(host="0.0.0.0" ,port=port)
