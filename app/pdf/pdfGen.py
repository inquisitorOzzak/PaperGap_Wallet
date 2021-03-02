
import os
import shutil
import qrcode

from reportlab.pdfgen import canvas
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
def parseTextFile(limit):
    user_Absolute_Path = os.path.abspath('derived_addresses.txt')
    infile = open(user_Absolute_Path)
    output_List = []

    count = 0
    for line in infile:
        if count > limit - 1:
            break
        line = line.strip("\n")
        formatted_Line = line.split(":\t")
        output_List.append(formatted_Line)
        count += 1

    return output_List

def createQR(data, path):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=50,
                       border=4)
    qr.add_data(str(data[1]))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    QR_Filename = path + str(data[0]) + ".jpg"
    img.save(QR_Filename)

    #resizing image
    image = Image.open(QR_Filename)
    new_image = image.resize((128, 128))
    new_image.save(QR_Filename)

def generateCodes(addressList):
    rel_path = '../../app/pdf/QR/'

    if os.path.exists(rel_path):
        shutil.rmtree(rel_path, ignore_errors=True)
        os.mkdir(rel_path)
    else:
        os.mkdir(rel_path)


    for line in addressList:
        print(str(line[1]))
        createQR(line, rel_path)



def generatePDF(title, QR_Status, rel_Image_Path, addressArray):

    filename = str(title) + '_Wallet.pdf'
    documentTitle = str(title)

    pdf = canvas.Canvas(filename)
    pdf.setTitle(documentTitle)
    pdf.drawCentredString(300, 750, documentTitle)


    pdf.setFont('Helvetica', size=10)

    pdf.line(30, 710, 550, 710)

    XCord = 40
    YCord = 680

    QRXCord = 350
    QRYCord = 600
    if QR_Status == True:
        print("generating pdf with QR codes")
        generateCodes(addressArray)
        for entry in addressArray:
            line = entry[0] + ': ' + entry[1]
            pdf.drawString(XCord, QRYCord, line)
            imgPath = rel_Image_Path + str(entry[0])+'.jpg'
            pdf.drawImage(imgPath, QRXCord + 30, QRYCord - 60)
            QRYCord -= 120

            if QRYCord < 60:
                QRYCord = 680
                pdf.showPage()

        pdf.save()
        return

    else:
        print("generating pdf with no QR codes")

        for entry in addressArray:
            line = entry[0] + ': ' + entry[1]
            pdf.drawString(XCord, YCord, line)
            YCord -= 20

            if YCord < 60:
                YCord = 720
                pdf.showPage()

        pdf.save()
        return

# addresses = parseTextFile("../derived_addresses.txt", 10)
# generateCodes(addresses)
# generatePDF("Robs_Wallet", True, '../app/pdf/QR/', addresses)

