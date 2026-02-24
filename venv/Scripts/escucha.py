import speech_recognition as sr

def escuchar_comando():
    reconocedor =sr.Recognizer()
    with sr.Microphone() as fuente:
        print ("escuchando")
        reconocedor.pause_threshold = 0.8
        audio = reconocedor.listen(fuente)
    try:
        texto = reconocedor.recognize_google(audio, language ='es-MX')
        return texto.lower()
    except Exception:
        return "nome"