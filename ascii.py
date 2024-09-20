from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import scrolledtext

def get_image_brightness(imagePath):
    # Open the image file
    with Image.open(imagePath) as img:
        # Convert the image to grayscale
        grayscale_img = img.convert('L')
        
        # Convert the grayscale image to a numpy array
        pixel_values = np.array(grayscale_img)
        
        # Get image dimensions
        width, height = img.size
        
        # Create a list of pixel brightness values
        brightnessList = pixel_values.flatten().tolist()
        
        return brightnessList, width, height

def convert_brightness_to_art(brightnessList, threshold=90):
    # Convert brightness values to art representation
    return ["0" if int(each) > threshold else "1" for each in brightnessList]

def display_art_in_window(art, width):
    # Create a Tkinter window
    root = tk.Tk()
    root.title("ASCII Art")
    
    # Create a scrolled text widget with a very small font size
    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 4))
    text_widget.pack(expand=True, fill='both')
    
    # Format the art into lines of the specified width
    formatted_art = '\n'.join(''.join(art[i:i + width]) for i in range(0, len(art), width))
    
    # Insert formatted art into the text widget
    text_widget.insert(tk.END, formatted_art)
    
    # Run the Tkinter main loop
    root.mainloop()

def main():
    # Path to the image file
    imagePath = "OIP.jpg"
    try:
        # Get the brightness list, width, and height
        brightnessList, width, height = get_image_brightness(imagePath)
        
        # Convert brightness values to art representation
        art = convert_brightness_to_art(brightnessList)
        
        # Display the art in a window
        display_art_in_window(art, width)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
