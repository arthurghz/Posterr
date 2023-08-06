# -*- coding: utf-8 -*-
import pytest
from unittest.mock import MagicMock, patch
from src.models.post import Post
from src.models.user import User
from src.services import (
    get_post
)

class TestPostFunctions:

    @patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_get_post(self, mock_query):
        mock = mock_query.return_value.filter_by.return_value
        mock_user = MagicMock(spec=Post)
        mock_user.to_dict.return_value = {'id': 1, 'text': 'test post'}
        mock.first.return_value = mock_user
        result = get_post(1)
        assert result == {'id': 1, 'text': 'test post'}
