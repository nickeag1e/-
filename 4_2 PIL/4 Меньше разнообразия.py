def less_variety(image, new_image):
    from PIL import Image
    im = Image.open(image)
    w, h = im.size
    pixels = im.load()
    count_color = len(set([pixels[i, j] for i in range(w) for j in range(h)]))
    while count_color > 256:
        count_color //= 2
    im = im.resize((w // 2, h // 2)).quantize(count_color)
    im.save(new_image)
less_variety('example.png', 'out.png')