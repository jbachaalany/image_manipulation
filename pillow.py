from PIL import Image
import os

def images():
    # Loop through each image in the folder
    for image in os.listdir(image_path):
        # check if the image ends with jpg
        if image.endswith(".jpg"):
            # display
            print(image)
            update_image(image)

def update_image(image):
    # Open the image
    img = Image.open(os.path.join(image_path,image))
    # Change image resolution and rotate 180 degrees
    new_img = img.resize((192, 192)).rotate(180,expand=True).convert('RGB')
    # Change format from .jpg to .png and Save image
    new_img.save(os.path.join(updated_image_path,image[:-4]+".png"))
    print(f"Name: {image[:-4]}.png | Size: {new_img.size}")

if __name__ == '__main__':
    image_path= os.path.join(os.getcwd(),"stock_images")
    updated_image_path = os.path.join(os.getcwd(),"updated_images") 
    images()