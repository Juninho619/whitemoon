from cs50 import get_string
from flask import Flask, flash


# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    # Ask user for input
    a = get_string("Enter your text here: ")

    # Make sure user entered text
    if a = "":
        flash("Please enter a text")