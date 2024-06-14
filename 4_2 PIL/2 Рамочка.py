def frame(image, width):
    from PIL import Image

    im = Image.open(image)
    x, y = im.size
    im = im.crop((x // 3, y // 3, 2 * x // 3, 2 * y // 3))
    x, y = im.size
    pixels = im.load()
    mid_r, mid_g, mid_b = 0, 0, 0

    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            mid_r, mid_g, mid_b = mid_r + r, mid_g + g, mid_b + b
    mid_r, mid_g, mid_b = mid_r // (x * y), mid_g // (x * y), mid_b // (x * y)
    im_new = Image.new('RGB', (x + width * 2, y + width * 2), (mid_r, mid_g, mid_b))
    im_new.paste(im, (width, width))
    im_new.save('done.png')


frame('bug.png', 20)
