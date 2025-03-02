import time
import tkinter as tk
from PIL import Image, ImageTk

def show_image(image_path, display_time, width=None, height=None):

    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Image Viewer")
    
    # Open and resize the image using PIL
    image = Image.open(image_path)

    if width and height:
        image = image.resize((width, height), Image.LANCZOS)
    
    photo = ImageTk.PhotoImage(image)
    
    # Add the image to a label widget
    label = tk.Label(window, image=photo)
    label.pack()

    # Schedule the window to close after display_time milliseconds
    window.after(display_time, window.destroy)

    # Run the Tkinter event loop
    window.mainloop()


def main():
    image_path = "Image.png"
    # Displaying parameters
    display_width = 1200  
    display_height = 700  
    interval = 20 * 60  # 20 minutes
    display_time = 20 * 1000  # 20 seconds

    try:
        while True:
            show_image(image_path, display_time, display_width, display_height)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Program is terminated.")


if __name__ == "__main__":
    main()