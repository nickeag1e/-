def color_gradient(out, size, kind='linear', color='r'):
    from PIL import Image

    if kind == 'linear':
        im = Image.linear_gradient('L')
    else:
        im = Image.radial_gradient('L')
    w, h = im.size
    pixels = im.load()
    im2 = Image.new('RGB', (w, h), (0, 0, 0))
    pixels2 = im2.load()
    for i in range(w):
        for j in range(h):
            if color == 'r':
                c = pixels[i, j]
                pixels2[i, j] = c, 0, 0
            elif color == 'g':
                c = pixels[i, j]
                pixels2[i, j] = 0, c, 0
            elif color == 'b':
                c = pixels[i, j]
                pixels2[i, j] = 0, 0, c
    im2 = im2.crop(size)
    im2.save(out)
color_gradient("res.png", (0, 56, 256, 256), kind="radial", color="b")