import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Create a tkinter window
root = tk.Tk()

# Create a blank image
img = Image.new("RGBA", (1000, 700), (255, 255, 255, 0))

# Create a draw object
draw = ImageDraw.Draw(img)

# Choose a font and specify its size
font = ImageFont.truetype("arial.ttf", 36)

# Draw some text
text = "Hello World! 987-654/321|0.0.0.0"
draw.text((50, 50), text, (0, 0, 0), font=font)

# Save the image
img.save("Sample_Saved_Image.png")

# Display the Image
#img.show()


# Load the image
img = Image.open("Sample_Saved_Image.png")

# Convert the image to a PhotoImage object
img = ImageTk.PhotoImage(img)



# Create a label to display the image
label = tk.Label(root, image=img)
label.image = img
label.pack()

# Start the GUI event loop
root.mainloop()