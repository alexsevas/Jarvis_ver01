
import os
import time
import speech_recognition as sr
from faster_whisper import WhisperModel

wake_word = 'Jarvis'

num_cores = os.cpu_count()
whisper_size = 'large'
whisper_model = WhisperModel(
    whisper_size,
    device='cpu',
    compute_type='int8',
    cpu_threads=num_cores // 2,
    num_workers=num_cores //2
)

r = sr.Recognizer()
source = sr.Microphone()

def wav_to_text(audio_path):
    segments, _ = whisper_model.transcribe(audio_path)
    text = ''.join(segment.text for segment in segments)
    return text

def callback(recognizer, audio):
    prompt_audio_path = 'prompt.wav'
    with open(prompt_audio_path, 'wb') as f:
        f.write(audio.get_wav_data())

    prompt_text = wav_to_text(prompt_audio_path)
    print(prompt_text)

def start_listening():
    with source as s:
        r.adjust_for_ambient_noise(s, duration=2)
    print('\nSay ', wake_word, 'followed with your prompt. \n')
    r.listen_in_background(source, callback)
    while True:
        time.sleep(.5)


start_listening()