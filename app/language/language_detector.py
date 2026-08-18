import re

from app.configuration.config import Config


class LanguageDetector:
    """
    Detects the language used by the user message.

    Default language is Brazilian Portuguese.
    """

    LANGUAGE_KEYWORDS = {
        "pt-BR": {
            "quanto",
            "calcule",
            "some",
            "soma",
            "mais",
            "subtraia",
            "menos",
            "multiplique",
            "divida",
            "dividido",
            "agora",
            "resultado",
            "por",
            "zero",
            "um",
            "uma",
            "dois",
            "duas",
            "três",
            "quatro",
            "cinco",
            "seis",
            "sete",
            "oito",
            "nove",
            "dez",
        },
        "en": {
            "what",
            "calculate",
            "add",
            "plus",
            "sum",
            "subtract",
            "minus",
            "multiply",
            "times",
            "divide",
            "divided",
            "now",
            "that",
            "by",
            "result",
            "is",
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
        },
        "es": {
            "cuánto",
            "calcula",
            "suma",
            "más",
            "resta",
            "menos",
            "multiplica",
            "divide",
            "dividido",
            "ahora",
            "resultado",
            "el",
            "por",
            "cero",
            "uno",
            "dos",
            "tres",
            "cuatro",
            "cinco",
            "seis",
            "siete",
            "ocho",
            "nueve",
            "diez",
        },
    }

    @classmethod
    def detect(cls, user_message: str) -> str:
        words = set(
            re.findall(
                r"\b[\wÀ-ÿ]+\b",
                user_message.lower(),
            )
        )

        scores = {
            language: len(words & keywords)
            for language, keywords in cls.LANGUAGE_KEYWORDS.items()
        }

        detected_language = max(
            scores,
            key=scores.get,
        )

        if scores[detected_language] == 0:
            return Config.DEFAULT_LANGUAGE

        return detected_language