#chat_bot
import os
from dotenv import load_dotenv

#Carregar variáveis do arquivo .env
load_dotenv()

#Imports corrigidos para versão atual do LangChain
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import BaseChatMessageHistory
from langchain.memory import ChatMessageHistory

#Template do sistema
template = """Você é um chat de conversa simples. Comece com: Oi, bom dia!:

Histórico: 
{history}

Entrada do usuário: 
{input}"""

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

#Definição do modelo
llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")

#Dicionário para armazenar históricos de sessão
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def iniciar_assistente():
    print("Bem vindo! Como posso ajudar? Digite 'sair' para encerrar.\n ")
    session_id = "user123"

    while True:
        pergunta_usuario = input('Você: ')

        if pergunta_usuario.lower() in ['sair', 'exit']:
            print('IA: Até a próxima!')
            break

        #recuperar histórico da sessão
        history = get_session_history(session_id)

        #montar prompt com histórico
        response = llm.invoke(
            prompt.format_messages(input=pergunta_usuario, history=history.messages)
        )

        #salvar no histórico
        history.add_user_message(pergunta_usuario)
        history.add_ai_message(response.content)

        print('IA:', response.content)

if __name__ == "__main__":
    iniciar_assistente()
