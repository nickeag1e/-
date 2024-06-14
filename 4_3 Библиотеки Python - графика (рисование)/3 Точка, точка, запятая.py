def human(colorbg, colorline, size, width):
    from PIL import Image, ImageDraw
    im = Image.new('RGB', (16 * size, 21 * size), colorbg)
    draw = ImageDraw.Draw(im)
    draw.ellipse(((6 * size, 1 * size), (10 * size, 5 * size)), width=width, outline=colorline)
    draw.ellipse(((7 * size - size // 5, 3 * size - size // 5), (7 * size + size // 5, 3 * size + size // 5)),
                 width=width, fill=colorline)
    draw.ellipse(((9 * size - size // 5, 3 * size - size // 5), (9 * size + size // 5, 3 * size + size // 5)),
                 width=width, fill=colorline)
    draw.arc(((6 * size, size - size // 2), (10 * size, 5 * size - size // 2)), start=45, end=135, width=width,
             fill=colorline)
    draw.line(((8 * size, 5 * size), (8 * size, 11 * size)), width=width, fill=colorline)
    draw.line(((7 * size, 6 * size), (9 * size, 6 * size)), fill=colorline, width=width)
    draw.line(((4 * size, 10 * size), (7 * size, 6 * size)), fill=colorline, width=width)
    draw.line(((9 * size, 6 * size), (12 * size, 10 * size)), fill=colorline, width=width)
    draw.line(((12 * size, 10 * size), (15 * size, 7 * size)), fill=colorline, width=width)
    draw.line(((4 * size, 10 * size), (6 * size, 13 * size)), fill=colorline, width=width)
    draw.line(((8 * size, 11 * size), (11 * size, 10 * size)), fill=colorline, width=width)
    draw.line(((11 * size, 10 * size), (13 * size, 15 * size)), fill=colorline, width=width)
    draw.line(((13 * size, 15 * size), (15 * size, 14 * size)), fill=colorline, width=width)
    draw.line(((8 * size, 11 * size), (6 * size, 15 * size)), fill=colorline, width=width)
    draw.line(((6 * size, 15 * size), (5 * size, 20 * size)), fill=colorline, width=width)
    draw.line(((5 * size, 20 * size), (7 * size, 20 * size)), fill=colorline, width=width)

    draw.ellipse((((7 * size - size // 5, 6 * size - size // 5)), (7 * size + size // 5, 6 * size + size // 5)),
                 fill=colorline, width=width)
    draw.ellipse((((9 * size - size // 5, 6 * size - size // 5)), (9 * size + size // 5, 6 * size + size // 5)),
                 fill=colorline, width=width)
    draw.ellipse((((4 * size - size // 5, 10 * size - size // 5)), (4 * size + size // 5, 10 * size + size // 5)),
                 fill=colorline, width=width)
    im.save('human.png', 'PNG')


human('#00fAdc', (200, 0, 0), 50, 7)
