def direction(image, color):
    w, h = image.size
    pixels = image.load()
    sx, sy = 0, 0
    kx, ky = 0, 0
    for i in range(w):
        for j in range(h):
            color1 = pixels[i, j]
            if color == color1:
                sx += i
                sy += j
                kx += 1
                ky += 1
    sredx = sx // kx
    sredy = sy // ky
    return abs(sredx - w // 2), abs(sredy - h // 2)
image = Image.open(input())
color = tuple(map(int, input().split()))
print(*direction(image, color))
