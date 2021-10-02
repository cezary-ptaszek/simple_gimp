import Convertion


def desaturation(tab_rgb):
    for sets in tab_rgb:
        for i in sets:
            r = float(i[0])
            g = float(i[1])
            b = float(i[2])
            high = max(r, g, b)
            low = min(r, g, b)
            h, s, l = ((high + low) / 2,) * 3

            if high == low:
                h = 0.0
                s = 0.0
            else:
                d = high - low
                s = 0.0
                h = {
                    r: (g - b) / d + (6 if g < b else 0),
                    g: (b - r) / d + 2,
                    b: (r - g) / d + 4,
                }[high]
                h /= 6
            i[0], i[1], i[2] = Convertion.hsl_to_rgb(h, s, l)
    return tab_rgb


def negative(tab_rgb):
    for sets in tab_rgb:
        for i in sets:
            redPixel = 255 - i[0]
            greenPixel = 255 - i[1]
            bluePixel = 255 - i[2]
            i[0], i[1], i[2] = redPixel, greenPixel, bluePixel
    return tab_rgb
