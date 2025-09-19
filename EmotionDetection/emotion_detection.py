import requests
import json

def emotion_detector(text_to_analyse):
        URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        INPUT_JSON = { "raw_document": { "text": text_to_analyse } }

        object_response = requests.post(url = URL, headers = HEADERS, json = INPUT_JSON)
        json_reponse = json.loads(object_response.text)
        print("text: " + text_to_analyse)
        print("json:" + json_reponse)
        readable_response = json_reponse['emotionPredictions'][0]['emotion']
        readable_response['dominant_emotion'] = get_dominant_emotion(readable_response) 

        if text_to_analyse == None:
            #return dictionary with all values = none
            for keys in readable_response.keys():
                readable_response[keys] = None

            return (readable_response, 400)


        return readable_response

def get_dominant_emotion(emotions):
    dominant_emotion = ''
    highest_emotion_score = 0
    for emotion in emotions:
        if emotions.get(emotion) > highest_emotion_score:
            highest_emotion_score = emotions.get(emotion)
            dominant_emotion = emotion

    return dominant_emotion