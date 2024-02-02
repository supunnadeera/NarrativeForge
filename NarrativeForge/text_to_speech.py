import os
from openai import OpenAI

class TextToSpeech:
    def __init__(self):
        self.client = OpenAI()

    def generate_speech(self, text, path, voice):
        """
        Generate speech from text and save it to a file.

        Parameters:
        - text (str): The input text for speech generation.
        - path (str): The path to save the generated speech file.
        - method (int, optional): The method of speech generation (0 for OpenAI, 1 for gTTS).

        Raises:
        - ValueError: If an unsupported method is provided.
        - Exception: If there is an error during speech generation.
        """

        try:
            response = self.client.audio.speech.create(
                model="tts-1",
                voice=voice,
                input=text,
            )
            response.write_to_file(path)
        except Exception as e:
            raise Exception(f"Error generating OpenAI speech: {str(e)}")


# Instantiate the class for use in other modules
text_to_speech_instance = TextToSpeech()
