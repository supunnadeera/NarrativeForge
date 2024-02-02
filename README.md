# NarrativeForge

NarrativeForge is a Python package that enhances videos by adding text and synthesized speech over a background video. It's designed to simplify the process of creating engaging videos with customizable text and voice narration.

## Features

- Add text and synthesized speech to background videos.
- Customize font, color, and other text parameters.
- Easily integrate into existing video editing workflows.

## Installation

You can install NarrativeForge using pip:

```bash
pip install NarrativeForge
```

Additionally, you need to set up your OpenAI API key. Obtain your API key by following the instructions on the OpenAI website. Once you have the API key, you can set it as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Make sure to replace "your-api-key-here" with your actual OpenAI API key.

You need to install [ImageMagick](https://imagemagick.org/script/download.php), make sure to add imagemagick path to the moviepy configfile if you are on windows.

## Usage

use in command line as

```bash
NarrativeForge -i "input.mp4" -t "Hello, World!, Enhance your videos with NarrativeForge"
```

or on a python file as

```python
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

```

Replace input_video.mp4 with the path to your input video and customize the texts list accordingly. The enhanced video will be saved as output_video.mp4.

## Configuration

You can customize various parameters using the generate_video function. Refer to the function signature and documentation for options.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.
