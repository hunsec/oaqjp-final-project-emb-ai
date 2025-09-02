import requests
import json

def emotion_detector(text_to_analyse):
        URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        INPUT_JSON = { "raw_document": { "text": text_to_analyse } }
        object_response = requests.post(url = URL, headers = HEADERS, json = INPUT_JSON)
        json_reponse = json.loads(object_response.text)
        readable_response = json_reponse['emotionPredictions'][0]['emotion']
        return readable_response
