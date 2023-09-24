from flask import Flask, render_template, url_for, jsonify
import dotenv
import os

dotenv.load_dotenv()

app = Flask(__name__)

app.config["FLASK_APP"] = os.getenv("FLASK_APP")
app.config["FLASK_ENV"] = os.getenv("FLASK_ENV")
app.config["FLASK_DEBUG"] = os.getenv("FLASK_DEBUG")


JOBS = [
    {"id": 1, "title": "Data Analyst", "location": "Warsaw", "salary": "6000 zł"},
    {"id": 2, "title": "Backend Engineer", "location": "Warsaw", "salary": "8000 zł"},
    {"id": 3, "title": "Frontend Engineer", "location": "Remote", "salary": "7000 zł"},
    {"id": 4, "title": "Fullstack Engineer", "location": "Wrocław"},
]


@app.route("/")
def index():
    return render_template("index.html", jobs=JOBS)


@app.route("/api/jobs")
def json():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
