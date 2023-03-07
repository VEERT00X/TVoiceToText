import os
import keyboard
import pyaudio
import wave
import whisper
import threading
import time
from colorama import Style
from googletrans import Translator

press_button = 'k'
do_delete = True
do_translate = True
destination_language = 'ja'

def transcribe_audio(audio_file_path, do_delete=False, model_path="tiny", do_translate=False, destination_language="en"):
    model = whisper.load_model(model_path)
    audio = whisper.load_audio(audio_file_path)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)
    print(Style.NORMAL+ f"English: {result.text}")
    if do_translate:
        translator = Translator()
        res = translator.translate(result.text, dest=destination_language)
        print(Style.NORMAL + f"{destination_language.capitalize()}: {res.text}")
    print("Thread finished in: ", time.perf_counter(), "seconds")
    if do_delete:
        os.remove(audio_file_path)
    return result.text


def record_audio(do_delete=False):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORDS_FOLDER = "records"
    if not os.path.exists(RECORDS_FOLDER):
        os.makedirs(RECORDS_FOLDER)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    WAVE_OUTPUT_FILENAME = os.path.join(RECORDS_FOLDER, f"output-{timestamp}.wav")

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        if not keyboard.is_pressed(press_button):
            break

    stream.stop_stream()
    stream.close()
    audio.terminate()

    threading.Thread(target=transcribe_audio, args=(WAVE_OUTPUT_FILENAME, do_delete, "tiny", do_translate, destination_language)).start()

while True:
    print(Style.DIM + f"Press '{press_button}' key to start recording audio...")
    keyboard.wait(press_button, suppress=True)
    record_audio(do_delete)