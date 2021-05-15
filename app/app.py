
from flask import Flask, jsonify

from connect import sensor


LOCATION = "server_room"
sensor = sensor()  # Temp sensor

# Flask
app = Flask(__name__)
debug = False


@app.route("/", methods=["GET"])
def temp() -> str:
    """Returns the temp (Centigrade) from the gpio temp sensor

    Returns:
        str: JSON string {"temp": float, "error": bool, "loc": str}
    """
    error = False
    try:

        return_val = sensor.temperature

    except Exception as exc:
        if debug:
            print(exc)

        error = True
        return_val = 0

    return jsonify({"temp": return_val, "error": error, "loc": LOCATION})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=82, debug=debug)
