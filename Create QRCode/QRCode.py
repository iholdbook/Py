# Import QRCode from pyqrcode
import pyqrcode
from pyqrcode import QRCode
import png

# String which represent the QR code
s = "any QR-code for you"

# Generate QR code .create(s)
url = pyqrcode.create(s)

# Create and save the png/svg file naming "QR.png"
url.png("QR.png", scale=6)
url.svg("QR.svg", scale=8)