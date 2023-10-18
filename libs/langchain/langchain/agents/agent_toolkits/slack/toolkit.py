from __future__ import annotations

from typing import TYPE_CHECKING, List

from langchain.agents.agent_toolkits.base import BaseToolkit
from langchain.pydantic_v1 import Field
from langchain.tools import BaseTool
from langchain.tools.slack.send_message import SlackSendMessage

if TYPE_CHECKING:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError

class SlackToolKit(BaseToolkit):
    """Toolkit for interacting with Slack."""

    class Config:
        """Pydantic config."""

        arbitrary_types_allowed = True

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return [SlackSendMessage()]