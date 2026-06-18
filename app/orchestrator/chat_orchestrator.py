from app.agents.expression_interpreter_agent import (
    ExpressionInterpreterAgent,
)
from app.agents.mathematical_agent import MathematicalAgent
from app.agents.writer_agent import WriterAgent
from app.language.language_detector import LanguageDetector
from app.memory.conversation_memory import ConversationMemory


class ChatOrchestrator:
    """
    Coordinates the interaction between memory and agents.
    """

    def __init__(
        self,
        memory: ConversationMemory,
        expression_interpreter_agent: ExpressionInterpreterAgent,
        mathematical_agent: MathematicalAgent,
        writer_agent: WriterAgent,
    ) -> None:
        self._memory = memory
        self._expression_interpreter_agent = expression_interpreter_agent
        self._mathematical_agent = mathematical_agent
        self._writer_agent = writer_agent

    def process_message(
        self,
        user_message: str,
    ) -> str:
        self._memory.add_user_message(user_message)

        try:
            language = LanguageDetector.detect(user_message)
            self._memory.set_language(language)

            interpreted_expression = (
                self._expression_interpreter_agent.interpret(
                    user_message=user_message,
                    last_result=self._memory.get_last_result(),
                )
            )

            calculation = self._mathematical_agent.calculate(
                expression=interpreted_expression["expression"],
            )

            self._memory.set_last_result(
                calculation["result"],
            )

            response = self._writer_agent.generate_response(
                calculation_result=calculation,
                user_message=user_message,
                language=self._memory.get_language(),
            )

        except ValueError as error:
             response = self._writer_agent.generate_response(
                calculation_result={
                    "operation": "error",
                    "operands": None,
                    "result": str(error),
                },
                user_message=user_message,
                language=self._memory.get_language(),
            )

        self._memory.add_assistant_message(response)

        return response