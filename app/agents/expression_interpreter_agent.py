import json

from openai import OpenAI

from app.prompts.expression_interpreter_prompt import (
    EXPRESSION_INTERPRETER_PROMPT,
)


class ExpressionInterpreterAgent:
    """
    Agent responsible for converting natural language into
    a mathematical expression.

    This agent must not calculate.
    """

    def __init__(
        self,
        llm_client: OpenAI,
        model: str,
    ) -> None:
        self._llm_client = llm_client
        self._model = model

    def interpret(
        self,
        user_message: str,
        last_result: float | None = None,
    ) -> dict:
        response = self._llm_client.chat.completions.create(
            model=self._model,
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": EXPRESSION_INTERPRETER_PROMPT,
                },
                {
                    "role": "user",
                    "content": (
                        f"User message: {user_message}\n"
                        f"Previous result: {last_result}"
                    ),
                },
            ],
        )

        content = response.choices[0].message.content

        try:
            result = json.loads(content)
        except json.JSONDecodeError as error:
            raise ValueError(
                "Could not interpret the mathematical request."
            ) from error

        if result is None or result.get("expression") is None:
            raise ValueError(
                "Please provide a mathematical operation."
            )
    
        return result