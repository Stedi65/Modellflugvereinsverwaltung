from gtts import gTTS
from playsound import playsound


def txt2speech(txt: str, lang: str, slow=False):
    tts = gTTS(text=txt, lang=lang, slow=slow)
    tts.save("tts.mp3")
    playsound("tts.mp3")


if __name__ == '__main__':
    text = "Sanitär Heizung Schwimmbadtechnik Röhrich"
    txt2speech(text, 'de')




