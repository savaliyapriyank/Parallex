import qrcode

#Taking UPI ID As a input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support

paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'

#Create QR Codes for each payment app
paytm_qr = qrcode.make(paytm_url)

#Save the QR code to image file (optional)
# paytm_qr.save( 'paytm_qr.png')
                    
#Display the QR codes (you may need to install PIL/Pillow Library)
paytm_qr.show()
