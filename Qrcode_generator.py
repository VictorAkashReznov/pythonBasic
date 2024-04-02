import qrcode
from PIL import Image
def Qrcode_generator_Default( address , nameQrCode): # without any discription 
    qr= qrcode.make(address)
    qr.save(nameQrCode+".png")

def Qrcode_generator_customized(address , nameQrCode, BoxSize, Border, colour_foreground, colour_background ): # with discription 1.boxSize 2.border 3.color
    qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=BoxSize , border=Border)
    qr.add_data(address)
    qr.make(fit=True)
    img_new=qr.make_image(fill_color=colour_foreground, back_color=colour_background)
    img_new.save(nameQrCode+".png")


print("Want to use a Customized press 1 or default 0 ")
k=int(input("Enter Preference "))
if k==1:
    address=input("Enter web Address ")
    nameQrCode=input("Enter QrCode name ")
    BoxSize=int(input("Enter BoxSize "))
    Border=int(input("Enter borderSize "))
    foreground=input("Enter ForeGround color ")
    backGround=input("Enter BackGround color ")
    Qrcode_generator_customized(address, nameQrCode, BoxSize, Border, foreground, backGround)
else:
    address=input("Enter web Address ")
    nameQrCode=input("Enter QrCode name ")
    Qrcode_generator_Default(address, nameQrCode)

