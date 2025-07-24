from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from mcp_server.llm.llm_config import llm
from mcp_server.tools.linkedin_poster import post_to_linkedin

tools = [
    Tool.from_function(
        func=post_to_linkedin,
        name="post_to_linkedin",
        description="Writes professional LinkedIn posts that follow specific personal style."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(prompt: str) -> str:
    return agent.run(prompt)
