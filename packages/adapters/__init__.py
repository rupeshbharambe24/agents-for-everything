"""Framework adapters for running afe/v1 agents in external orchestrators."""

from .claude_agent_sdk import as_claude_subagent
from .crewai import as_crewai_agent_spec
from .google_adk import as_google_adk_agent_spec
from .langgraph import as_langgraph_node
from .ms_agent_framework import as_ms_agent_config
from .openai_agents import as_openai_agent_spec

__all__ = [
    "as_claude_subagent",
    "as_crewai_agent_spec",
    "as_google_adk_agent_spec",
    "as_langgraph_node",
    "as_ms_agent_config",
    "as_openai_agent_spec",
]
