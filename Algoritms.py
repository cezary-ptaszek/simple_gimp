import Convertion
from skimage.color import rgb2lab
from matplotlib import pyplot as plt
import numpy as np
from PIL import ImageEnhance, ImageFilter


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


def contrast(image, value):
    enhancer = ImageEnhance.Contrast(image)
    im_output = enhancer.enhance(value)
    return np.asarray(im_output)


def brightness(image, value):
    enhancer = ImageEnhance.Brightness(image)
    im_output = enhancer.enhance(value * 0.1)
    return np.asarray(im_output)


def saturation(image, value):
    converter = ImageEnhance.Color(image)
    img2 = converter.enhance(value)
    return np.asarray(img2)


def getHistorgramRGB(tab_rgb):
    colors = ("red", "green", "blue")
    channel_ids = (0, 1, 2)

    # create the histogram plot, with three lines, one for
    # each color
    plt.xlim([0, 256])
    for channel_id, c in zip(channel_ids, colors):
        histogram, bin_edges = np.histogram(
            tab_rgb[:, :, channel_id], bins=256, range=(0, 256)
        )
        plt.plot(bin_edges[0:-1], histogram, color=c)

    plt.xlabel("Color value")
    plt.ylabel("Pixels")

    plt.show()
    return tab_rgb


def getHistorgram(image):
    # Barwę opisują matematycznie trzy składowe:
    # L – jasność (luminancja),
    # a – barwa od zielonej do magenty,
    # b – barwa od niebieskiej do żółtej.
    lab = rgb2lab(image)

    plt.xlim([0, 100])
    histogram, bin_edges = np.histogram(
        lab[0, :, 0], bins=100, range=(0, 100)
    )
    plt.plot(bin_edges[0:-1], histogram)

    plt.xlabel("Lumination")
    plt.ylabel("Pixels")

    plt.show()
    return np.asarray(image)


def gaussianNoisy(image, var):
    image = image.filter(ImageFilter.GaussianBlur(radius=var))
    return np.asarray(image)
