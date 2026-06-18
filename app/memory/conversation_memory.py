from typing import Any


class ConversationMemory:
    """
    Stores conversation history, latest result and current language.
    """

    def __init__(self) -> None:
        self._messages: list[dict[str, str]] = []
        self._last_result: Any = None
        self._language = "pt-BR"

    def add_user_message(self, content: str) -> None:
        self._messages.append(
            {
                "role": "user",
                "content": content,
            }
        )

    def add_assistant_message(self, content: str) -> None:
        self._messages.append(
            {
                "role": "assistant",
                "content": content,
            }
        )

    def get_messages(self) -> list[dict[str, str]]:
        return self._messages

    def set_last_result(self, result: Any) -> None:
        self._last_result = result

    def get_last_result(self) -> Any:
        return self._last_result

    def set_language(self, language: str) -> None:
        self._language = language

    def get_language(self) -> str:
        return self._language

    def clear(self) -> None:
        self._messages.clear()
        self._last_result = None
        self._language = "pt-BR"