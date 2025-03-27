import flask

app = flask.Flask(__name__)

@app.route("/api/<command>")
def command_api(command):
    return f"TODO: Implement command {command}"

app.run(host="0.0.0.0", port=8080, debug=True)