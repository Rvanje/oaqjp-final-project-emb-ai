# Utilization of a emotion detection model installed locally due to connection issues with watson.ai on my local machine


def emotion_detector(text_to_analyze: str):
    model = pipeline(model="seara/rubert-tiny2-ru-go-emotions")
    return model(text_to_analyze)[0]


if __name__ == "__main__":
    # Testin functionalities
    from transformers import pipeline
    model = pipeline(model="seara/rubert-tiny2-ru-go-emotions")

    while True:
        client_input = str(input(">"))
        emotion = emotion_detector(client_input)
        print(emotion["label"])