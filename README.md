# Calculate-Frame-Difference

## Overview
This script processes a dataset of images to retain only unique frames based on a specified threshold. It is useful for filtering out redundant frames in datasets where consecutive images have minimal differences.

## Features
- Reads image paths from `list.txt`.
- Computes the pixel-wise absolute difference between consecutive frames.
- Saves only unique frames based on a user-defined threshold.
- Outputs a text file with paths to unique frames.

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies:

```bash
pip install opencv-python numpy tqdm
```

## Usage
### Command-line Arguments
```bash
python frame_difference.py <root_path> <output_folder> --threshold <value>
```

### Parameters:
- `root_path` (str): Path to the directory containing `list.txt` and an `images` folder.
- `output_folder` (str): Directory where unique frames will be saved.
- `--threshold` (float, optional): Difference threshold for frame uniqueness (default: 0.05).

### Example:
```bash
python frame_difference.py /path/to/dataset /path/to/output --threshold 0.05
```

## Explanation of the Code
1. **Parsing Arguments:** The script starts by parsing command-line arguments using `argparse`. It takes the root path, output folder, and an optional threshold as inputs.
2. **Setting Up Paths:** The `list.txt` file inside the root path is read to get a list of image paths.
3. **Processing Images:**
   - Each image is read using `cv2.imread()`.
   - The script compares each frame to the previous one using `cv2.absdiff()` to compute the mean pixel-wise absolute difference.
   - If the difference is greater than the specified threshold, the frame is considered unique.
4. **Saving Unique Frames:**
   - Unique frames are saved in the output folder with sequential names (`unique_00000.jpg`, etc.).
   - A `unique_frames.txt` file is created to store paths of saved frames.
5. **Handling Errors:**
   - If an image cannot be read, the script prints a warning and skips it.
   - The first frame is always saved by default.

## Output
- Unique frames saved in the specified output folder.
- A `unique_frames.txt` file listing the paths of saved unique frames.

## Notes
- The script skips unreadable or missing images with a warning.
- The first frame is always saved.

## License
This project is open-source and available under the [MIT License](LICENSE).
