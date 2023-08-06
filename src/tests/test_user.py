# -*- coding: utf-8 -*-
import pytest
from unittest.mock import MagicMock, patch
from src.models.user import User
from src.services import get_user, get_user_posts  # replace 'your_functions_module' with the actual module name

class TestUserFunctions:

    @patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_get_user(self, mock_query, mocker):
        mock_filter = mock_query.return_value.filter_by.return_value
        mock_user = MagicMock(spec=User)
        mock_user.to_dict.return_value = {'id': 1, 'username': 'test', 'date_joined': '2023-08-06', 'posts': [], 'total_posts': 0}
        mock_filter.first.return_value = mock_user
        result = get_user('test')
        assert result == {'id': 1, 'username': 'test', 'date_joined': '2023-08-06', 'posts': [], 'total_posts': 0}

    @patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_get_user_posts(self, mock_query, mocker):
        mock_filter = mock_query.return_value.filter_by.return_value
        mock_user = MagicMock(spec=User)
        mock_user.posts_to_dict.return_value = []
        mock_filter.first.return_value = mock_user
        result = get_user_posts('test')
        assert result == []
