from tkinter import *
import tkinter.font as font
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import RGBtoHSL

VALUES = ['Desaturacja',
          'Kontrast',
          'Negatyw']


def chooseFile():
    filename = askopenfilename(initialdir="/", title="Select file")
    # label = labelChooseFileState['text'] = filename
    label = labelChooseFileState['text'] = 'sample/owl.jpg'
    if label != 'nie wybrano':
        global IMPORTED_IMG
        IMPORTED_IMG = Image.open(label)
        canvas.image = ImageTk.PhotoImage(IMPORTED_IMG)
        canvas.create_image(0, 0, image=canvas.image, anchor=NW)


def run():
    func = comboChooseFunc.get()
    # Desaturacja
    if func == VALUES[0]:
        tab_pix = list(IMPORTED_IMG.getdata())
        print(tab_pix)
        for sets in tab_pix:
            RGBtoHSL.convert(sets[0], sets[1], sets[2])
        print('Desaturacja')


window = Tk()
window.title('Przetwarzanie obrazu')
window.geometry('500x550')
window.configure(background='white')

fontStyle = font.Font(family="Lucida Grande", size=15)
labelChooseFile = Label(window, text='Wybierz obraz', font=fontStyle, bg='white')
labelChooseFile.grid(column=0, row=0, columnspan=2, padx=50, pady=20)

buttonChooseFile = Button(window, text='Wybierz', command=chooseFile, width=10)
buttonChooseFile.grid(column=2, row=0, columnspan=2, pady=5)

labelChooseFileState = Label(window, text='nie wybrano', bg='white')
labelChooseFileState.grid(column=1, row=2, columnspan=2, pady=5, padx=10)

labelChoosePeriod = Label(window, text='Wybierz filtr', bg='white')
labelChoosePeriod.grid(column=0, row=3, pady=20, padx=10)

comboChooseFunc = ttk.Combobox(window, values=VALUES, state='readonly')
comboChooseFunc.grid(column=2, row=3, pady=20, padx=10)

buttonRun = Button(window, text='Przetwórz', command=run, width=10)
buttonRun.grid(column=1, row=4, columnspan=2, pady=5)

canvas = Canvas(window, width=300, height=300)
canvas.grid(column=1, row=5, columnspan=2, pady=5)

window.mainloop()
