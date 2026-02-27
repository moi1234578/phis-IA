import os
home = os.path.expanduser('~')
def crear_carpeta_voz(nombre_carpeta):
    escritorio = os.path.join(home, "Desktop")
    ruta_final = os.path.join(escritorio,nombre_carpeta)

    try:
        if not os.path.exists(ruta_final):
            os.makedirs(ruta_final)
            return f"Hecho. He creado la carpeta {nombre_carpeta} en tu escritorio."
        else:
            return "La carpeta ya existe."
    except Exception as e:
        return f"Hubo un error al crear la carpeta: {e}"
        