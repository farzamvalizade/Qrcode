import pyqrcode
from pyqrcode import QRCode
dest ="https://www.dropbox.com/scl/fi/8fo5dnmghaxhf7jksvvet/Screenshot-4.png?rlkey=7nn4957qdthzikjihobvzan4y&dl=0"
myQR = QRCode(dest, error='H', version=None, mode=None, encoding='iso-8859-1')
myQR.png('qrcode1.png', scale=8)