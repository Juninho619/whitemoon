from flask import Flask, flash


# Configure application
app = Flask(__name__)

@app.route("/")
def index():

    if method == "GET":
        # Ask user for input
        text = request.form.get("text")
        keyword = request.form.get("keyword")


def keyword():

    for i in range(text):
        if i == " ":
            i += 1
            word_count = i + 1
            return word_count

    for j in range(text):
        if j == keyword:
            j += 1
            return j

    keyword_density = j * 100 / word_count


    if keyword_density > 0.015:
         # Inform user that he should reduce keyword density

    elif keyword_density < 0.015:
        # Inform user he should enter more keywords

    elif keyword_density == 0.015:
        # Inform user density is correct