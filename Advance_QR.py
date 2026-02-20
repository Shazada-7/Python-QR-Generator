# Importing Basic Necessities
import qrcode
from PIL import Image
import qrcode.constants

#Now Setting Up The QR Code Sizing, Border & Error Correction
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,
                 )
#Data You Want To Put in a QR Code
qr.add_data("https://google.com")            # Change Link Here //
qr.make(fit=True)
img=qr.make_image(fill_color="Black",back_color="white")
img.save("QR_Code.png")

print("QR Code Generated....")