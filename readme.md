# TVoiceToText

TVoiceToText is a Python script that allows you to transcribe speech in real-time and translate it to another language. It uses the Whisper library for speech recognition and Google Translate API for translation.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- PyAudio
- Whisper
- Wave
- Colorama
- Googletrans

You can install all the required packages using the requirements.txt file included in this repository. To install the packages, run:

```bash
pip install -r requirements.txt
```

### Usage

To start recording and transcribing speech, run the main.py file:

The script will prompt you to press the k key to start recording. Once you press the key, the script will start recording your speech until you release the key. It will then transcribe the speech to English and translate it to another language (default is Japanese) using Google Translate API. The translation can be disabled by setting the do_translate parameter to False in the config dictionary.

The recorded audio file will be saved in the records directory by default. You can change the output directory by modifying the RECORDS_FOLDER variable in the record_audio function.

### Configuration

The behavior of the script can be customized by modifying the config dictionary in the main.py file. The following options are available:

press_button: The key to press to start recording (default is k).
do_delete: Whether to delete the recorded audio file after transcription (default is True).
do_translate: Whether to translate the transcription to another language (default is True).
language: The language to translate the transcription to (default is Japanese).
