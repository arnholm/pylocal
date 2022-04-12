#ui.py
from tkinter import filedialog
from tkinter import Tk
def get_image_file():
    Tk().withdraw()
    filename =  filedialog.askopenfilename(title = "Select file",filetypes = [("jpeg files","*.jpg")])
    return filename