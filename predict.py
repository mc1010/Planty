import random

def predict(image_bytes):
    label = random.choice(["sain", "malade"])
    confidence = round(random.uniform(0.6, 0.99), 2)
    return label, confidence
