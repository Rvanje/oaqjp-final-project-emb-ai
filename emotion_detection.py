import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://www.facebook.com'
    # url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = {"raw_document": {"text": text_to_analyze}}

    connecton_check(requests.post(url, headers=header, json=input))

def connecton_check(response):
    if response == range(200, 211):
        return "Connection established.", response.json().get('emotions', {})
    if response == range(300, 311):
        return "Connection error."
    if response == range(400, 411):
        return "Client error."
    if response == range(500, 511):
        return "Server error."
    else:
        return "Unknown error."


if __name__ == "__main__":
    emotion_detector("I am so happy I am doing this")