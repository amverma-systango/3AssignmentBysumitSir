from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    render_template("index.html")


app.run()
