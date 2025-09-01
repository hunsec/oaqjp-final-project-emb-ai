import requests
import json

text_to_analyse = "I would love it if this works"


def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT_JSON = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url = URL, headers = HEADERS, json = INPUT_JSON)
    return response.text

if __name__ == "__main__":
    result = emotion_detector(text_to_analyse)
    print(result)