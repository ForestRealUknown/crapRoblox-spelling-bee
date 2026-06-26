import speech_recognition as sr


def transcribe():
    Audio_Files = "desktop_audio.wav"

    r = sr.Recognizer()

    with sr.AudioFile(Audio_Files) as source:
        audio = r.record(source)
        try:
            return (r.recognize_google(audio))
        except:
            print("transcription failed")