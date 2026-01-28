import torch
from transformers import pipeline
import soundfile as sf

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

speaker_embedding = torch.zeros((1, 512))

speech = synthesiser(
    "hii, how are you doing? are you doing fine?",
    forward_params={"speaker_embeddings": speaker_embedding}
)
sf.write("speech.wav", speech["audio"], speech["sampling_rate"])
from IPython.display import Audio, display

display(Audio("speech.wav"))
