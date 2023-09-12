"""
This script, `video_eval_helpers.py`, is designed to assist in the evaluation of video results by combining two videos side by side into a single video. 
This can be particularly useful for comparing different video processing techniques or visualizing changes over time in a video dataset.

The script contains a single function `combine_videos` which performs the following operations:
1. Opens two video files specified by their paths.
2. Retrieves the properties of the first video (FPS, width, and height) to set up the output video parameters.
3. Creates a VideoWriter object to save the output video with the combined width of the two videos and the height of the first video.
4. Iterates through the frames of both videos, adding a text overlay to each frame indicating the video name, and combines the frames side by side.
5. Writes the combined frame to the output video.
6. Releases the resources once all frames have been processed.

Attributes:
    video1_name (str): The name of the first video file.
    video2_name (str): The name of the second video file.
    video1_path (str): The file path to the first video.
    video2_path (str): The file path to the second video.
    output_path (str): The file path where the combined video will be saved.

Usage:
    The script is executed directly. The video file paths and output path are specified at the bottom of the script, 
    and the `combine_videos` function is called with these paths as arguments.

Example:
    video1_name = "video1.mp4"
    video2_name = "video2.mp4"
    video1_path = "/path/to/video1.mp4"
    video2_path = "/path/to/video2.mp4"
    output_path = "/path/to/output.mp4"
    
    combine_videos(video1_path, video2_path, output_path)
"""

import cv2


def combine_videos(video1_path, video2_path, output_path):
    # Open the first video file
    video1 = cv2.VideoCapture(video1_path)
    success1, frame1 = video1.read()

    # Open the second video file
    video2 = cv2.VideoCapture(video2_path)
    success2, frame2 = video2.read()

    # Get video properties
    fps = video1.get(cv2.CAP_PROP_FPS)
    width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a VideoWriter object to save the output video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output = cv2.VideoWriter(output_path, fourcc, fps, (2 * width, height))

    # Loop through the frames and combine them side by side
    frame_count = 0
    while success1 and success2:
        # Add text overlay to the top left corner of video 1 frame
        cv2.putText(frame1, video1_name, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Add text overlay to the top left corner of video 2 frame
        cv2.putText(frame2, video2_name, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        combined_frame = cv2.hconcat([frame1, frame2])
        output.write(combined_frame)

        # Read the next frames
        success1, frame1 = video1.read()
        success2, frame2 = video2.read()

        frame_count += 1

    # Release the resources
    video1.release()
    video2.release()
    output.release()

    print("Combined video created successfully!")


# Usage
video1_name = "cutting_tissues_twice_fixidentity_100000_rgb.mp4"
video2_name = "cutting_tissues_twice_HITNet_StereoNet_plain_fixidentity_100000_rgb.mp4"
video1_path = f"/dhc/home/ennio.strohauer/EndoNeRF/logs/cutting_tissues_twice/{video1_name}"
video2_path = f"/dhc/home/ennio.strohauer/EndoNeRF/logs/cutting_tissues_twice_HITNet_StereoNet_plain/{video2_name}"
output_path = "/dhc/home/ennio.strohauer/EndoNeRF/video_comparisons/StereoNet_holefilling_sub100_vs_plain.mp4"

combine_videos(video1_path, video2_path, output_path)
