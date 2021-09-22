#Import Library
import qrcode
import cv2


# Read QR Code
def qr_reader(qrImageName):
    img = cv2.imread(qrImageName)
    det = cv2.QRCodeDetector()
    val, pts, st_code = det.detectAndDecode(img)
    print(val)


def qr_generator(qrMessage, qrSaveName):
    # Generate QR Code
    img = qrcode.make(qrMessage)
    img.save(qrSaveName)


qr_reader('hello.png')
