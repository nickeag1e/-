def train(save):
    from PIL import Image, ImageDraw
    im = Image.new('RGB', (280, 200), '#ccecff')
    draw = ImageDraw.Draw(im)
    draw.rectangle((40, 110, 80, 150), fill='#c55a11')
    draw.polygon(((40, 110), (60, 75), (80, 110)), fill='#ffc000')
    draw.rectangle((80, 90, 160, 150), fill='#0070c0')
    draw.rectangle((80, 60, 110, 90), fill='#ff0000')
    draw.polygon(((80, 60), (95, 34), (110, 60)), fill='#ffc000')
    draw.rectangle((160, 50, 240, 150), fill='#548235')
    draw.rectangle((150, 40, 250, 50), fill='#c55a11')
    draw.rectangle((185, 60, 215, 100), fill='#ffffff')
    draw.ellipse(((80, 140), (110, 170)), fill='#000000')
    draw.ellipse(((120, 130), (160, 170)), fill='#000000')
    draw.ellipse(((180, 130), (220, 170)), fill='#000000')
    im.save(save, "PNG")

train("out.png")