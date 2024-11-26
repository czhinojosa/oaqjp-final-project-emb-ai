"""
Emotion Detector Flask Application
Dependencies:
- Flask
- A custom `emotion_detector` function from the EmotionDetection package.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def get_emotion_detector():
    """
    Endpoint to analyze emotions in the provided text.

    Query Parameters:
        textToAnalyze (str): The text input from the user to analyze emotions.

    Returns:
        str: A formatted string with emotion scores for anger, disgust, fear,
             joy, and sadness. Also, includes the dominant emotion if found.
             Returns an error message if no valid input is provided.

    Example Usage:
        GET /emotionDetector?textToAnalyze=I+am+so+happy
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Try again."

    return f"For the given statement, the system response is " \
           f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, " \
           f"'joy': {joy}, and 'sadness': {sadness}.\nThe dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    Renders the index page of the application.

    Returns:
        str: Rendered HTML content from the 'index.html' template.
    """
    return render_template('index.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
