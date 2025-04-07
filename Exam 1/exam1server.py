import flask
import threading
from exam1arduino import ArduinoCommander

app = flask.Flask(__name__, 
                  static_url_path="", 
                  static_folder="public")

serial_lock = threading.Lock()

@app.get("/")
def naked_domain_redirect():
    return flask.redirect("index.html")

@app.route("/api/<command>")
def command_api(command):
    with serial_lock:
        pl = ArduinoCommander()
        pl.connect("ttyACM0")
        response = pl.send_command(command)
        pl.disconnect()
        return response

app.run(host="0.0.0.0", port=8080, debug=True)
