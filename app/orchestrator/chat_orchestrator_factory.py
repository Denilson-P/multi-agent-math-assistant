from app.agents.expression_interpreter_agent import (
    ExpressionInterpreterAgent,
)
from app.agents.mathematical_agent import MathematicalAgent
from app.agents.writer_agent import WriterAgent
from app.clients.openai_client import OpenAIClient
from app.memory.conversation_memory import ConversationMemory
from app.orchestrator.chat_orchestrator import ChatOrchestrator
from app.tools.tool_registry import TOOL_REGISTRY


class ChatOrchestratorFactory:
    """Creates configured chat orchestrator instances."""

    def create(
        self,
        memory: ConversationMemory,
    ) -> ChatOrchestrator:
        openai_client = OpenAIClient()

        expression_interpreter_agent = ExpressionInterpreterAgent(
            llm_client=openai_client.get_client(),
            model=openai_client.get_model(),
        )

        mathematical_agent = MathematicalAgent(
            tool_registry=TOOL_REGISTRY,
        )

        writer_agent = WriterAgent(
            llm_client=openai_client.get_client(),
            model=openai_client.get_model(),
        )

        return ChatOrchestrator(
            memory=memory,
            expression_interpreter_agent=expression_interpreter_agent,
            mathematical_agent=mathematical_agent,
            writer_agent=writer_agent,
        )