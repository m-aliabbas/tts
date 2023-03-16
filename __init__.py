from tts_config import config
from Narrator import Narrator
nr = Narrator(**config)
nr.get_audio_array("Ali is good Bot")