"""
This script is part of the generalization attempt in the EndoNeRF project, where it facilitates the creation of a `poses_bounds.npy` file, 
a necessary component of the dataset as per the framework requirements. The script calculates the near and far bounds from the depth maps of 
the images and combines them with camera parameters to create a matrix that is saved as `poses_bounds.npy`.

The script performs the following operations:
1. Retrieves the number of pictures in the specified path.
2. Calculates the near and far bounds for each image based on the depth maps.
3. Calculates the focal length in pixels using the given focal length in mm, sensor width in mm, and image width in pixels.
4. Constructs a matrix using the camera parameters (focal length, image width, and height) and the calculated near and far bounds.
5. Saves the constructed matrix as `poses_bounds.npy` in the specified path.

Functions:
    get_number_pictures(path: str) -> int:
        Retrieves and prints the number of pictures in the specified path.
    
    get_bounds_for_pictures(path: str) -> Tuple[np.ndarray, np.ndarray]:
        Calculates and returns the near and far bounds for each image in the specified path based on the depth maps.

Attributes:
    focal_length_mm (float): The focal length of the camera in millimeters.
    sensor_width_mm (float): The width of the camera sensor in millimeters.
    image_width_pixels (int): The width of the image in pixels.
    FOCAL (float): The calculated focal length in pixels.
    D (int): A constant used in the construction of the matrix.
    HEIGHT (int): The height of the images.
    WIDTH (int): The width of the images.
    path_to_pictures (str): The path to the picture data, specified as a command-line argument.

Usage:
    The script is executed directly with the `--path` argument specifying the path to the picture data.
    
    Example:
        python script_name.py --path "/path/to/picture/data"

Note:
    The calculation instructions for `poses_bounds.npy` can be found at:
    https://github.com/Fyusion/LLFF#using-your-own-poses-without-running-colmap
    The focal length is retrieved from the camera calibration data, and it is assumed that the x and y focal distances are the same in the EndoNeRF project.
"""


import configargparse
import cv2
import glob
import numpy as np
import os


def get_number_pictures(path):
    number_of_pictures = len(glob.glob(f"{path}/images/*.png"))
    print(f"Number of Pictures detected: {number_of_pictures}")
    return number_of_pictures


def get_bounds_for_pictures(path):
    near, far = [], []
    image_files = os.listdir(f"{path}/depth/")
    print("N_image_files", len(image_files))
    sorted_image_files = sorted(image_files)
    print("N_sorted", len(sorted_image_files))
    for image_file in sorted_image_files:
        image_path = os.path.join(f"{path}/depth/", image_file)
        print("image_path", image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image_near = np.min(image)
        image_far = np.max(image)
        print("near,far", image_near, image_far)
        near = np.append(near, image_near)
        far = np.append(far, image_far)

    return near, far


""" 
The poses_bounds.npy calculation instructions can be found here https://github.com/Fyusion/LLFF#using-your-own-poses-without-running-colmap

The focal length is retrieved from the camera_calibration.txt for the left camera 
(Camera-0-F: 1080.36 1080.18 // left camera x,y focal dist in pixels) taking the mean from the x,y focal dist.
in EndoNeRF they assume that x,y dist is the same
"""
focal_length_mm = 77
sensor_width_mm = 3.4
image_width_pixels = 1080

focal_length_pixels = (focal_length_mm / sensor_width_mm) * image_width_pixels
print(focal_length_pixels)

FOCAL = focal_length_pixels
D = 17
HEIGHT = 1080
WIDTH = 1080
# FOCAL = 1080.27
# HEIGHT = 1024
# WIDTH = 1280

parser = configargparse.ArgumentParser()
parser.add_argument('--path', help='picture data path', required=True)
args = parser.parse_args()

# "/dhc/home/ennio.strohauer/endonerf_sample_datasets/human_transform"
path_to_pictures = args.path
number_pictures = get_number_pictures(path_to_pictures)

result = np.empty((number_pictures, D))

identity_matrix = np.eye(3, 4)
camera_vector = np.array([WIDTH, HEIGHT, FOCAL]).reshape(-1, 1)

matrix = np.concatenate((identity_matrix, camera_vector), axis=1)
flat = matrix.flatten()

# I checked that they use the min/max values from their depth maps as near/far bounds
near, far = get_bounds_for_pictures(path_to_pictures)

for n in range(number_pictures):
    result_vector = np.append(flat, [near[n], far[n]])
    result = np.vstack((result, result_vector))

np.save(f"{path_to_pictures}/poses_bounds.npy", result)
print(f"poses_bounds.npy saved to {path_to_pictures}")
