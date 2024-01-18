from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)


@app.route("/")
def get_system_info():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    return f"System Date: {current_date}\nHostname: {hostname}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
