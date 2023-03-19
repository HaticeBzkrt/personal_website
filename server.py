from flask import Flask
from flask import render_template
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.datetime.now().year
    return render_template("index.html", c_year = year)



if __name__ == "__main__":
    app.run(debug=True)
