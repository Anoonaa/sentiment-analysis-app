from flask import Flask, request, render_template

app = Flask(__name__)

# Simple keyword-based sentiment dictionary
sentiment_dict = {
    "positive": ["love", "good", "great", "happy", "excellent", "amazing"],
    "negative": ["hate", "bad", "awful", "terrible", "disappointing", "poor"]
}

def predict_sentiment(text):
    text = text.lower()
    if not text:
        return None
    for word in text.split():
        if any(word in sentiment_dict["positive"]):
            return "Positive"
        if any(word in sentiment_dict["negative"]):
            return "Negative"
    return "Neutral"  # Default if no strong sentiment is detected

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    text = ''
    if request.method == 'POST':
        text = request.form['text'].strip()
        if text:
            prediction = predict_sentiment(text)
    return render_template('index.html', prediction=prediction, text=text)

if __name__ == '__main__':
    app.run(debug=True)
