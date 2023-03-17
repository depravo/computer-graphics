import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

class App:

    def __init__(self):
        super().__init__()

        def show_files_info():
            directory = os.fsencode(self.filepath)
            for item in self.tree.get_children():
                self.tree.delete(item)
            for file in os.listdir(directory):
                filename = os.fsdecode(file)
                if filename.endswith(".jpg") \
                        or filename.endswith(".gif") \
                        or filename.endswith(".tif") \
                        or filename.endswith(".bmp") \
                        or filename.endswith(".png") \
                        or filename.endswith(".pcx") \
                        or filename.endswith(".BMP"):
                    im = Image.open(self.filepath + "/" + filename)
                    width, height = im.size
                    size = width * height

                    res = im.info.get('dpi')

                    mode_to_bpp = {'1': 1, 'L': 8, 'P': 8, 'RGB': 24, 'RGBA': 32, 'CMYK': 32, 'YCbCr': 24, 'I': 32, 'F': 32}
                    color_depth = mode_to_bpp[im.mode]

                    comp = im.info.get('compression')

                    self.tree.insert("", "end", values=(filename, size, res, color_depth, comp))

        self.root = tk.Tk()
        self.gridframe = tk.Frame(self.root)
        for col in range(3):
            self.gridframe.columnconfigure(index=col, weight=1)
        for row in range(2):
            self.gridframe.rowconfigure(index=row, weight=1)

        self.filepath = ''

        self.label_cur_path = tk.Label(text="Example:")
        self.label_cur_path.grid(row=0, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky="NSW")

        self.label_path = tk.Label(text="D:\\Your path\\Yor Dir\\file.png")
        self.label_path.grid(row=0, column=1, ipadx=6, ipady=6, padx=4, pady=4, sticky="NS")

        def click_button():
            self.filepath = filedialog.askdirectory()
            self.label_cur_path.configure(text="Current path: ")
            self.label_path.configure(text=self.filepath)
            if self.filepath != '':
                show_files_info()
            else:
                messagebox.showerror(title="Error", message="Directory path is empty! Try again.")

        btn = ttk.Button(text="Choose directory", command=click_button)
        btn.grid(row=0, column=2, ipadx=6, ipady=6, padx=4, pady=4, sticky="NSE")

        s = ttk.Style()
        s.configure('Treeview', rowheight=25)

        columns = ("file_name", "image_size", "resolution", "color_depth", "compression")
        self.tree = ttk.Treeview(columns=columns, show="headings", style='Treeview')
        self.tree.grid(row=1, column=0, columnspan=3, ipadx=6, ipady=6, padx=4, pady=4, sticky="NS")

        self.tree.heading("file_name", text="File name")
        self.tree.heading("image_size", text="Image size(pixels)")
        self.tree.heading("resolution", text="Resolution(dpi)")
        self.tree.heading("color_depth", text="Color depth")
        self.tree.heading("compression", text="Compression")

        self.files = [("Whale.jpg", "320000", "80 80", "24", "None"), ("Dog.png", "5778240", "300 300", "1", "None"), ("Rabbit.bmp", "192000", "100 100", "8", "0")]
        for f in self.files:
            self.tree.insert("", "end", values=f)

        scrollbar = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky="ns")

if __name__ == '__main__':
    app = App()
    app.root.title("Images metadata")
    app.root.mainloop()