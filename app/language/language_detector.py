from app.configuration.config import Config


class LanguageDetector:
    """
    Detects the language used by the user message.

    Default language is Brazilian Portuguese.
    """

    LANGUAGE_KEYWORDS = {
        "pt-BR": [
            "quanto",
            "calcule",
            "some",
            "soma",
            "subtraia",
            "multiplique",
            "divida",
            "agora",
            "resultado",
        ],
        "en": [
            "what",
            "calculate",
            "add",
            "subtract",
            "multiply",
            "now",
            "that",
            "by",
            "result",
        ],
        "es": [
            "cuánto",
            "calcula",
            "suma",
            "resta",
            "multiplica",
            "divide",
            "ahora",
            "resultado",
            "el",
            "por",
        ],
    }

    @classmethod
    def detect(cls, user_message: str) -> str:
        message = user_message.lower()

        scores = {
            language: sum(
                1 for keyword in keywords if keyword in message
            )
            for language, keywords in cls.LANGUAGE_KEYWORDS.items()
        }

        detected_language = max(scores, key=scores.get)

        if scores[detected_language] == 0:
            return Config.DEFAULT_LANGUAGE

        return detected_language