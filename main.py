import streamlit as st

from app.agents.expression_interpreter_agent import ExpressionInterpreterAgent
from app.agents.mathematical_agent import MathematicalAgent
from app.agents.writer_agent import WriterAgent
from app.clients.openai_client import OpenAIClient
from app.memory.conversation_memory import ConversationMemory
from app.orchestrator.chat_orchestrator import ChatOrchestrator
from app.tools.tool_registry import TOOL_REGISTRY


st.set_page_config(
    page_title="Multi-Agent Math Assistant",
    page_icon="🧮",
    layout="wide",
)


st.markdown(
    """
    <style>
        .stApp {
            background-color: #111827;
            color: #f3f4f6;
        }

        section[data-testid="stSidebar"] {
            background-color: #0f172a;
        }

        div[data-testid="stMetric"] {
            background-color: #1f2937;
            padding: 12px;
            border-radius: 10px;
            border: 1px solid #374151;
        }

        .welcome-card {
            background-color: #1f2937;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #374151;
            margin-bottom: 20px;
        }

        .muted-text {
            color: #cbd5e1;
            font-size: 14px;
        }

        .example-item {
            margin-bottom: 6px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def get_last_user_message() -> str:
    messages = st.session_state.memory.get_messages()

    for message in reversed(messages):
        if message["role"] == "user":
            return message["content"]

    return "—"


if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()


if "orchestrator" not in st.session_state:
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

    st.session_state.orchestrator = ChatOrchestrator(
        memory=st.session_state.memory,
        expression_interpreter_agent=expression_interpreter_agent,
        mathematical_agent=mathematical_agent,
        writer_agent=writer_agent,
    )


messages = st.session_state.memory.get_messages()
last_result = st.session_state.memory.get_last_result()
last_user_message = get_last_user_message()


with st.sidebar:
    st.markdown("## 📊 Sessão")

    st.metric(
        label="Mensagens",
        value=len(messages),
    )

    st.metric(
        label="Último resultado",
        value=(
            last_result
            if last_result is not None
            else "-"
        ),
    )

    st.markdown(
        f"""
        <div style="
            background-color:#1f2937;
            padding:12px;
            border-radius:10px;
            border:1px solid #374151;
            margin-top:12px;
        ">
            <p class="muted-text">Última mensagem</p>
            <p>{last_user_message}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### 🧠 Recursos")

    st.markdown(
        """
        - Memória contextual
        - Multi-idioma
        - Ferramentas matemáticas
        - Agentes especializados
        """
    )

    st.divider()

    if st.button(
        "🗑️ Nova conversa",
        use_container_width=True,
    ):
        st.session_state.memory.clear()
        st.rerun()


st.markdown("# 🧮 Multi-Agent Math Assistant")

st.caption(
    """
    Resolva operações matemáticas utilizando agentes especializados,
    memória contextual e ferramentas dedicadas.
    """
)


st.markdown(
    """
<div class="welcome-card">

### 💡 Experimente algumas mensagens

- Calcule: (18 + 6) ÷ 3
- Multiplique o resultado por 4
- Tenho 6 caixas com 12 itens cada e perdi 9
- Quanto é 125 dividido por 5?
- What is five plus four?
- Ahora divide el resultado por 2

</div>
""",
    unsafe_allow_html=True,
)


for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Digite uma mensagem"):
    response = st.session_state.orchestrator.process_message(prompt)
    st.rerun()