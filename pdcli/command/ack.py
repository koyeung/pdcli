"""Implement pd ack command."""
from typing import List
import json
import sys

from ..api.incident import update_incidents, Status


def ack(
    incident_ids: List[str] = None,
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
