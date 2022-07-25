import pytest
from pythonapi import create_app

@pytest.fixture()
def app():
    app = api()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here