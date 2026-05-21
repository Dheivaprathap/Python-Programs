
from flask import Flask

app = Flask(__name__)

@app.route("/api")
def api():
    return {
        "name": "Hackup",
        "course": "Python"
    }

app.run(debug=True)
