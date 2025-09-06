from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    text_to_analyse = request.args.get('text_to_analyse')
    response = emotion_detector(text_to_analyse)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

    
