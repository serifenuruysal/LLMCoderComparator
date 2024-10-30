```python
import unittest
from virtual_language_learning_buddy.cultural_context import CulturalContext
from virtual_language_learning_buddy.user_profile import UserProfile
from data.cultural_data import cultural_data

class TestCulturalContext(unittest.TestCase):

    def setUp(self):
        # Create a mock user profile
        self.user_profile = UserProfile(
            user_id="test_user",
            language="Spanish",
            tone_preference="formal",
            context_preference="travel",
            progress={}
        )
        # Initialize CulturalContext with the mock user profile
        self.cultural_context = CulturalContext(self.user_profile, cultural_data)

    def test_provide_contextual_response(self):
        # Test input text
        input_text = "What should I say when I meet someone for the first time in Spain?"
        
        # Expected response based on cultural data
        expected_response = "In Spain, a common greeting is 'Hola, ¿cómo estás?'"

        # Get the actual response from the CulturalContext
        actual_response = self.cultural_context.provide_contextual_response(input_text)

        # Assert that the actual response matches the expected response
        self.assertEqual(actual_response, expected_response)

    def test_provide_contextual_response_with_unknown_context(self):
        # Test input text with an unknown context
        input_text = "How do I greet someone in a business meeting in Japan?"

        # Expected response when the context is not found
        expected_response = "I'm sorry, I don't have information on that cultural context."

        # Get the actual response from the CulturalContext
        actual_response = self.cultural_context.provide_contextual_response(input_text)

        # Assert that the actual response matches the expected response
        self.assertEqual(actual_response, expected_response)

    def test_provide_contextual_response_with_empty_input(self):
        # Test with empty input text
        input_text = ""

        # Expected response for empty input
        expected_response = "Please provide a valid input."

        # Get the actual response from the CulturalContext
        actual_response = self.cultural_context.provide_contextual_response(input_text)

        # Assert that the actual response matches the expected response
        self.assertEqual(actual_response, expected_response)

if __name__ == '__main__':
    unittest.main()
```

This test suite for the `CulturalContext` class includes tests for providing contextual responses based on user input. It checks for expected responses, handles unknown contexts, and validates behavior with empty input. The `setUp` method initializes a mock user profile and a `CulturalContext` instance for use in the tests.