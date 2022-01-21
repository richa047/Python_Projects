from PIL import Image, ImageDraw
import qrcode
data = "richa"
img = qrcode.make(data)
img.save("richa.png")

'''
#Status: not working.where to see the output



import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8) '''