import requests
import json
from flask import jsonify

def emotion_detector(text_to_analyse):
        URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        INPUT_JSON = { "raw_document": { "text": text_to_analyse } }
        
        response = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

        if text_to_analyse == None or text_to_analyse == 0 or text_to_analyse == "":
            #return dictionary with all values = none
            print("text is None")
            return response, 400


        object_response = requests.post(url = URL, headers = HEADERS, json = INPUT_JSON)
        json_reponse = json.loads(object_response.text)
        emotions_results = json_reponse['emotionPredictions'][0]['emotion']

        for keys in emotions_results.keys():
            response[keys] = emotions_results[keys]
            
        response['dominant_emotion'] = get_dominant_emotion(emotions_results) 

        return response,200

def get_dominant_emotion(emotions):
    dominant_emotion = ''
    highest_emotion_score = 0
    for emotion in emotions:
        if emotions.get(emotion) > highest_emotion_score:
            highest_emotion_score = emotions.get(emotion)
            dominant_emotion = emotion

    return dominant_emotion