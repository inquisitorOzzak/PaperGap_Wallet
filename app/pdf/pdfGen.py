
import os
import shutil
import tempfile

import qrcode
from pdf2image import convert_from_path
from reportlab.pdfgen import canvas
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

    print(output_List)
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

def generateCodes(addressList, abs_Path):
    if os.path.exists(abs_Path):
        #resetting previous path
        shutil.rmtree(abs_Path)
        os.mkdir(abs_Path)
    else:
        os.mkdir(abs_Path)


    for line in addressList:
        print(str(line[1]))
        createQR(line, abs_Path)



def generatePDF(title, QR_Status, Image_Path, addressArray):

    filename = str(title) + '.pdf'
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
        generateCodes(addressArray, Image_Path)
        for entry in addressArray:
            line = entry[0] + ': ' + entry[1]
            pdf.drawString(XCord, QRYCord, line)
            imgPath = Image_Path + str(entry[0])+'.jpg'
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




