import os
from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip, AudioFileClip
from .text_to_speech import text_to_speech_instance
from NarrativeForge.speech_to_text import speech_to_text_instance


class TextToVideo:
    def __init__(self):
        self.audio_file = "test.mp3"
        self.fps = 30
    
    def _create_text_clips(self, segments, caption_size, text_clip_params):
        txt_clips = []

        for segment in segments:
            text = segment["text"]
            start = segment["start"]
            end = segment["end"]
            duration = end - start

            default_params = {
                "font": "Impact",
                "fontsize": 150,
                "color": "white",
                "stroke_color": "black",
                "stroke_width": 5,
                "bg_color": "transparent",
                "size": (caption_size, None),
                "method": "caption",
                "align": "center",
                "interline": -15,
            }

            merged_params = default_params.copy()
            merged_params.update(text_clip_params or {})

            txt_clip = TextClip(text, **merged_params)
            txt_clip = (
                txt_clip.set_pos("center").set_duration(duration).set_start(start)
            )
            txt_clips.append(txt_clip)

        return txt_clips

    def show_available_fonts(self):
        print(TextClip.list("font"))

    def show_available_colors(self):
        print(TextClip.list("color"))

    def generate_video(
        self,
        input_filename,
        texts,
        voice="shimmer",
        output_filename="output.mp4",
        caption_padding=100,
        text_clip_params=None,
    ):
        """
        Generate a video with text overlays.

        Parameters:
        - input_filename (str): Path to the input video file.
        - texts (List[str]): List of texts to overlay on the video.
        - output_filename (str): Path for the output video file (default is 'output.mp4').
        - voice (str): The voice to use for speech generation (available: shimmer(default), nova, onyx, fable, echo, alloy ).
        - caption_padding (int): Padding for the captions (default is 100).
        - text_clip_params (Optional[Dict[str, any]]): Additional parameters for MoviePy TextClip.
        Returns:
        - None
        """
        text_to_speech_instance.generate_speech(texts, self.audio_file, voice=voice)
        segmented_texts = speech_to_text_instance.generate_text(self.audio_file)
        clip_duration = segmented_texts[-1]["end"]

        clip = VideoFileClip(os.path.join(os.getcwd(), input_filename))
        clip = clip.without_audio()
        clip = clip.subclip(0, clip_duration)
        audio_clip = AudioFileClip(os.path.join(os.getcwd(), self.audio_file))

        caption_size = clip.size[1] - caption_padding
        txt_clips = self._create_text_clips(
            segmented_texts, caption_size, text_clip_params
        )
        video = CompositeVideoClip([clip.set_audio(audio_clip)] + txt_clips)
        video.write_videofile(
            os.path.join(os.getcwd(), output_filename), fps=self.fps, codec="libx264"
        )


text_to_video_instance = TextToVideo()
