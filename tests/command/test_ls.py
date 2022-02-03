from unittest.mock import Mock, patch
import json
import csv
import io

from pdcli.command.ls import ls

from .conftest import INCIDENTS


def test_ls():

    session_mock = Mock(list_all=Mock(return_value=INCIDENTS))

    with patch("pdcli.api.incident.get_api_session", return_value=session_mock):
        result = ls()

    assert json.loads(result) == INCIDENTS
    session_mock.list_all.assert_called_once_with("incidents", params={})


def test_ls__columns():

    session_mock = Mock(list_all=Mock(return_value=INCIDENTS))

    with patch("pdcli.api.incident.get_api_session", return_value=session_mock):
        result = ls(column=True)

    with io.StringIO(result) as file_:
        table = list(csv.DictReader(file_, delimiter="\t"))
    assert table == [
        {
            "status": "triggered",
            "urgency": "high",
            "title": "The server is on fire.",
            "created_at": "2015-10-06T21:30:42Z",
            "service": "My Mail Service",
            "assignments": "ABC CDE",
        }
    ]
    session_mock.list_all.assert_called_once_with("incidents", params={})


def test_ls__params():

    session_mock = Mock(list_all=Mock(return_value=INCIDENTS))

    with patch("pdcli.api.incident.get_api_session", return_value=session_mock):
        ls(
            since="2022-02-03",
            statuses=["triggered", "acknowledged"],
            urgency="high",
        )

    session_mock.list_all.assert_called_once_with(
        "incidents",
        params={
            "since": "2022-02-03",
            "statuses": ["triggered", "acknowledged"],
            "urgencies": ["high"],
        },
    )
