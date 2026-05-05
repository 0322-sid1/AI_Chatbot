from utils import preprocess, extract_entities
from model import predict_intent
from db import save_message

context = {}

responses = {
    "greeting": "Hello! How can I help you?",
    "goodbye": "Goodbye! Have a nice day!",
    "weather": "Please tell me your city.",
    "name": "I am your AI assistant."
}


def chatbot(user_input, user_id="user1"):
    processed = preprocess(user_input)
    intent = predict_intent(processed)

    entities = extract_entities(user_input)

    # Context handling
    if context.get(user_id) == "weather":
        response = f"Weather info for {user_input} coming soon..."
    else:
        response = responses.get(intent, "Sorry, I didn't understand.")

    context[user_id] = intent

    # Save to DB
    save_message(user_id, user_input, response)

    return response