import pyttsx3
import os
import io


def transcrever_para_audio(text: str):
    temp_file = "temp_audio.mp3"
    engine = pyttsx3.init() 

    ## Procurar uma voz em português nas vozes do seu sistema
    voices = engine.getProperty('voices')
    for voice in voices:
        if "brazil" in voice.name.lower() or "portuguese" in voice.languages:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 205)
    engine.setProperty('volume', 1.0)

    engine.save_to_file(text, temp_file)
    engine.runAndWait()

    with open(temp_file, "rb") as f:
        dados_audio = io.BytesIO(f.read())
    os.remove(temp_file)
    dados_audio.seek(0)
    return dados_audio
