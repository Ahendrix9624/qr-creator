"""
USAGE - The code generates a QR code for a given website link (here, the YouTube channel link) 
        using the qrcode library. It creates an instance of QRCode, adds the website link to it, 
        and generates an image of the QR code with the specified box size, border, and color 
        using make_image() function. Finally, it saves the generated image as 'qrcode001.png' in 
        the current working directory.

AUTHOR - https://github.com/Ahendrix9624/
"""
import qrcode
# Link for website
input_data = "https://www.youtube.com/channel/UCWA6QltSggvOm49y9Mx_vPQ"

#Creating an instance of qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')
