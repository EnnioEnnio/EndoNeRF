"""
This script is designed to generate a specified number of black images, which will serve as non-existent tool masks for datasets derived from non-surgical videos. 
Originally, the datasets contained binary tool masks corresponding to surgical tools present in the images. 
However, as it is planned that the project is generalizing to include videos not from endoscopic surgeries, these tool masks are no longer necessary, 
hence the creation of black images to replace them.

The script contains a function `create_black_images` which performs the following operations:
1. Checks if the specified output directory exists, and creates it if not.
2. Generates a black image with specified width and height.
3. Saves the specified number of black images to the output directory with a standardized naming convention.

Attributes:
    output_folder (str): The directory path where the generated black images will be saved.
    total_images (int): The total number of black images to generate. Defaults to 156.
    width (int): The width of the generated black images. Defaults to 1080.
    height (int): The height of the generated black images. Defaults to 1080.

Usage:
    The script can be executed directly. To use the `create_black_images` function, 
    uncomment the function call at the bottom of the script and specify the appropriate output folder path.

Example:
    create_black_images(
        output_folder="/path/to/output/folder",
        total_images=156,
        width=1080,
        height=1080
    )
"""

import cv2
import os
import numpy as np


def create_black_images(output_folder, total_images=156, width=1080, height=1080):
    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Black image
    black_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Save the images
    for i in range(total_images):
        # file_name = os.path.join(output_folder, f"frame-{i:06d}.mask.png")
        file_name = os.path.join(output_folder, f"{i:06d}.png")

        cv2.imwrite(file_name, black_image)
    print(f"Generated {total_images} black images in {output_folder}")


# Call the method
# create_black_images(
#     output_folder="/dhc/home/ennio.strohauer/endonerf_sample_datasets/human_transform/masks")
create_black_images(
    output_folder="/dhc/home/ennio.strohauer/endonerf_sample_datasets/human_transform/gt_masks")
