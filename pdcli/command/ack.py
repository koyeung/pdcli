"""Implement pd ack command."""
import json
import sys
from typing import List, Union

from ..api.incident import Status, update_incidents


def ack(
    incident_ids: Union[str, List[str]] = None,
) -> str:
    """Acknowledge incidents.

    :param incident_ids: incident ids
    """
    if not incident_ids:
        incidents = json.load(sys.stdin)
        incident_ids = [incident["id"] for incident in incidents]
    if isinstance(incident_ids, str):
        incident_ids = [incident_ids]

    assert incident_ids, "unable to determine incident ids"

    updates = [
        {"id": id, "type": "incident_reference", "status": Status.ACKNOWLEDGED}
        for id in incident_ids
    ]

    result = update_incidents(updates=updates)

    return json.dumps(result)
