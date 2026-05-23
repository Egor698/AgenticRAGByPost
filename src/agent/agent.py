from langchain.agents import create_agent

from src.components.llm_model import llm
from src.agent.tools import retrieve
from src.agent.prompts import SYSTEM_PROMPT

agent = create_agent(
    llm,
    tools=[retrieve],
    system_prompt=SYSTEM_PROMPT
)

