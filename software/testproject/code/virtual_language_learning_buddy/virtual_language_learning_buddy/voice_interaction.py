```python
import speech_recognition as sr
from gtts import gTTS
import os
from models.speech_recognition_model import SpeechRecognitionModel
from models.text_to_speech_model import TextToSpeechModel
from virtual_language_learning_buddy.user_profile import UserProfile

class VoiceInteraction:
    def __init__(self, user_profile: UserProfile):
        self.user_profile = user_profile
        self.speech_recognition_model = SpeechRecognitionModel()
        self.text_to_speech_model = TextToSpeechModel()

    def process_voice_input(self, voice_input):
        """
        Processes voice input from the user and converts it to text.
        """
        try:
            recognized_text = self.speech_recognition_model.recognize_speech(voice_input)
            return recognized_text
        except Exception as e:
            print(f"Error processing voice input: {e}")
            return None

    def provide_voice_feedback(self, text):
        """
        Provides feedback in voice form by converting text to speech.
        """
        try:
            self.text_to_speech_model.speak(text)
        except Exception as e:
            print(f"Error providing voice feedback: {e}")

# models/speech_recognition_model.py
class SpeechRecognitionModel:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, voice_input):
        with sr.AudioFile(voice_input) as source:
            audio = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                raise Exception("Could not understand audio")
            except sr.RequestError:
                raise Exception("Could not request results from Google Speech Recognition service")

# models/text_to_speech_model.py
class TextToSpeechModel:
    def speak(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("mpg321 output.mp3")
```

### Explanation

- **VoiceInteraction Class**: This class handles the interaction with the user through voice. It uses the `SpeechRecognitionModel` to convert voice input to text and the `TextToSpeechModel` to convert text to speech.

- **SpeechRecognitionModel Class**: This class uses the `speech_recognition` library to convert audio input into text. It handles exceptions for cases where the audio cannot be understood or if there is an issue with the recognition service.

- **TextToSpeechModel Class**: This class uses the `gTTS` library to convert text into speech and plays the audio using a system command. It saves the audio as an MP3 file and plays it using `mpg321`.

### Note
- Ensure that the necessary libraries (`speech_recognition`, `gTTS`, and `mpg321`) are installed and configured correctly in your environment.
- The `mpg321` command is used to play the audio file. Ensure that this command is available on your system, or replace it with an appropriate command for your platform.