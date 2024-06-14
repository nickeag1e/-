def snow_forest(coords, p):
    from PIL import Image
    p = p / 100
    forest = Image.open('forest.png')
    snow = Image.open('snow.png').resize((100, 100))
    w, h = forest.size
    pixels1 = forest.load()
    pixels2 = snow.load()
    for i in range(100):
        for j in range(100):
            r1, g1, b1 = pixels1[coords[0] + i, coords[1] + j]
            r2, g2, b2 = pixels2[i, j]
            pixels1[coords[0] + i, coords[1] + j] = (
                round(r1 * (1 - p) + r2 * p),
                round(g1 * (1 - p) + g2 * p),
                round(b1 * (1 - p) + b2 * p)
            )
    forest.save('output.png')


snow_forest((450, 300), 30)
