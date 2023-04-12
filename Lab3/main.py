import math
from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter
import cv2
import numpy as np
from tkinter import filedialog


class App:
    def __init__(self):
        super().__init__()
        self.root = tkinter.Tk()
        self.root.geometry("400x400")
        self.root.minsize(900, 600)
        self.root.maxsize(900, 600)
        self.panelA = None
        self.panelB = None
        self.path = ''
        formChoice = None

        def getStructuringElement():
            morph_kernel = None
            size = int(self.spinbox.get())
            if formChoice.get() == options[0]:
                morph_kernel = np.ones((size, size), 'uint8')
            elif formChoice.get() == options[1]:
                morph_kernel = np.zeros((size, size), 'uint8')
                center = math.ceil(size / 2) - 1
                for i in range(size):
                    morph_kernel[i][center] = 1
                    morph_kernel[center][i] = 1
            return morph_kernel

        def dilatation():
            img = cv2.imread(self.path)

            morph_kernel = getStructuringElement()
            print(morph_kernel)
            dilate_img = cv2.dilate(img, kernel=morph_kernel, iterations=1)

            dilate_img = cv2.cvtColor(dilate_img, cv2.COLOR_BGR2RGB)
            dilate_img = Image.fromarray(dilate_img)
            dilate_img = dilate_img.resize((400, 300))
            dilate_img = ImageTk.PhotoImage(dilate_img)

            self.panelB.configure(image=dilate_img)
            self.panelB.image = dilate_img

        def erosion():
            img = cv2.imread(self.path)

            morph_kernel = getStructuringElement()
            erode_img = cv2.erode(img, kernel=morph_kernel, iterations=1)

            erode_img = cv2.cvtColor(erode_img, cv2.COLOR_BGR2RGB)
            erode_img = Image.fromarray(erode_img)
            erode_img = erode_img.resize((400, 300))
            erode_img = ImageTk.PhotoImage(erode_img)

            self.panelB.configure(image=erode_img)
            self.panelB.image = erode_img

        def closure():
            img = cv2.imread(self.path)

            morph_kernel = getStructuringElement()
            dilate_img = cv2.dilate(img, kernel=morph_kernel, iterations=1)
            dilate_img = cv2.erode(dilate_img, kernel=morph_kernel, iterations=1)

            dilate_img = cv2.cvtColor(dilate_img, cv2.COLOR_BGR2RGB)
            dilate_img = Image.fromarray(dilate_img)
            dilate_img = dilate_img.resize((400, 300))
            dilate_img = ImageTk.PhotoImage(dilate_img)

            self.panelB.configure(image=dilate_img)
            self.panelB.image = dilate_img

        def breaking():
            img = cv2.imread(self.path)

            morph_kernel = getStructuringElement()
            erode_img = cv2.erode(img, kernel=morph_kernel, iterations=1)
            erode_img = cv2.dilate(erode_img, kernel=morph_kernel, iterations=1)

            erode_img = cv2.cvtColor(erode_img, cv2.COLOR_BGR2RGB)
            erode_img = Image.fromarray(erode_img)
            erode_img = erode_img.resize((400, 300))
            erode_img = ImageTk.PhotoImage(erode_img)

            self.panelB.configure(image=erode_img)
            self.panelB.image = erode_img

        def highFrequencyFilter1():
            img = cv2.imread(self.path)

            kernel = np.array([[0.0, -1.0, 0.0], [-1.0, 5.0, -1.0], [0.0, -1.0, 0.0]])
            filtered_img = cv2.filter2D(img, -1, kernel)

            filtered_img = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)
            filtered_img = Image.fromarray(filtered_img)
            filtered_img = filtered_img.resize((400, 300))
            filtered_img = ImageTk.PhotoImage(filtered_img)

            self.panelB.configure(image=filtered_img)
            self.panelB.image = filtered_img

        def highFrequencyFilter2():
            img = cv2.imread(self.path)

            kernel = np.array([[-1.0, -1.0, -1.0], [-1.0, 9.0, -1.0], [-1.0, -1.0, -1.0]])
            filtered_img = cv2.filter2D(img, -1, kernel)

            filtered_img = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)
            filtered_img = Image.fromarray(filtered_img)
            filtered_img = filtered_img.resize((400, 300))
            filtered_img = ImageTk.PhotoImage(filtered_img)

            self.panelB.configure(image=filtered_img)
            self.panelB.image = filtered_img

        def select_image():
            self.path = filedialog.askopenfilename()
            if len(self.path) > 0:
                image = cv2.imread(self.path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = image.resize((400, 300))
                image = ImageTk.PhotoImage(image)
                if self.panelA is None or self.panelB is None:
                    self.panelA = Label(image=image)
                    self.panelA.image = image
                    self.panelA.pack(side="left", padx=10, pady=10)
                    self.panelB = Label(image=image)
                    self.panelB.image = image
                    self.panelB.pack(side="right", padx=10, pady=10)
                    self.erosionBtn['state'] = tkinter.NORMAL
                    self.dilatationBtn['state'] = tkinter.NORMAL
                    self.highFreqFilterBtn1['state'] = tkinter.NORMAL
                    self.highFreqFilterBtn2['state'] = tkinter.NORMAL
                    self.breakingBtn['state'] = tkinter.NORMAL
                    self.closureBtn['state'] = tkinter.NORMAL
                else:
                    self.panelA.configure(image=image)
                    self.panelB.configure(image=image)
                    self.panelA.image = image
                    self.panelB.image = image

        options = ["square", "cross"]
        formChoice = StringVar(self.root)
        formChoice.set(options[0])

        # GUI Builder
        self.f_choice = Frame(self.root)
        self.dilatationBtn = Button(self.root, text="Dilatation", command=dilatation)
        self.erosionBtn = Button(self.root, text="Erosion", command=erosion)
        self.breakingBtn = Button(self.root, text="Breaking", command=breaking)
        self.closureBtn = Button(self.root, text="Closure", command=closure)
        self.highFreqFilterBtn1 = Button(self.root, text="High-frequency filter 1", command=highFrequencyFilter1)
        self.highFreqFilterBtn2 = Button(self.root, text="High-frequency filter 2", command=highFrequencyFilter2)
        self.chooseImgBtn = Button(self.root, text="Select an image", command=select_image)
        self.formMenu = OptionMenu(self.f_choice, formChoice, *options)
        self.spinbox = Spinbox(self.f_choice, from_=3, to=19, increment=2, width=50)
        self.chooseImgBtn.pack(expand=1, fill=X, side=TOP)
        self.f_choice.pack()
        self.formMenu.pack(expand=1, fill=X, side=LEFT)
        self.spinbox.pack(expand=1, fill=X, side=RIGHT)
        self.erosionBtn.pack(expand=1, fill=X, side=TOP)
        self.dilatationBtn.pack(expand=1, fill=X, side=TOP)
        self.breakingBtn.pack(expand=1, fill=X, side=TOP)
        self.closureBtn.pack(expand=1, fill=X, side=TOP)
        self.highFreqFilterBtn1.pack(expand=1, fill=X, side=TOP)
        self.highFreqFilterBtn2.pack(expand=1, fill=X, side=TOP)
        if self.panelA is None:
            self.erosionBtn['state'] = tkinter.DISABLED
            self.dilatationBtn['state'] = tkinter.DISABLED
            self.highFreqFilterBtn1['state'] = tkinter.DISABLED
            self.highFreqFilterBtn2['state'] = tkinter.DISABLED
            self.breakingBtn['state'] = tkinter.DISABLED
            self.closureBtn['state'] = tkinter.DISABLED
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.root.title("Lab3")
    app.root.mainloop()
