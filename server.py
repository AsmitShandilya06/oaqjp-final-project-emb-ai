from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app=Flask("Emotion Detector App")

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)
    if(response.get('dominant_emotion')== None):
        return "Invalid text! Please try again!."
    dominant_emotion= response.popitem()
    return f"For the given statement, the system response is {str(response)}. The dominant emotion is {dominant_emotion[1]}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)