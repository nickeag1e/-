def reflect(image, kind):
    from PIL import Image

    im = Image.open(image)
    if kind == 1:
        method = Image.FLIP_TOP_BOTTOM
    elif kind == 2:
        method = Image.FLIP_LEFT_RIGHT
    else:
        method = Image.ROTATE_180
    im = im.transpose(method)
    im.save('result.png')
reflect('example.png', 1)