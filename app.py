from flask import Flask, render_template, url_for
import dotenv
import os

dotenv.load_dotenv()

app = Flask(__name__)

app.config["FLASK_APP"] = os.getenv("FLASK_APP")
app.config["FLASK_ENV"] = os.getenv("FLASK_ENV")
app.config["FLASK_DEBUG"] = os.getenv("FLASK_DEBUG")


@app.route("/")
def index():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
