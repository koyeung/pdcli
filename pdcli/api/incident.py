"""Interface to incident endpoint."""
import datetime
import logging
from enum import Enum
from typing import Any, Dict, List, Optional

from .session import get_api_session

LOGGER = logging.getLogger(__name__)


class Status(Enum):
    """Incident status."""

    TRIGGERED = "triggered"
    ACKNOWLEDGED = "acknowledged"
    RESOLVED = "resolved"


class Urgency(Enum):
    """Incident urgency."""

    HIGH = "high"
    LOW = "low"


def list_incidents(
    *,
    since: Optional[datetime.date] = None,
    statuses: Optional[List[Status]] = None,
    user_ids: Optional[List[str]] = None,
    urgency: Optional[Urgency] = None,
) -> List:
    """List incidents."""
    params: Dict[str, Any] = {}
    if since:
        params["since"] = since.isoformat()

    if statuses:
        params["statuses"] = [status.value for status in statuses]

    if user_ids:
        params["user_ids"] = user_ids

    if urgency:
        params["urgencies"] = [urgency.value]

    LOGGER.debug(f"{params=}")

    session = get_api_session()
    incidents = session.list_all("incidents", params=params)

    return incidents


def update_incidents(
    *,
    updates: List[Dict],
) -> List:
    """Update incidents."""

    def convert_enum_to_json_encodable(key, value):
        if key == "status":
            value = value.value
        return key, value

    updates = [
        dict(
            convert_enum_to_json_encodable(key=key, value=value)
            for key, value in update.items()
        )
        for update in updates
    ]

    session = get_api_session()
    results = session.rput("incidents", json=updates)

    return results
