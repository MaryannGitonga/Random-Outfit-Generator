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

        # collecting all clothes and shoes
        self.top_images = ALL_TOPS
        self.bottom_images = ALL_BOTTOMS
        self.shoes_images = ALL_SHOES

        # first pictures for top, bottom and shoes
        self.tops_image_path = self.top_images[0]
        self.bottoms_image_path = self.bottom_images[0]
        self.shoes_image_path = self.shoes_images[0]

        # creating 3 frames
        self.tops_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)
        self.bottoms_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)
        self.shoes_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)

        # adding top
        self.top_image_label = self.create_photo(self.tops_image_path, self.tops_frame)
        self.top_image_label.pack(side=tk.TOP)

        # adding bottom
        self.bottom_image_label = self.create_photo(self.bottoms_image_path, self.bottoms_frame)
        self.bottom_image_label.pack(side=tk.TOP)

        # adding shoe
        self.shoe_image_label = self.create_photo(self.shoes_image_path, self.shoes_frame)
        self.shoe_image_label.pack(side=tk.TOP)

        # create background
        self.create_background()

    def create_background(self):
        # add title to window and change the size
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

        # create buttons
        self.create_buttons()

        # add the initial clothes onto the screen
        self.tops_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.bottoms_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.shoes_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_buttons(self):
        top_prev_button = tk.Button(self.tops_frame, text="Prev", command=self.get_prev_top)
        top_prev_button.pack(side=tk.LEFT)

        create_outfit_button = tk.Button(self.tops_frame, text="Create Outfit", command=self.create_outfit)
        create_outfit_button.pack(side=tk.LEFT)

        top_next_button = tk.Button(self.tops_frame, text="Next", command=self.get_next_top)
        top_next_button.pack(side=tk.RIGHT)

        bottom_prev_button = tk.Button(self.bottoms_frame, text="Prev", command=self.get_prev_bottom)
        bottom_prev_button.pack(side=tk.LEFT)

        bottom_next_button = tk.Button(self.bottoms_frame, text="Next", command=self.get_next_bottom)
        bottom_next_button.pack(side=tk.RIGHT)

        shoe_prev_button = tk.Button(self.shoes_frame, text="Prev", command=self.get_prev_shoe)
        shoe_prev_button.pack(side=tk.LEFT)

        shoe_next_button = tk.Button(self.shoes_frame, text="Next", command=self.get_next_shoe)
        shoe_next_button.pack(side=tk.RIGHT)

    def create_photo(self, image, frame):
        top_image_file = Image.open(image)
        image = top_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo, anchor=tk.CENTER)
        image_label.image = photo

        return image_label



if __name__ == '__main__':
    root = tk.Tk()
    app = MyOutfitGenerator(root)
    root.mainloop()