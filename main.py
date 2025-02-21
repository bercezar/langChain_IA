from dotenv import load_dotenv
import os

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq


load_dotenv()  # Carrega o arquivo .env
key_api = os.getenv("CROQ_API_KEY")

if key_api is None:
    print("Error: API KEY")
else:
    print("SUCCESSFUL: API KEY")

messages = [
    SystemMessage(),
    HumanMessage()
]

# Passando a chave da API com o nome correto do parâmetro
model = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=key_api)

response = model.invoke(messages)
print(response)
