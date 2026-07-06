import logging
import os

#Crear registro de logs de pruebas
os.makedirs("proyecto_final/logs", exist_ok=True)
logging.basicConfig(
    filename="proyecto_final/logs/execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)
logger = logging.getLogger(__name__)

