import os

from dotenv import load_dotenv
from openai import OpenAI

from app.configuration.config import Config

load_dotenv()


class OpenAIClient:
    """
    Creates and provides the OpenAI client.
    """

    def __init__(self) -> None:
        self._client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    def get_client(self) -> OpenAI:
        return self._client

    def get_model(self) -> str:
        return Config.MODEL_NAME