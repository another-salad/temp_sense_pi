
from flask import Flask, jsonify

from connect import sensor


sensor = sensor()  # Temp sensor

# Flask
app = Flask(__name__, static_url_path="")
debug = False


@app.route("/temp", methods=["GET"])
def temp() -> str:
    """Returns the temp (Centigrade) from the gpio temp sensor

    Returns:
        str: JSON string {"temp": float, "error" Null or String}
    """
    exc_msg = None
    try:

        return_val = sensor.temperature

    except Exception as exc:
        exc_msg = str(exc)
        return_val = 0

    return jsonify({"temp": return_val, "error": exc_msg})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082, debug=debug)
