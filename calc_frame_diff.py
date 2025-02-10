import argparse
from pathlib import Path
import cv2
import numpy as np
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser(
        description="Preprocess dataset to retain unique frames based on a threshold."
    )
    parser.add_argument(
        "root_path",
        type=str,
        help="Root path containing 'list.txt' and 'images' folder.",
    )
    parser.add_argument(
        "output_folder",
        type=str,
        help="Folder to save unique frames.",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.05,
        help="Threshold for frame differences (default: 0.05).",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    
    # Paths
    list_path = Path(args.root_path).joinpath("list.txt")
    output_folder = Path(args.output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)  # Create folder if it doesn't exist
    unique_paths_file = output_folder.joinpath("unique_frames.txt")
    
    # Read the image paths from list.txt
    with open(list_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # Initialize variables
    prev_img = None
    unique_count = 0

    with open(unique_paths_file, "w") as unique_file:
        for line in tqdm(lines, total=len(lines)):
            img_path = Path(args.root_path).joinpath(line)
            img = cv2.imread(str(img_path))
            
            if img is None:
                print(f"Warning: Could not read image at {img_path}. Skipping.")
                continue

            # Check for uniqueness
            is_unique = False
            if prev_img is not None:
                # Calculate mean pixel-wise absolute difference
                diff = np.mean(cv2.absdiff(img, prev_img))
                if diff > args.threshold:  # Check if above threshold
                    is_unique = True
            else:
                # Always save the first frame
                is_unique = True

            if is_unique:
                # Save the frame
                unique_img_path = output_folder.joinpath(f"unique_{unique_count:05d}.jpg")
                cv2.imwrite(str(unique_img_path), img)
                
                # Save the path to the text file
                unique_file.write(str(unique_img_path) + "\n")
                unique_count += 1

            prev_img = img

    print(f"Unique frames saved: {unique_count}")
    print(f"Paths to unique frames saved in: {unique_paths_file}")


if __name__ == "__main__":
    main()
