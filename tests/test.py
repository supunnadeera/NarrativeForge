import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from NarrativeForge import TextToVideo

# Create an instance of TextToVideo
text_to_video_instance = TextToVideo()

# Specify input video, text, and output filename
input_filename = "input_video.mp4"
texts = "Hello, World!, Enhance your videos with NarrativeForge"
output_filename = "output_video.mp4"

# Generate the enhanced video
text_to_video_instance.generate_video(
    input_filename, texts, output_filename=output_filename, caption_padding=100
)