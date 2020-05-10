import os
import random

import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

WINDOW_TITLE = "My Random Outfit Generator "
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
IMG_HEIGHT = 200
IMG_WIDTH = 200
BEIGE_COLOR_HEX = '#986c5e'

# store all the clothes and shoes into an accessible file & skip hidden files
ALL_TOPS = [str("tops/") + file for file in os.listdir("tops/") if not file.startswith('.')]
ALL_BOTTOMS = [str("bottoms/") + file for file in os.listdir("bottoms/") if not file.startswith('.')]
ALL_SHOES = [str("shoes/") + file for file in os.listdir("shoes/") if not file.startswith('.')]



class MyOutfitGenerator:
    def __init__(self, root):
        self.root = root



if __name__ == '__main__':
    root = tk.Tk()
    app = MyOutfitGenerator(root)
    root.mainloop()