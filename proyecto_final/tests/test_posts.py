import pytest

from pages.post_api_page import PostApi
from utils.logger import get_logger

api = PostApi()
logger=get_logger()

def test_get_one_post():
    logger.info("SE INICIA EL LLAMADO DEL POST")
    logger.info(f"LLAMADO AL POST CON ID: {api.get_one_post().id}")
    post_id = 2
    res= api.get_post(post_id)

def test_delete_one_post():
    logger.info("SE INICIA EL LLAMADO DEL POST")
    logger.info(f"LLAMADO AL POST CON ID: {api.get_one_post().id}")
    res= api.delete_post(post_id)