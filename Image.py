from PIL import Image
import io
import urllib
import os
import shutil

from Link import getlinkfromkw

def saveImagebySearch(keyword, title, driver, language):
    url = ""
    newimg = ""
    try:
        url = getlinkfromkw(keyword, driver, language)
        imageweb = urllib.request.urlopen(url)
        imagefilename = io.BytesIO(imageweb.read())
        newimg = Image.open(imagefilename)
    except:
        url = getlinkfromkw(title, driver, language)
        imageweb = urllib.request.urlopen(url)
        imagefilename = io.BytesIO(imageweb.read())
        newimg = Image.open(imagefilename)
    # urllib.request.urlretrieve(url, "./Downloads/images/currentimage.{}".format(url.split(".")[-1]))
    # imageweb = urllib.request.urlopen(url)
    # imagefilename = io.BytesIO(imageweb.read())
    # newimg = Image.open(imagefilename)
    # imagefilename = "./Downloads/images/currentimage.{}".format(url.split(".")[-1])
    print("Found Image")
    imgwidth, imgheight = newimg.size
    newwidth = imgwidth * 1080 // imgheight
    if newwidth > 1920:
        newwidth = 1920
    newimg = newimg.resize((newwidth, 1080))
    flankingimage1 = Image.new('RGB', ((1920-newwidth)//2,1080))
    flankingimage2 = Image.new('RGB', ((1920-newwidth)//2,1080))
    dst = Image.new('RGB', (flankingimage1.width + newimg.width + flankingimage2.width, newimg.height))
    dst.paste(flankingimage1, (0, 0))
    dst.paste(newimg, (flankingimage1.width, 0))
    dst.paste(flankingimage2, (flankingimage1.width + newimg.width, 0))

    folder = './Downloads/images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except:
            print('Failed to delete')

    dst = dst.convert("RGB")
    dst.save("./Downloads/images/currentimage.png")
    return "./Downloads/images/currentimage.png"