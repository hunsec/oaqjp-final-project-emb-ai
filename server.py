""" server.py
---------
Routes:
    - /emotionDetector [GET]: Accepts a 'textToAnalyze' query parameter and returns
      predicted emotions in JSON format. Returns HTTP 400 if input is invalid.
Usage:
    Run the server:
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/")
def render_index_page():
    """ Render the main index page of the web application.
    Returns:
        str: Rendered HTML content of 'index.html'.
    Usage:
        Visit the root URL ("/") of the server to see the homepage.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    """ Detect emotions from a text query parameter and return results.
    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions.
    Returns:
        str or dict: 
            - If the text is invalid (empty, None, or 0), returns an error message string.
            - Otherwise, returns a dictionary of detected emotions.
    Usage:
        Example GET request:
            /emotionDetector?textToAnalyze=I%20am%20happy
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response, status = emotion_detector(text_to_analyse)
    if status == 400:
        return " Invalid text! Please try again!"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
