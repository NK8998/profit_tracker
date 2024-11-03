from tkinter import Label
from PIL import Image, ImageTk

def add_image_widget(parent, url, width=200, height=200, background="white"):
    original_image = Image.open(url)

    # Resize the image
    resized_image = original_image.resize((width, height))

    # Create PhotoImage from resized image
    img = ImageTk.PhotoImage(resized_image)

    # Create a Label widget to display the image
    label = Label(parent, image=img, background=background)
    label.image = img  # Keep a reference to avoid garbage collection

    return label  # Optionally return label if you need a reference

