"""Flask server application for handling emotion detection requests via a web interface."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Constants for query parameters nad error messages
TEXT_ANALYZE_PARAM = "textToAnalyze"
ERROR_MESSAGE = "Invalid text! Please try again!"

# Initialize Flask application with standard naming convention
app = Flask(
    __name__,
    template_folder='../oaqjp-final-project-emb-ai/templates',
    static_folder='../oaqjp-final-project-emb-ai/static'
)

@app.route("/", methods=["GET"])
def render_index_page():
    """
    Render the main index.html page for the emotion detection app.
    This route serves the main page of the application where the user can input text 
    for emotion detection.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """
    Handle emotion detection for user input text.
    If the input is valid, the function calls the emotion detector and returns the emotions.
    If the input is empty or invalid, it returns an error message.
    """
    text_to_analyze = request.args.get(TEXT_ANALYZE_PARAM, "")

    # Check if the input text is empty
    if not text_to_analyze:
        return ERROR_MESSAGE

    # Call emotion detector function to analyze the provided text
    result = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None and return an error message
    if result['dominant_emotion'] is None:
        return ERROR_MESSAGE

    # Format the response with the emotions and dominant emotion
    response_string = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_string


if __name__ == "__main__":
    # Run the Flask app on localhost
    app.run(host="0.0.0.0", port=5000)