# Final Project – Emotion Detector

A small Flask web application that uses the Watson NLP Emotion Prediction API to identify anger, disgust, fear, joy, and sadness in text.

## Setup

```bash
python -m pip install -r requirements.txt
```

## Run the application

```bash
python server.py
```

Open http://127.0.0.1:5000 in your browser.

## Run unit tests

```bash
python -m unittest discover -s tests -v
```

## Run static analysis

```bash
python -m pylint server.py emotion_detection
```

## Notes

- The application calls the Watson NLP Emotion Prediction API over the internet.
- A network/API issue may prevent live predictions. The application reports an error instead of inventing results.
- This is a starter project. If your course provides an original repository, compare its expected filenames and requirements before submitting.
