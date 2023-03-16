# -- Configurations for the Transcriptor module
import torch
config = dict()

# -------------- General configs ------------#
config["samplerate"] = 16000
config["language"] = "en"
config["gpu"] = False
config["progress_bar"] = False
config["cuda_device"] = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
config["local_flag"] = True 
config["tts_type"] = "ConquiYourTTS" 


# -------------- Hubert ASR configs ------------#
if config["tts_type"] == "ConquiYourTTS": 
    config["tts"] = dict()
    config["tts"]["model_repo_path"] =   "tts_models/multilingual/multi-dataset/your_tts"   
    config["tts"]["language"] = config["language"]
    config["tts"]["gpu"] = config["gpu"] 
    config["tts"]["progress_bar"] = config["progress_bar"] 
    config["tts"]["output_speaker"] = "/home/ali/Desktop/idrak_work/tts/referenec_audios/speaker_1.wav"