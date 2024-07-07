import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://www.facebook.com'
    # url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url) # , json=input)
    # response = requests.post(url, headers=header, json=input)

    print(response.status_code)
    # return response.json().get('emotions', {})

def connecton_check():
    pass

if __name__ == "__main__":
    emotion_detector("I am so happy I am doing this")