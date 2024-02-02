from openai import OpenAI


class SpeechToText:
    def __init__(self):
        self.client = OpenAI()

    def generate_text(self, audio_file_path):
        """
        Generate text from an audio file.

        Parameters:
        - audio_file_path (str): The path to the audio file.

        Returns:
        - str: The generated text.

        Raises:
        - Exception: If there is an error during text generation.
        """
        try:
            audio_file = open(audio_file_path, "rb")
            response = self.client.audio.transcriptions.create(
                model="whisper-1", response_format="verbose_json", file=audio_file
            )
            return response.segments
        except Exception as e:
            raise Exception(f"Error generating text from audio: {str(e)}")


speech_to_text_instance = SpeechToText()
