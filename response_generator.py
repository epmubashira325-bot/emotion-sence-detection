def generate_response(emotion):
    responses = {
        "sad": "I understand you're feeling sad. I'm here for you.",
        "happy": "That's wonderful! I'm glad you're feeling happy!",
        "angry": "I see that you're upset. Let's try to stay calm.",
        "fear": "It seems you're feeling anxious. Take a deep breath.",
        "neutral": "I'm here with you. How can I help?",
    }
    return responses.get(emotion, "I'm here for you.")