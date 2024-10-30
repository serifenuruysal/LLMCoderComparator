```python
import unittest
from virtual_language_learning_buddy.user_profile import UserProfile

class TestUserProfile(unittest.TestCase):

    def setUp(self):
        self.user_profile = UserProfile(
            user_id="12345",
            language="Spanish",
            tone_preference="formal",
            context_preference="travel",
            progress={"vocabulary": 50, "grammar": 40}
        )

    def test_update_preferences(self):
        self.user_profile.update_preferences(tone="informal", context="work")
        self.assertEqual(self.user_profile.tone_preference, "informal")
        self.assertEqual(self.user_profile.context_preference, "work")

    def test_update_progress(self):
        new_progress = {"vocabulary": 60, "grammar": 50}
        self.user_profile.update_progress(new_progress)
        self.assertEqual(self.user_profile.progress["vocabulary"], 60)
        self.assertEqual(self.user_profile.progress["grammar"], 50)

    def test_initialization(self):
        self.assertEqual(self.user_profile.user_id, "12345")
        self.assertEqual(self.user_profile.language, "Spanish")
        self.assertEqual(self.user_profile.tone_preference, "formal")
        self.assertEqual(self.user_profile.context_preference, "travel")
        self.assertEqual(self.user_profile.progress["vocabulary"], 50)
        self.assertEqual(self.user_profile.progress["grammar"], 40)

if __name__ == '__main__':
    unittest.main()
```

This test suite for the `UserProfile` class includes tests for initialization, updating preferences, and updating progress. It uses Python's `unittest` framework to verify that the `UserProfile` class behaves as expected.