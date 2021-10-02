def convert(r, g, b):
    r /= 255
    g /= 255
    b /= 255

    c_min = min(r, g, b)
    c_max = max(r, g, b)
    delta = c_max - c_min

    if delta == 0:
        h = 0
    elif c_max == r:
        h = ((g - b) / delta) % 6
    elif c_max == g:
        h = (b - r) / delta + 2
    else:
        h = (r - g) / delta + 4

    h = round(h * 60)

    if h < 0:
        h += 360

    # Lightness
    l = (c_max + c_min) / 2

    # Saturation
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))

    s = round(s * 100, 1)
    l = round(l * 100, 1)

    print("hsl(" + str(h) + "," + str(s) + "%," + str(l) + "%)")
