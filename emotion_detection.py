import requests
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return ("you are home"),200


@app.route("/emotion_detector", methods=['GET','POST'])
def emotion_detector(text_to_analyse):
        URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        INPUT_JSON = { "raw_document": { "text": text_to_analyse } }
        object_response = requests.post(url = URL, headers = HEADERS, json = INPUT_JSON)
        json_reponse = json.loads(object_response.text)
        readable_response = json_reponse['emotionPredictions']
        return readable_response

'''
        response_json = response.json()
        emotion_predictions_list = response_json['emotionPredictions']
        emotion_predictions_json = jsonify(emotion_predictions_list) 
        #emotion_json = emotion_predictions_json['emotions']
        return emotion_predictions_json
    if requests.methods == 'GET':
        return ("get requested"), 200


def find_dominant_emotion(emotion_scores):
    highest_value = 0
    dominant_emotion = ''
    for emotion in emotion_scores:
        if emotion.getValue() > highest_value:
            highest_value = emotion.getValue()
            dominant_emotion = emotion.getKey()

    return dominant_emotion 
'''

if __name__ == "__main__":
    app.run(debug=True)
