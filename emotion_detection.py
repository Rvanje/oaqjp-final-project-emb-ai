import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://www.facebook.com'
    # url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=header, json=input)

    if 200 <= response.status_code <= 211:
        print("Connection established."), response.json().get('emotions', {})
    if 300 <= response.status_code <= 311:
        print("Connection error.")
    if 400 <= response.status_code <= 411:
        print("Client error.")
    if 500 <= response.status_code <= 511:
        print("Server error.")
    else:
        print("Unknown error.")


if __name__ == "__main__":
    emotion_detector("I am so happy I am doing this")