import pytest
import pytest_check as check
from pages.post_api_page import PostApi
from utils.logger import logger

api = PostApi()


def test_get_one_post():
    logger.info("Obteniendo un post en especifico")
    
    response = api.get_one_post(1)

    check.equal(
        response.status_code,
        200,
        "Status incorrecto"
        )
    body = response.json()
    check.equal(
        body["id"], #meda el valor del id del post
        1,
        "ID no coincide"
        )
def test_all_posts():
    logger.info("Obteniendo todos los posts")
    response = api.get_all_posts()
    print(response)

    check.equal(
        response.status_code,
        200,
        "Status incorrecto"
        )
    posts=response.json()

    check.is_true(
        len(posts) > 0,
        "No se encontraron posts"
    )
    check.is_true(
        isinstance(posts, list),
    )