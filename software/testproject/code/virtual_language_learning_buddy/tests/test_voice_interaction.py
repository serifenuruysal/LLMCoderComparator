```python
import unittest
from unittest.mock import MagicMock
from virtual_language_learning_buddy.voice_interaction import VoiceInteraction
from virtual_language_learning_buddy.user_profile import UserProfile
from models.speech_recognition_model import SpeechRecognitionModel
from models.text_to_speech_model import TextToSpeechModel

class TestVoiceInteraction(unittest.TestCase):

    def setUp(self):
        # Create a mock user profile
        self.user_profile = UserProfile(
            user_id="test_user",
            language="English",
            tone_preference="formal",
            context_preference="work",
            progress={}
        )

        # Create mock models
        self.speech_recognition_model = MagicMock(SpeechRecognitionModel)
        self.text_to_speech_model = MagicMock(TextToSpeechModel)

        # Initialize VoiceInteraction with mock models
        self.voice_interaction = VoiceInteraction(
            user_profile=self.user_profile,
            speech_recognition_model=self.speech_recognition_model,
            text_to_speech_model=self.text_to_speech_model
        )

    def test_process_voice_input(self):
        # Mock the behavior of the speech recognition model
        self.speech_recognition_model.recognize_speech.return_value = "Hello, how are you?"

        # Test the process_voice_input method
        voice_input = "audio_input_placeholder"
        result = self.voice_interaction.process_voice_input(voice_input)

        # Assert that the speech recognition model was called with the correct input
        self.speech_recognition_model.recognize_speech.assert_called_with(voice_input)

        # Assert that the result is as expected
        self.assertEqual(result, "Hello, how are you?")

    def test_provide_voice_feedback(self):
        # Mock the behavior of the text-to-speech model
        self.text_to_speech_model.speak.return_value = "audio_output_placeholder"

        # Test the provide_voice_feedback method
        text = "This is a test."
        result = self.voice_interaction.provide_voice_feedback(text)

        # Assert that the text-to-speech model was called with the correct input
        self.text_to_speech_model.speak.assert_called_with(text)

        # Assert that the result is as expected
        self.assertEqual(result, "audio_output_placeholder")

if __name__ == '__main__':
    unittest.main()
```

This test suite uses the `unittest` framework to test the `VoiceInteraction` class. It mocks the `SpeechRecognitionModel` and `TextToSpeechModel` to isolate the `VoiceInteraction` class and test its methods independently. The `setUp` method initializes the necessary components, and the test methods verify that the `process_voice_input` and `provide_voice_feedback` methods function as expected.