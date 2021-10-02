from tkinter import *
import tkinter.font as font
from tkinter import ttk
from tkinter.filedialog import askopenfilename

VALUES = ['Desaturacja',
          'Kontrast',
          'Negatyw']


def chooseFile():
    filename = askopenfilename(initialdir="/", title="Select file")
    labelChooseFileState['text'] = filename


def run():
    print()


window = Tk()
window.title('Przetwarzanie obrazu')
window.geometry('500x500')
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
comboChoosePeriod = ttk.Combobox(window, values=VALUES, state='readonly')
comboChoosePeriod.grid(column=2, row=3, pady=20, padx=10)

buttonRun = Button(window, text='Przetwórz', command=run, width=10)
buttonRun.grid(column=1, row=4, columnspan=2, pady=5)


window.mainloop()
