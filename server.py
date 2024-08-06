from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def detector():
    if request.args.get('textToAnalyze') is not None:
        emotions = emotion_detector(request.args.get('textToAnalyze'))
        dominant_emotion = emotions['dominant_emotion']

        if dominant_emotion:
            del emotions['dominant_emotion']
            outp = 'For the given statement, the system response is '

            for emotion in emotions.keys():
                if emotion != list(emotions)[-1]:
                    outp += f"'{emotion}': {emotions[emotion]}, "
                else:
                    outp = outp[:-2] + \
                        f" and '{emotion}': {emotions[emotion]}. "

            outp += f'The dominant emotion is <strong>{dominant_emotion}</strong>.'
        else:
            outp = '<strong>Invalid text! Please try again!</strong>'

        return outp
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
