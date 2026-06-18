from openai import OpenAI

from app.prompts.writer_prompt import WRITER_AGENT_PROMPT


ERROR_MESSAGES = {
    "division_by_zero": (
        "The user attempted to divide a number by zero."
    ),
    "invalid_expression": (
        "The mathematical expression could not be interpreted."
    ),
    "calculation_error": (
        "An unexpected error occurred while processing the calculation."
    ),
}


class WriterAgent:
    """
    Agent responsible for creating user-friendly responses.

    This agent must never perform calculations.
    """

    def __init__(
        self,
        llm_client: OpenAI,
        model: str,
    ) -> None:
        self._llm_client = llm_client
        self._model = model

    def generate_response(
        self,
        calculation_result: dict,
        user_message: str,
        language: str,
    ) -> str:
        operation = calculation_result.get("operation")
        operands = calculation_result.get("operands")
        result = calculation_result.get("result")

        if operation == "error":
            error_description = ERROR_MESSAGES.get(
                result,
                result,
            )

            user_content = (
                f"Detected language: {language}\n"
                f"Original user message: {user_message}\n"
                f"Error description: {error_description}\n"
                "Create a friendly and natural error response. "
                "Do not return the raw error code."
            )

        else:
            user_content = (
                f"Detected language: {language}\n"
                f"Original user message: {user_message}\n"
                f"Expression: {operands}\n"
                f"Tool result: {result}\n"
                "Create a friendly and natural response."
            )

        response = self._llm_client.chat.completions.create(
            model=self._model,
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": WRITER_AGENT_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_content,
                },
            ],
        )

        return response.choices[0].message.content