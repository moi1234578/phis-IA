from escucha import escuchar_comando
from habla import hablar
from acciones import crear_carpeta_voz

def ejecutar_phis():
    while True:
        voz = escuchar_comando() # Fase 1: Escucha activa [cite: 28]

        if "phis" in voz:
            hablar("Dime, ¿qué carpeta quieres que cree?")
            nombre = escuchar_comando()
            
            if nombre != "none":
                # Fase 2 y 3: Procesamiento y Skill [cite: 29, 30]
                resultado = crear_carpeta_voz(nombre)
                hablar(resultado)

if __name__ == "__main__":
    ejecutar_phis()