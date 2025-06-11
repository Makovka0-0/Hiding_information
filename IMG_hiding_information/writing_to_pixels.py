from PIL import Image, ImageDraw
from random import randint
from re import findall

def stega_encrypt(img: str, text: str):
    text = "MAO" + text
    name = img
    img = Image.open(img)
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    f = open('keys.txt','w')

    for elem in ([ord(elem) for elem in text]):
        key = (randint(1, width - 10), randint(1, height - 10))
        g, b = pix[key][1:3]
        draw.point(key, (elem, g, b))
        f.write(str(key) + '\n')

    index = -1
    if ".png" in name: index = name.find(".png") - 1
    elif ".jpg" in name: index = name.find(".jpg") - 1
    elif ".bmp" in name: index = name.find(".bmp") - 1
    else: print("supported formats: png, jpg, bmp")

    output_name = name[:(index+1)] + "_encrypted.png"
    print('keys were written to the keys.txt file')
    img.save(output_name, "PNG")
    f.close()

def stega_decrypt(img: str):
    a = []
    keys = []
    img = Image.open(img)
    pix = img.load()
    f = open(input('path to keys: '),'r')
    y = str([line.strip() for line in f])

    for i in range(len(findall(r'\((\d+)\,', y))):
        keys.append((int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)', y)[i])))
    for key in keys:
        a.append(pix[tuple(key)][0])

    text = ''.join([chr(elem) for elem in a])
    if text[0:3] != "MAO": return [0, text]
    return [1, text[3:]]


def text_to_binary(event):
    return [int(format(ord(elem),'b')) for elem in event]
def binary_to_text(event):
    return [chr(int(str(elem),2)) for elem in event]



