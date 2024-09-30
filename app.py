from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
from io import BytesIO

app = Flask(__name__)

# Serve the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to convert text to speech
@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.get_json()
    text = data['text']

    if not text.strip():
        return "Error: No text provided", 400

    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='en')

    # Save audio in a BytesIO object to avoid writing to disk
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)  # Reset the file pointer to the beginning

    return send_file(audio_file, as_attachment=True, download_name='output.mp3', mimetype='audio/mpeg')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
