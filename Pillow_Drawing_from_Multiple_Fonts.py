import tkinter as tk
import os
from PIL import Image, ImageDraw, ImageFont, ImageTk
import textwrap

# Create a tkinter window
root = tk.Tk()

# Set the window size
root.geometry("1000x700")

# Create a blank image
img = Image.new("RGBA", (800, 600), (255, 255, 255, 0))

# Create a draw object
draw = ImageDraw.Draw(img)

# Choose a font size
font_size = 36

# Get the list of .ttf files in the "Fonts" directory
font_dir = "Fonts"
font_files = [os.path.join(font_dir, f) for f in os.listdir(font_dir) if f.endswith('.ttf')]


# Initialize the font index
font_index = 0

# Load the first font and draw the initial sample text
font_file = font_files[font_index]
try:
    font = ImageFont.truetype(font_file, font_size)
    sample_text = f"Hello World!\nFont: {font_file}"
    lines = textwrap.wrap(sample_text, width=20)
    y = 50
    for line in lines:
        text_bbox = draw.textbbox((50, y), line, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        draw.text((50, y), line, (0, 0, 0), font=font)
        y += text_height + 10
    # Update the image on the label
    img_tk = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img_tk)
    label.image = img_tk
    label.pack()
except OSError:
    print(f"Invalid font file: {font_file}")
    label = None


# Define a function to update the sample text with the next font
def update_text(delta):
    global font_index
    global label
    font_index = (font_index + delta) % len(font_files)
    font_file = font_files[font_index]
    try:
        # Load the font
        font = ImageFont.truetype(font_file, font_size)
        # Prepare the sample text with word wrap
        sample_text = f"Hello World!\nFont: {font_file}"
        lines = textwrap.wrap(sample_text, width=20)
        # Draw the sample text
        draw.rectangle((0, 0, img.width, img.height), fill=(255, 255, 255, 0))
        y = 50
        for line in lines:
            draw.text((50, y), line, (0, 0, 0), font=font)
            y += font.getsize(line)[1]
        # Update the image on the label
        img_tk = ImageTk.PhotoImage(img)
        if label:
            label.configure(image=img_tk)
            label.image = img_tk
        else:
            label = tk.Label(root, image=img_tk)
            label.image = img_tk
            label.pack()
    except OSError:
        print(f"Invalid font file: {font_file}")
        if label:
            label.destroy()
            label = None


# Create a "Previous Font" button
prev_button = tk.Button(root, text="Previous Font", command=lambda: update_text(-1))
prev_button.pack(side=tk.LEFT)

# Create a "Next Font" button
next_button = tk.Button(root, text="Next Font", command=lambda: update_text(1))
next_button.pack(side=tk.RIGHT)

# Start the GUI event loop
root.mainloop()
