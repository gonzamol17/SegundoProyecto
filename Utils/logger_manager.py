import logging
from pathlib import Path
from Utils.path_manager import get_project_root

def get_logger(name: str):
    logger = logging.getLogger(name)

    # Evita crear handlers duplicados
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # Carpeta Logs en la raíz
    logs_dir = get_project_root() / "Logs"
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "framework.log"

    # Handler para archivo
    file_handler = logging.FileHandler(str(log_file), encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.propagate = False

    print(f"[LOGGER] Escribiendo logs en: {log_file}")  # DEBUG VISIBLE EN CONSOLA

    return logger