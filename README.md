# Color Detection with OpenCV

This repository contains two Python scripts for real-time color detection using OpenCV. The project demonstrates different approaches to color detection and highlighting in video streams.

## Features

- Real-time color detection using webcam
- Multiple color detection capabilities
- HSV color space implementation
- Bounding box visualization
- Color highlighting functionality

## Scripts

### 1. Detect and Label Color (`detect_and_label_color.py`)

This script provides multi-color detection with bounding boxes and labels.

**Features:**
- Detects multiple colors simultaneously (Red, Green, Blue, Yellow)
- Draws bounding boxes around detected colors
- Labels each detected color in real-time
- Configurable color ranges using HSV color space

**Usage:**
```python
python detect_and_label_color.py
```
- Press 'q' to exit the program

### 2. Highlight Color in Frame (`highlight_color_in_frame.py`)

This script allows users to select and highlight a specific color in the video stream.

**Features:**
- Interactive color selection (Red, Blue, Green)
- Real-time color highlighting
- Shows both original and highlighted frames
- User-friendly command-line interface

**Usage:**
```python
python highlight_color_in_frame.py
```
- Choose a color by entering its corresponding number:
  1. Red
  2. Blue
  3. Green
- Press 'q' to exit the program

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
```

2. Install the required packages:
```bash
pip install opencv-python numpy
```

## How It Works

Both scripts use the HSV (Hue, Saturation, Value) color space for more accurate color detection. The process involves:

1. Converting BGR frame to HSV color space
2. Creating color masks using predefined HSV ranges
3. Applying the masks to detect specific colors
4. Processing and displaying the results

## Note

- Ensure your webcam is properly connected and accessible
- Lighting conditions may affect color detection accuracy
- HSV ranges can be adjusted for better detection in different environments

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for bugs or feature requests.
