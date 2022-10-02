# QR CODE GENERATOR
import pyqrcode

text = input('Enter the text to generate the QR code for: ')

# create a pyqrcode object by calling the create() method 
# with the text input as argument
qr_code = pyqrcode.create(text)

# calling the svg() method of the qr_code object
# creates a file named 'qr_code.svg' in svg format
# the scale argument specifies how large the image should be
qr_code.svg('qr_code.svg', scale=8)