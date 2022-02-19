from unittest.mock import Mock, patch
import json

from pdcli.command.merge import merge

_TARGET_INCIDENT = {
    "incident": {
        "id": "PT4KHLK",
        "type": "incident_reference",
        "summary": "[#1234] The server is on fire.",
        "self": "https://api.pagerduty.com/incidents/PT4KHLK",
        "html_url": "https://subdomain.pagerduty.com/incidents/PT4KHLK",
    }
}


def test_merge():

    session_mock = Mock(
        put=Mock(return_value=Mock(json=Mock(return_value=_TARGET_INCIDENT)))
    )

    with patch("pdcli.api.incident.get_api_session", return_value=session_mock):
        result = merge(
            source_incident_ids=["P8JOGX7", "PPVZH9X"],
            target_incident_id="PT4KHLK",
        )

    assert json.loads(result) == _TARGET_INCIDENT
    session_mock.put.assert_called_once_with(
        "incidents/PT4KHLK/merge",
        json={
            "source_incidents": [
                {
                    "id": "P8JOGX7",
                    "type": "incident_reference",
                },
                {
                    "id": "PPVZH9X",
                    "type": "incident_reference",
                },
            ],
        },
    )
