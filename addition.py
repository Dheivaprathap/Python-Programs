from flask import Flask
app = Flask(__name__)
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(a + b)
app.run(debug=True)

