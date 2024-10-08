````markdown
# Code Documentation

This document provides a detailed overview of the Python script for interactive vocabulary practice using speech recognition and text-to-speech technologies.

## Script Overview

The script uses the `speech_recognition` library to convert speech to text, the `gtts` (Google Text-to-Speech) library to convert text to speech, and the `playsound` library to play audio files.

## Code Breakdown

### 1. Importing Libraries

```python
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
```
````

- `speech_recognition`: Library for speech-to-text conversion.
- `gtts`: Google Text-to-Speech library for text-to-speech conversion.
- `os`: Provides functions for interacting with the operating system, such as file management.
- `playsound`: Simple library for playing sound files.

### 2. Initialize Recognizer

```python
recognizer = sr.Recognizer()
```

- Creates an instance of `Recognizer` from the `speech_recognition` library to handle speech recognition.

### 3. Vocabulary List

```python
vocab_list = [
    "Khí quyễn",  # atmosphere
    "khoãng",     # almost
    "Phần lớn",   # mostly
    "Giải thích", # explanation
    "Áp lực",     # pressure
    "Có sẵn",     # available
    "Bốc hơi",    # evaporating
    "Tan ra trong", # dissolved in
    "Kết tủa",    # precipitation
    "Thành phần", # composition
    "Mất",        # disappearance
    "Nhiệt độ",   # temperature
    "Phổ biến",   # prevalent
    "Kết quả là", # result in
    "Tích tụ",    # accumulation
    "Mở rộng",    # expansion
    "Hút vào",    # absorb into
    "Giải phóng", # release
    "Kết hợp",    # combine with
    "Thay thế"    # replace
]
```

- Defines a list of vocabulary words in Vietnamese, with English translations in comments.

### 4. Function: `speak(text)`

```python
def speak(text):
    tts = gTTS(text=text, lang='vi')
    tts.save("speak.mp3")
    playsound("speak.mp3")
    os.remove("speak.mp3")
```

- Converts text to speech using `gTTS` and saves it as an MP3 file.
- Plays the MP3 file using `playsound`.
- Deletes the MP3 file after playing to clean up.

### 5. Function: `listen()`

```python
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="vi-VN")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection")
            return ""
```

- Captures audio from the microphone.
- Converts the audio to text using Google's speech recognition API.
- Handles exceptions if the audio is not recognized or if there is a network error.

### 6. Main Loop

```python
for word in vocab_list:
    speak(word)  # Máy phát từ vựng
    user_input = listen()  # Người dùng trả lời
    print(f"User response: {user_input}")
    # Tiếp tục hỏi từ tiếp theo
```

- Iterates through the list of vocabulary words.
- Speaks each word and listens for the user's response.
- Prints the user's response to the console.

## Running the Script

1. Ensure all required libraries are installed:

   ```sh
   pip install SpeechRecognition gTTS playsound
   ```

2. Run the script using Python:

   ```sh
   python listen.py
   ```

3. Follow the prompts as the script asks each vocabulary word and listens for your spoken responses.

## Troubleshooting

- **No Sound or Audio Issues**: Ensure your speakers are working and the volume is up.
- **Microphone Issues**: Ensure your microphone is properly connected and configured.
- **Library Installation Issues**: Verify that all required libraries are installed correctly.

## License

This script is provided under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

For questions or feedback, please contact [Anh Nghĩa](mailto:your-quocnghia91ll@gmail.com).
