import requests
import json
def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        
        # Extract the emotion scores dictionary
        emotions = response_dict['emotionPredictions'][0]['emotion']
        
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Prepare output dictionary with scores and dominant emotion
        emotion_score = {
            'anger': emotions.get('anger', 0.0),
            'disgust': emotions.get('disgust', 0.0),
            'fear': emotions.get('fear', 0.0),
            'joy': emotions.get('joy', 0.0),
            'sadness': emotions.get('sadness', 0.0),
            'dominant_emotion': dominant_emotion
        }
        
        return emotion_score
    else:
        return None