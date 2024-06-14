def search_for_lilies(image, color):
    w, h = image.size
    pixels = image.load()
    max_count = 0
    max_n = 0
    for i in range(w):
        count = 0
        for j in range(h):
            c = pixels[i, j]
            if c == color:
                count += 1
        if count > max_count:
            max_count = count
            max_n = i
    return max_n * 1001 // w - 500

from PIL import Image
image = Image.open(input())
color = tuple(map(int, input().split()))
print(search_for_lilies(image, color))