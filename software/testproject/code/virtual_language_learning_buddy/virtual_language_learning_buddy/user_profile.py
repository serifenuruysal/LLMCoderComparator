```python
class UserProfile:
    def __init__(self, user_id, language, tone_preference, context_preference):
        self.user_id = user_id
        self.language = language
        self.tone_preference = tone_preference
        self.context_preference = context_preference
        self.progress = {}

    def update_preferences(self, tone, context):
        """Update the user's tone and context preferences."""
        self.tone_preference = tone
        self.context_preference = context
        print(f"Preferences updated: Tone - {tone}, Context - {context}")

    def update_progress(self, new_progress):
        """Update the user's learning progress."""
        self.progress.update(new_progress)
        print(f"Progress updated: {new_progress}")

    def get_progress(self):
        """Get the user's current progress."""
        return self.progress

    def __str__(self):
        return (f"UserProfile(user_id={self.user_id}, language={self.language}, "
                f"tone_preference={self.tone_preference}, context_preference={self.context_preference}, "
                f"progress={self.progress})")
```

This code defines the `UserProfile` class, which manages user preferences and progress. It includes methods to update preferences and progress, as well as a method to retrieve the current progress. The `__str__` method provides a string representation of the user profile for easy debugging and logging.