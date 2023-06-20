import cv2


def combine_videos(video1_path, video2_path, output_path, loop_count):
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
    while success1 and success2 and frame_count < loop_count * video1.get(cv2.CAP_PROP_FRAME_COUNT):
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
video2_name = "cutting_tissues_twice_HITNet_fixidentity_100000_rgb.mp4"
video1_path = f"/dhc/home/ennio.strohauer/EndoNeRF/logs/cutting_tissues_twice/{video1_name}"
video2_path = f"/dhc/home/ennio.strohauer/EndoNeRF/logs/cutting_tissues_twice_HITNet/{video2_name}"
output_path = "/dhc/home/ennio.strohauer/EndoNeRF/video_comparisons/base_vs_TinyHITNet.mp4"
loop_count = 3

combine_videos(video1_path, video2_path, output_path, loop_count)
