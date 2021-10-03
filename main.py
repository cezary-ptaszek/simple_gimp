from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import Algoritms as alg
import numpy as np

VALUES = ['Desaturacja',
          'Kontrast',
          'Negatyw',
          'Jasność',
          'Nasycenie',
          'HistogramRGB',
          'Histogram',
          'Gauss']


def chooseFile():
    filename = askopenfilename(initialdir="/", title="Select file")
    # label = labelChooseFileState['text'] = filename
    label = labelChooseFileState['text'] = 'sample/owl.jpg'
    if label != 'nie wybrano':
        global IMPORTED_IMG
        IMPORTED_IMG = Image.open(label)
        canvas.image = ImageTk.PhotoImage(IMPORTED_IMG)
        canvas.create_image(0, 0, image=canvas.image, anchor=NW)
    if comboChooseFunc.get() == 'Kontrast' \
            or comboChooseFunc.get() == 'Jasność' \
            or comboChooseFunc.get() == 'Gauss'\
            or comboChooseFunc.get() == 'Nasycenie':
        scala['state'] = tk.NORMAL
        window.update()


def run():
    func = comboChooseFunc.get()
    tab_rgb = np.asarray(IMPORTED_IMG)
    tab = []

    # Desaturacja
    if func == VALUES[0]:
        tab = alg.desaturation(tab_rgb)
        print('Desaturacja')

    # Kontrast
    if func == VALUES[1]:
        tab = alg.contrast(IMPORTED_IMG, scala.get())
        print('Kontrast')

    # Negatyw
    if func == VALUES[2]:
        tab = alg.negative(tab_rgb)
        print('Negatyw')

    # Jansość
    if func == VALUES[3]:
        tab = alg.brightness(IMPORTED_IMG, scala.get())
        print('Jasność')

    # Nasycenie
    if func == VALUES[4]:
        tab = alg.saturation(IMPORTED_IMG, scala.get())
        print('Nasycenie')

    # Historgram
    if func == VALUES[5]:
        tab = alg.getHistorgramRGB(tab_rgb)
        print('HistogramRGB')

    # HistorgramRGB
    if func == VALUES[6]:
        tab = alg.getHistorgram(IMPORTED_IMG)
        print('HistogramRGB')

    # Gauss
    if func == VALUES[7]:
        tab = alg.gaussianNoisy(IMPORTED_IMG, scala.get())
        print('Gauss')

    createWindow(Image.fromarray(tab))


def createWindow(image):
    def save(im):
        im.save("saved.jpg")

    t = tk.Toplevel(window)
    canvas = Canvas(t, width=300, height=300)
    canvas.grid(column=0, row=0)
    canvas.image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=canvas.image, anchor=NW)
    buttonSave = Button(t, text='Zapisz', command=save(image), width=10)
    buttonSave.grid(column=0, row=1)


window = Tk()
window.title('Przetwarzanie obrazu')
window.geometry('500x550')
window.configure(background='white')

fontStyle = font.Font(family="Lucida Grande", size=15)

labelChoosePeriod = Label(window, text='Wybierz filtr', font=fontStyle, bg='white')
labelChoosePeriod.grid(column=0, row=0, pady=5, padx=20)

comboChooseFunc = ttk.Combobox(window, values=VALUES, state='readonly')
comboChooseFunc.grid(column=2, row=0, pady=5, padx=10)


labelGauss = Label(window, text='Skala rozmycia', font=fontStyle, bg='white')
labelGauss.grid(column=0, row=1, pady=5, padx=10)

scala = Scale(window, from_=0, to=100, state=DISABLED, orient=HORIZONTAL)
scala.grid(column=2, row=1, pady=5, padx=10)


labelChooseFile = Label(window, text='Wybierz obraz', font=fontStyle, bg='white')
labelChooseFile.grid(column=0, row=2, columnspan=2, padx=50, pady=20)

buttonChooseFile = Button(window, text='Wybierz', command=chooseFile, width=10)
buttonChooseFile.grid(column=2, row=2, columnspan=2, pady=5)

labelChooseFileState = Label(window, text='nie wybrano', bg='white')
labelChooseFileState.grid(column=1, row=3, columnspan=2, pady=5, padx=10)

buttonRun = Button(window, text='Przetwórz', command=run, width=10)
buttonRun.grid(column=1, row=5, columnspan=2, pady=5)

canvas = Canvas(window, width=300, height=300)
canvas.grid(column=1, row=6, columnspan=2, pady=5)

window.mainloop()
