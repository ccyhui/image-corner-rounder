from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

class ImageCornerRounder:
    def __init__(self, radius = 50):
        self.radius = radius
        self.image = None
        self.path = None

    def input_image(self):
        self.path = filedialog.askopenfilename(title = "Input Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        self.image = Image.open(self.path)
        message = "Image imported successfully"
        messagebox.showinfo(title = "Selected File", message = message)

    def run(self):
        mask = Image.new("L", self.image.size)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle(((0, 0), self.image.size), self.radius, fill = 255)
        self.image.putalpha(mask)
        directory_path = os.path.dirname(self.path)
        save_name = "rounded.png"
        save_path = os.path.join(directory_path, save_name)
        self.image.save(save_path, "PNG")
        message = "Rounded corner image saved successfully"
        messagebox.showinfo(title = "Selected File", message = message)
        root.destroy()


rounder = ImageCornerRounder(radius = 50)

root = tk.Tk()
root.title("Image Corner Rounder")
root.resizable(False, False)
root.geometry("300x150")

input_button = tk.Button(root, text = "Input Image", command = rounder.input_image)
run_button = tk.Button(root, text = "Run", command = rounder.run)

input_button.pack(expand = True)
run_button.pack(expand = True)

root.mainloop()