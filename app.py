import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
url_to_encrypt = "https://www.linkedin.com/in/sergio-andres-rojas/"
  
# Generate QR code 
url = pyqrcode.create(url_to_encrypt) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8) 