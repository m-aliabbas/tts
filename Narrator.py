from ConquiYourTTS import ConquiYourTTS


class Narrator:
    """
    A class that generates synthesized audio from input text using various TTS models.
    """

    def __init__(self, **kwargs):
        """
        Initialize Narrator object with a TTS model.

        Args:
            **kwargs: Keyword arguments specifying the TTS model to use and its parameters.
        """
        self.tts_object = self.get_tts(kwargs["tts_type"], **kwargs["tts"])

    def get_tts(self, tts_type, **kwargs):
        """
        Load a TTS model based on its type and parameters.

        Args:
            tts_type (str): The type of TTS model to load.
            **kwargs: Keyword arguments specifying the parameters for the TTS model.

        Returns:
            TTSInterface: An instance of the TTS model specified by `tts_type`.
        """
        print(kwargs)
        if tts_type == "ConquiYourTTS":
            return ConquiYourTTS(**kwargs)
        else:
            print("[ERROR]: TTS type not recognized")
            return None

    def get_audio_array(self, text=""):
        """
        Synthesize audio from input text.

        Args:
            text (str): Input text to synthesize.

        Returns:
            np.ndarray: Numpy array containing the synthesized audio waveform.
        """
        return self.tts_object.get_audio(text=text)
