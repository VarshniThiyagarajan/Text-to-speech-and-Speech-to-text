from flask import Flask, render_template, request, send_file # type: ignore
from gtts import gTTS # type: ignore
from textblob import TextBlob # type: ignore

app = Flask(__name__)

transliteration_dict = {
    "epdi": "எப்படி",
    "vaanga": "வாங்க",
    "nalla": "நல்ல",
    # Add more as necessary
}

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

def apply_transliteration(text):
    for key, value in transliteration_dict.items():
        text = text.replace(key, value)
    return text

@app.route('/')
def intro():
    return render_template('intro.html')  

@app.route('/login')
def index2():
    return render_template('index2.html')  

@app.route('/category')
def deaf():
    return render_template('deaf.html')    

@app.route('/language')
def index1():
    return render_template('index1.html')

@app.route('/phone-dial')
def index():
    return render_template('index.html')

@app.route('/speech-to-text')
def speech_to_text():
    return render_template('webstt.html')

@app.route('/text-to-speech')
def text_to_speech():
    return render_template('tts.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    lang = request.form.get('lang', 'ta')  # default language is Tamil

    text = apply_transliteration(text)
    sentiment = analyze_sentiment(text)
    if sentiment > 0:
        rate = 140
        volume = 1.0
    elif sentiment < 0:
        rate = 100
        volume = 0.7
    else:
        rate = 130
        volume = 0.9

    tts = gTTS(text=text, lang=lang, slow=False)
    temp_filename = 'output.mp3'
    tts.save(temp_filename)

    return send_file(temp_filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
