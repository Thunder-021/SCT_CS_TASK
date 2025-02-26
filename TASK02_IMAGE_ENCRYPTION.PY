from PIL import Image
import numpy as np


def swap_pixels(image):
    pixels = np.array(image)
   
    pixels[0, 0], pixels[1, 1] = pixels[1, 1], pixels[0, 0]
    return Image.fromarray(pixels)


def apply_operation(image, operation='add', value=50):
    pixels = np.array(image)
    if operation == 'add':
        pixels = np.clip(pixels + value, 0, 255)  
    elif operation == 'multiply':
        pixels = np.clip(pixels * value, 0, 255)  
    return Image.fromarray(pixels)

# Function to show the image
def show_image(image):
    image.show()


image_path = 'image.png' 
image = Image.open(image_path)


image_swapped = swap_pixels(image)
show_image(image_swapped)

image_transformed = apply_operation(image, operation='add', value=50)
show_image(image_transformed) 

image_transformed = apply_operation(image, operation='multiply', value=2)
show_image(image_transformed)  