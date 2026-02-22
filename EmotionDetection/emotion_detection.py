import requests
import json

def emotion_detector(text_to_analyse):
    try:
        response=requests.post(
            url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
            headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
            json={ "raw_document": { "text": text_to_analyse } }
        )
        response.raise_for_status()
        response=response.json()
        text=''
        emotions={}
        for attr1 in response['emotionPredictions']:
            emotions=attr1['emotion']
            for attr2 in attr1['emotionMentions']:
                text=attr2['span']['text']
        dominant_emotion= max(emotions.items(), key= lambda x:x[1])
        dominant_name, dominant_score= dominant_emotion
        return {
            **emotions,
            'dominant_emotion': dominant_name
        }
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error {e.response.status_code}: {e}")
        if e.response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        return {
            'message': str(e),
            'detail': e.response.text
        }
    except requests.exceptions.RequestException as e:
        print(f"API call failed: {e}")
        return None