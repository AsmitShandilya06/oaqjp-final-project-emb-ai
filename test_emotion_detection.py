import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test1(self):
        response=emotion_detector("I am glad this happened")
        dominant_emotion=response.get("dominant_emotion")
        self.assertEqual(dominant_emotion, "joy")
    def test2(self):
        response=emotion_detector("I am really mad about this")
        dominant_emotion=response.get("dominant_emotion")
        self.assertEqual(dominant_emotion, "anger")    
    def test3(self):
        response=emotion_detector("I feel disgusted just hearing about this")
        dominant_emotion=response.get("dominant_emotion")
        self.assertEqual(dominant_emotion, "disgust")    
    def test4(self):
        response=emotion_detector("I am so sad about this")
        dominant_emotion=response.get("dominant_emotion")
        self.assertEqual(dominant_emotion, "sadness")    
    def test5(self):
        response=emotion_detector("I am really afraid that this will happen")
        dominant_emotion=response.get("dominant_emotion")
        self.assertEqual(dominant_emotion, "fear")
unittest.main()