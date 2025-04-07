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
        pl.connect("/dev/ttyACM0")
        response = pl.send_command(command)
        pl.disconnect()
        return response

@app.route("/api/led/on")
def led_on():
    return send_serial_command("LED ON")

@app.route("/api/led/off")
def led_off():
    return send_serial_command("LED OFF")

@app.route("/api/flash/<int:count>/<int:delay>")
def flash(count, delay):
    return send_serial_command(f"FLASH {count} {delay}")

app.run(host="0.0.0.0", port=8080, debug=True)
