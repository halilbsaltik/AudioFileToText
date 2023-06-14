import speech_recognition as sr

def voiceText():
    r = sr.Recognizer()
    with sr.AudioFile('C:\\Users\\AIBlack\\Desktop\\wav.wav') as source:
        audio_text = r.listen(source)

        try:
            text = r.recognize_google(audio_text, language="en-EN")
            print('converting')
            print(text)
            return text
        except:
            return "Not Detection"

voiceText()