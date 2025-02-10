# Program To Extract Frames from Video

import cv2
import os
from pathlib import Path

# Function to extract frames from video
def VideoToFrames(video_path, output_folder, fps=60):
    
    # Create output folder if it does not exist
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)
    
    # Open video file
    vidObj = cv2.VideoCapture(video_path)
    
    # Get video FPS and calculate frame interval
    video_fps = int(vidObj.get(cv2.CAP_PROP_FPS))
    frame_interval = max(1, video_fps // fps)
    
    count = 0
    frame_count = 0
    success = True
    
    while success:
        success, image = vidObj.read()
        
        if success and count % frame_interval == 0:
            frame_path = output_folder / f"frame{frame_count:05d}.jpg"
            cv2.imwrite(str(frame_path), image)
            frame_count += 1
        
        count += 1
    
    print(f"Extracted {frame_count} frames at {fps} FPS into {output_folder}")

# Driver Code
if __name__ == '__main__': 
    
    # Calling the function 
    VideoToFrames("C:\\path\\to\\video.mp4", "C:\\path\\to\\frames", fps=60)
