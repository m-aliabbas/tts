from TTS.api import TTS
from TTSInterface import TTSInterface
from utils import *
import numpy as np

class ConquiYourTTS(TTSInterface):
    """
    Implementation of TTSInterface using the ConquiYourTTS model.
    """

    def __init__(self, model_repo_path='tts_models/multilingual/multi-dataset/your_tts',
                 output_speaker='referenec_audios/speaker_1.wav', language='en', progress_bar=False, gpu=False,):
        """
        Initialize ConquiYourTTS model.

        Args:
            model_repo_path (str): Path to the directory containing the model files.
            output_speaker (str): Speaker ID to use for output audio.
            language (str): Language code for the text to synthesize.
            progress_bar (bool): Whether to display a progress bar during synthesis.
            gpu (bool): Whether to use GPU for synthesis.
        """
        super().__init__()
        self.model_repo_path = model_repo_path
        self.model = TTS(self.model_repo_path, progress_bar=progress_bar, gpu=gpu)
        self.output_speaker = output_speaker
        self.language = language

    def get_audio(self, text: str) -> np.ndarray:
        """
        Synthesize audio from input text.

        Args:
            text (str): Input text to synthesize.

        Returns:
            np.ndarray: Numpy array containing the synthesized audio waveform.
        """
        text = convert_to_words(text=text)
        print(self.output_speaker)
        wave = self.model.tts(text=text, speaker_wav=self.output_speaker, language=self.language)
        wave= np.array(wave, dtype=np.float32)
        return wave

