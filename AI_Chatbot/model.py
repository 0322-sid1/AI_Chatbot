from transformers import pipeline

# Use zero-shot classification (no training needed)
classifier = pipeline("zero-shot-classification")

labels = ["greeting", "goodbye", "weather", "name"]

def predict_intent(text):
    result = classifier(text, candidate_labels=labels)
    return result["labels"][0]