import numpy as np

class TTSInterface:
    """
    Interface for implementing an ASR
    """

    def get_audio(self, text: str, **kwargs):
        """
        It get a text string and make audio of it.

        return: numpy_array
        """
    