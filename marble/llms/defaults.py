"""
Default model names, overridable through environment variables so that
simulations can run against local or alternative providers via LiteLLM.
"""

import os

DEFAULT_LLM: str = os.environ.get("MARBLE_DEFAULT_LLM", "gpt-3.5-turbo")
DEFAULT_EMBEDDING_MODEL: str = os.environ.get(
    "MARBLE_EMBEDDING_MODEL", "text-embedding-3-small"
)
