def generate_response(emotion):
    responses = {
        "sad",
        "happy",
        "angry",
        "fear",
        "neutral",
    }
    return responses.get(emotion, "I'm here for you.")
