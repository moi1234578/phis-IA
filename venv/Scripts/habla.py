import pyttsx3
engine = pyttsx3.init('sapi5')

def hablar(mensaje):
    print(f"Asistente dice: {mensaje}")
    engine.say(mensaje)
    engine.runAndWait()