"""Interface to user endpoint."""
import logging
from typing import Dict, List

from .session import get_api_session

LOGGER = logging.getLogger(__name__)


def get_user(*, user_id: str) -> Dict:
    """Get user.

    :return: user dictionary
    """
    session = get_api_session()
    return session.rget(f"/users/{user_id}")


def ls_user() -> List:
    """List users."""
    session = get_api_session()
    return session.list_all("users")
