from escucha import escuchar_comando
from habla import hablar
from acciones import crear_carpeta_voz

def ejecutar_phis():
    while True:
        voz = escuchar_comando()

        if "Fis" in voz:
            hablar("Dime, ¿qué carpeta quieres que cree?")
            nombre = escuchar_comando()
            
            if nombre != "none":
                resultado = crear_carpeta_voz(nombre)
                hablar(resultado)

if __name__ == "__main__":
    ejecutar_phis()