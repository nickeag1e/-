def wb_negative(image):
    from PIL import Image
    im = Image.open(image)

    pixels = im.load()
    x, y = im.size

    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            grey = 255 - (r + g + b) // 3
            pixels[i, j] = grey, grey, grey
    im.save('out.png')
wb_negative('riana2.jpeg')