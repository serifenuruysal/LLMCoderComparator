```python
import pyttsx3

class TextToSpeechModel:
    def __init__(self, language='en', voice_type='default', rate=150):
        self.engine = pyttsx3.init()
        self.language = language
        self.voice_type = voice_type
        self.rate = rate
        self._configure_voice()

    def _configure_voice(self):
        voices = self.engine.getProperty('voices')
        # Set the voice based on language and voice type
        for voice in voices:
            if self.language in voice.languages:
                if self.voice_type == 'default' or self.voice_type in voice.name:
                    self.engine.setProperty('voice', voice.id)
                    break
        self.engine.setProperty('rate', self.rate)

    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in TextToSpeechModel.speak: {e}")

    def set_language(self, language):
        self.language = language
        self._configure_voice()

    def set_voice_type(self, voice_type):
        self.voice_type = voice_type
        self._configure_voice()

    def set_rate(self, rate):
        self.rate = rate
        self.engine.setProperty('rate', self.rate)
```

### Explanation

- **Initialization**: The `TextToSpeechModel` class initializes a text-to-speech engine using the `pyttsx3` library. It allows setting the language, voice type, and speech rate.

- **Voice Configuration**: The `_configure_voice` method sets the voice based on the specified language and voice type. It iterates through available voices and selects one that matches the criteria.

- **Speech Synthesis**: The `speak` method converts the given text into speech. It handles exceptions to ensure robustness.

- **Dynamic Configuration**: Methods `set_language`, `set_voice_type`, and `set_rate` allow changing the language, voice type, and speech rate dynamically, reconfiguring the engine as needed.

### Best Practices

- **Error Handling**: The `speak` method includes error handling to manage any issues during speech synthesis.

- **Modularity**: The class is designed to be modular, with separate methods for configuration and speech synthesis.

- **Flexibility**: The class supports dynamic changes to language, voice type, and rate, making it adaptable to different user preferences.

This implementation provides a basic text-to-speech functionality that can be integrated into the `VoiceInteraction` component of the Virtual Language Learning Buddy.