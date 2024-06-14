def stripes(count, sizes, direction='v'):
    from PIL import Image, ImageDraw
    im = Image.new('RGB', sizes, '#ffffff')
    draw = ImageDraw.Draw(im)
    if direction == 'h':
        for y in range(0, sizes[1], round(sizes[1] / count * 2)):
            draw.rectangle((0, y, sizes[0] - 1, y + round(sizes[1] / count)), fill='#000000', width=0, outline=0)
    if direction == 'v':
        for x in range(0, sizes[0], round(sizes[0] / count * 2)):
            draw.rectangle((x, 0, x + round(sizes[0] / count), sizes[1] - 1), fill='#000000', width=0, outline=0)
    im.save('zebra.png', 'PNG')


stripes(5, (600, 400), direction='v')
