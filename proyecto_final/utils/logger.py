import logging
import os

#Crear registro de logs de pruebas
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)
logger = logging.getLogger(__name__)

