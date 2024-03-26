#Just a  bulk renamer :)

from PIL import Image
import os

folder_n_file_name = "brake"

def crop_resize_and_rename_images(new_width, new_height):
    # Create output folder if it doesn't exist
    output_folder = folder_n_file_name
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all image files in the current directory
    files = [file for file in os.listdir() if file.endswith(('.png', '.jpg', '.jpeg'))]

    for idx, file in enumerate(files, 1):
        # Open image
        img = Image.open(file)
        
        # Crop from the top
        width, height = img.size
        top_crop = 350  # Adjust this value to change how much to crop from the top
        img = img.crop((0, top_crop, width, height))

        # Resize image
        img = img.resize((new_width, new_height))

        # Generate new filename
        new_filename = f"{folder_n_file_name}_{idx}{os.path.splitext(file)[1]}"

        # Save resized image to output folder
        img.save(os.path.join(output_folder, new_filename))

    print("Done men.")

if __name__ == "__main__":
    new_width = 480  # New width in pixels
    new_height = 270  # New height in pixels

    crop_resize_and_rename_images(new_width, new_height)
