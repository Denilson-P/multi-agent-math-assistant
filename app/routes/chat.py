from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.orchestrator.chat_orchestrator_factory import (
    ChatOrchestratorFactory,
)
from app.memory.conversation_memory import ConversationMemory

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        description="Message sent by the user.",
    )


class ChatResponse(BaseModel):
    response: str
    result: float | None = None


memory = ConversationMemory()
orchestrator = ChatOrchestratorFactory().create(
    memory=memory,
)


@router.post(
    "",
    response_model=ChatResponse,
)
def send_message(
    request: ChatRequest,
) -> ChatResponse:
    orchestrator.process_message(request.message)

    messages = memory.get_messages()
    last_result = memory.get_last_result()

    assistant_messages = [
        message
        for message in messages
        if message["role"] == "assistant"
    ]

    response_text = assistant_messages[-1]["content"]

    return ChatResponse(
        response=response_text,
        result=last_result,
    )