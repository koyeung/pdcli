import io
import json
from unittest.mock import Mock, patch

from pdcli.command.ack import ack

from .conftest import INCIDENTS

_ACKNOWLEDGED_INCIDENTS = [
    dict(incident, status="acknowledged") for incident in INCIDENTS
]


def test_ack():

    session_mock = Mock(rput=Mock(return_value=_ACKNOWLEDGED_INCIDENTS))

    with patch("pdcli.api.incident.get_api_session", return_value=session_mock):
        result = ack(incident_ids="PT4KHLK")

    assert json.loads(result) == _ACKNOWLEDGED_INCIDENTS
    session_mock.rput.assert_called_once_with(
        "incidents",
        json=[
            {"id": "PT4KHLK", "type": "incident_reference", "status": "acknowledged"}
        ],
    )


def test_ack__stdin(monkeypatch):

    session_mock = Mock(rput=Mock(return_value=_ACKNOWLEDGED_INCIDENTS))

    monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps(INCIDENTS)))

    with patch("pdcli.api.incident.get_api_session", return_value=session_mock):
        result = ack()

    assert json.loads(result) == _ACKNOWLEDGED_INCIDENTS
    session_mock.rput.assert_called_once_with(
        "incidents",
        json=[
            {"id": "PT4KHLK", "type": "incident_reference", "status": "acknowledged"}
        ],
    )
