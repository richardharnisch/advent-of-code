import sys
import os
from copy import deepcopy
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 2

frames = []


def create_frame(grid, iteration, total_removed):
    """Create a video frame from the grid state"""
    cell_size = 5
    height = len(grid)
    width = len(grid[0]) if grid else 0

    # Add space for text at bottom (30 pixels)
    text_height = 30
    img_width = width * cell_size
    img_height = height * cell_size + text_height

    # Ensure dimensions are even for H.264 encoding
    if img_width % 2 == 1:
        img_width += 1
    if img_height % 2 == 1:
        img_height += 1

    img = Image.new("RGB", (img_width, img_height), color="white")
    draw = ImageDraw.Draw(img)

    # Draw grid
    for i in range(height):
        for j in range(len(grid[i])):
            x = j * cell_size
            y = i * cell_size
            color = "black" if grid[i][j] == "@" else "white"
            draw.rectangle([x, y, x + cell_size - 1, y + cell_size - 1], fill=color)

    # Draw text at bottom
    text = f"Iteration: {iteration} | Removed: {total_removed}"
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    except:
        font = ImageFont.load_default()

    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (img_width - text_width) // 2
    text_y = height * cell_size + 5

    draw.text((text_x, text_y), text, fill="black", font=font)

    return img


input = sys.stdin.read().strip().split("\n")
input = [list(row) for row in input]
output = 0


def remove_rolls(input, iteration, total_removed):
    input_copy = deepcopy(input)
    removed_rolls = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if (
                input[i][j] == "@"
                and count_nested(
                    get_neighborhood(input, (i, j), use_diagonal=True), "@"
                )
                < 5
            ):
                removed_rolls += 1
                input_copy[i][j] = "."
                if DEBUG >= 2:
                    frames.append(
                        create_frame(
                            input_copy, iteration, total_removed + removed_rolls
                        )
                    )
                if DEBUG:
                    print("x", end="")
            elif DEBUG:
                print(input[i][j], end="")
        if DEBUG:
            print("\n", end="")
    return removed_rolls, input_copy


if DEBUG >= 2:
    frames.append(create_frame(input, 0, 0))

iteration = 1
while True:
    if DEBUG:
        print(f"=== Iteration {iteration} ===")
    previous_output = output
    removed, input = remove_rolls(input, iteration, output)
    output += removed
    iteration += 1
    if previous_output == output:
        break

if DEBUG >= 2 and frames:
    import subprocess
    import tempfile

    # Add last frame 50 times to hold for 1 second (at 50 fps)
    last_frame = frames[-1]
    for _ in range(50):
        frames.append(last_frame)

    # Save frames as temporary PNG files
    temp_dir = tempfile.mkdtemp()
    for i, frame in enumerate(frames):
        frame.save(os.path.join(temp_dir, f"frame_{i:05d}.png"))

    # Create MP4 using ffmpeg at 50 fps (50x faster than 1 fps)
    output_path = os.path.join(os.path.dirname(__file__), "output.mp4")
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-framerate",
            "50",
            "-i",
            os.path.join(temp_dir, "frame_%05d.png"),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            output_path,
        ],
        check=True,
    )

    # Clean up temporary files
    import shutil

    shutil.rmtree(temp_dir)

    print(f"Video saved to {output_path}")

print(output)
