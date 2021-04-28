
import board
import busio
import adafruit_pct2075


def sensor():
    """Returns the PCT2075 object"""
    return adafruit_pct2075.PCT2075(busio.I2C(board.SCL, board.SDA))
