from PIL import Image, ImageDraw, ImageFont

def create_thumbnails(text):

    filenameFull = "./TNPics/FullTN.png"
    imFull = Image.open(filenameFull)
    print(imFull.size)
    dFull = ImageDraw.Draw(imFull)
    customfont = ImageFont.truetype("./Fonts/Alegreya-Bold.ttf", size=150)
    # height_text, width_text = dFull.textsize(text, customfont)
    width_text, height_text = customfont.getsize(text)
    print(height_text,width_text)
    top_left_x = 960 - (width_text / 2)
    top_left_y = 850
    xy = top_left_x, top_left_y

    BLACK = (0, 0, 0)
    dFull.text(xy, text, font=customfont, fill=BLACK)
    imFull.save("./OutputFiles/fullvideothumbnail.png")

    filenameSummary = "./TNPics/SummaryTN.png"
    imSummary = Image.open(filenameSummary)
    dSummary = ImageDraw.Draw(imSummary)
    dSummary.text(xy, text, font=customfont, fill=BLACK)
    imSummary.save("./OutputFiles/summaryvideothumbnail.png")