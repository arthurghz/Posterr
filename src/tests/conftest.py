# -*- coding: utf-8 -*-
import pytest
from src import create_app

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        yield app
