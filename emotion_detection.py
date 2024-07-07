
from transformers import pipeline
model = pipeline(model="seara/rubert-tiny2-ru-go-emotions")

def emotion_detector():
    text_to_analyze = input(">")
    print(model(text_to_analyze))


if __name__ == "__main__":
    while True:
        emotion_detector()