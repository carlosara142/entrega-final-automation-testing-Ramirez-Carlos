import pytest

@pytest.fixture
def posts_data():
    return {
    "userId": 23,
    "title": "mi primer post",
    "body": "contenido de mi primer posteo"
    }

@pytest.fixture
def users_data():
    return {
    "name": "carlos ramirez",
    "username": "carlosr",
    "email": "carlosram@gmail.com",
    }