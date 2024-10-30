```python
import speech_recognition as sr

class SpeechRecognitionModel:
    def __init__(self, language='en-US'):
        self.recognizer = sr.Recognizer()
        self.language = language

    def recognize_speech(self, voice_input):
        """
        Recognizes speech from the given audio input and returns the recognized text.
        
        :param voice_input: Audio input to be recognized.
        :return: Recognized text from the audio input.
        """
        try:
            with sr.AudioFile(voice_input) as source:
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio_data, language=self.language)
                return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Sorry, there was an error with the speech recognition service."
        except Exception as e:
            return f"An error occurred: {str(e)}"
```

### Explanation

- **Initialization**: The `SpeechRecognitionModel` class initializes with a default language set to 'en-US'. It uses the `speech_recognition` library's `Recognizer` class to handle speech recognition tasks.

- **recognize_speech Method**: This method takes an audio input file, processes it, and returns the recognized text using Google's speech recognition service. It handles exceptions for unknown values, request errors, and other general exceptions, providing appropriate error messages.

- **Error Handling**: The method includes error handling for common issues such as unrecognized speech and service request errors, ensuring robustness in various scenarios.

- **Dependencies**: The code requires the `speech_recognition` library, which can be installed via pip if not already available in your environment.