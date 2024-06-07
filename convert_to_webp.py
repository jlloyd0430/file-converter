import os
from PIL import Image

# Specify the directory containing .png images
input_directory = './images'
output_directory = './webp'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate over all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.png'):
        # Open the image file
        with Image.open(os.path.join(input_directory, filename)) as img:
            # Convert the image to RGB mode (required for .webp)
            img = img.convert('RGB')
            # Define the output file path
            output_filepath = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.webp")
            # Save the image in .webp format
            img.save(output_filepath, 'webp')
            print(f"Converted {filename} to {output_filepath}")

print("All images have been converted to .webp format.")
