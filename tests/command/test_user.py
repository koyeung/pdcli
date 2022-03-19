import json
from unittest.mock import Mock, patch

from pdcli.command.user import user

_USER = {
    "name": "Zvezdochka",
    "email": "zvezdochka@ussr.example",
    "id": "PL17ZLG",
    "type": "user",
    "summary": "Zvezdochka",
}


def test_user():

    session_mock = Mock(list_all=Mock(return_value=[_USER]))

    with patch("pdcli.api.user.get_api_session", return_value=session_mock):
        result = user()

    assert json.loads(result) == [_USER]
    session_mock.list_all.assert_called_once_with("users")


def test_user__user_id():

    session_mock = Mock(rget=Mock(return_value=_USER))

    with patch("pdcli.api.user.get_api_session", return_value=session_mock):
        result = user(user_id="PL17ZLG")

    assert json.loads(result) == _USER
    session_mock.rget.assert_called_once_with("/users/PL17ZLG")
