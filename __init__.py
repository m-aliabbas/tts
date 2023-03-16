from tts_config import config
from Narrator import Narrator
import sounddevice as sd
nr = Narrator(**config)
wave = nr.get_audio_array("Hello How are you? I am Fine . Are you okay?")
sd.play(wave, samplerate=16000)
sd.wait()
del nr