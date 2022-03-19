"""Implement pd merge command."""
import json
import logging
import sys
from typing import List

from ..api.incident import merge_incidents

LOGGER = logging.getLogger(__name__)


def merge(source_incident_ids: List[str] = None, target_incident_id: str = None) -> str:
    """Merge incidents.

    :param source_incident_ids: list incidents to merge. if absent, read from stdin

    :return: incident dictionaries in json
    """
    if not source_incident_ids:
        source_incidents = json.load(sys.stdin)
        source_incident_ids = [incident["id"] for incident in source_incidents]
    if isinstance(source_incident_ids, str):
        source_incident_ids = [source_incident_ids]

    assert len(source_incident_ids) > 0, "no source incidents to merge"

    if not target_incident_id:
        target_incident_id = source_incident_ids[0]
        source_incident_ids = source_incident_ids[1:]

    assert len(source_incident_ids) > 0, "no source incidents to merge"

    source_incidents = [
        {"id": id, "type": "incident_reference"} for id in source_incident_ids
    ]

    result = merge_incidents(
        source_incidents=source_incidents, target_incident_id=target_incident_id
    )

    return json.dumps(result)
