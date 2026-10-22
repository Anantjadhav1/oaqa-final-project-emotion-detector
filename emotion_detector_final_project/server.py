"""Flask web interface for the Emotion Detector."""

from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Display the input form and process submitted text."""
    result = None
    error = None
    submitted_text = ""

    if request.method == "POST":
        submitted_text = request.form.get("text", "").strip()
        if not submitted_text:
            error = "Invalid input: please enter some text."
        else:
            result = emotion_detector(submitted_text)
            if result.get("dominant_emotion") is None:
                error = (
                    "Unable to analyze the text. Check your connection "
                    "and try again."
                )
                result = None

    return render_template(
        "index.html",
        result=result,
        error=error,
        submitted_text=submitted_text,
    )


if __name__ == "__main__":
    app.run(debug=False)
