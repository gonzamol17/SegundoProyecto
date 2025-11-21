from pathlib import Path

def get_project_root():
    # Obtiene la carpeta actual donde está ESTE archivo
    current_file = Path(__file__).resolve()

    # Buscamos la carpeta raíz por nombre del proyecto
    # Ajusta el nombre si tu carpeta del proyecto cambia
    for parent in current_file.parents:
        if parent.name == "SegundoProyecto":
            return parent

    # Si no se encontró, usamos el parent del archivo actual
    return current_file.parents[1]