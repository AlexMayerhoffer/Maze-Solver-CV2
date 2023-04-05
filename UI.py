from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import numpy as np
import cv2
from PIL import ImageTk, Image
from Solver import Solver


class UI:
    def __init__(self):
        self.image_label = None
        self.image = None
        self.can_solve = False

        self.window = Tk()
        self.window.geometry('500x500')

        self.menu_bar = Menu(self.window)
        self.menu_bar.add_command(label='Add Image', command=self.selectImagine)
        self.menu_bar.add_separator()
        self.menu_bar.add_command(label='Solve Maze', command=self.rezolvaLabirint)

        canvas = Canvas(self.window, width=300, height=300)
        canvas.pack()

        self.window.config(menu=self.menu_bar)
        self.window.mainloop()

    def afisareImagine(self):
        blue, green, red = cv2.split(self.image)
        img = cv2.merge((red, green, blue))
        img = Image.fromarray(img)
        img = img.resize((400, 400))
        imgtk = ImageTk.PhotoImage(image=img)
        self.image_label = Label(self.window, image=imgtk)
        self.image_label.place(relx=0.5, rely=0.5, anchor='center')
        self.window.mainloop()

    def selectImagine(self):
        filetypes = (
            ('Image file', '*.png'),
            ('All files', '*.*')
        )

        filename = askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        # TODO chestii dupa incarcarea imaginii

        self.image = cv2.imread(filename)
        self.can_solve = True
        self.afisareImagine()

    def rezolvaLabirint(self):
        if self.image is not None:
            if self.can_solve:
                self.image = Solver.solve(self.image)
                self.can_solve = False
                self.afisareImagine()
            else:
                messagebox.showerror('Eroare!', 'Selecteaza o noua imagine!')
        else:
            messagebox.showerror('Eroare!', 'Selecteaza o imagine!')

