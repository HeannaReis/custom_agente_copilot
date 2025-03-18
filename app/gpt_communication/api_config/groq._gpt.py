import os
from dotenv import load_dotenv
from groq import Groq
from typing import Optional
import logging

class GroqHandler:
    def __init__(self, model_name: str):
        self.model_name: str = model_name
        self.client: Optional[Groq] = None
        self.api_key: Optional[str] = None
        self._load_env_variables()
        self._configure_client()

    def _load_env_variables(self) -> None:
        """Carregar variáveis do arquivo .env"""
        load_dotenv()
        self.api_key = os.getenv('GROQ_API_KEY')
        if not self.api_key:
            raise ValueError("API Key não encontrada nas variáveis de ambiente")

    def _configure_client(self) -> None:
        """Configurar o cliente Groq com a chave da API"""
        try:
            self.client = Groq(api_key=self.api_key)
        except Exception as e:
            raise RuntimeError(f"Erro ao configurar o cliente Groq: {e}")

    def generate_chat_completion(self, messages: list) -> str:
        """Gerar conclusão do chat com base nas mensagens fornecidas"""
        try:
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=self.model_name,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            logging.error(f"Erro ao gerar conclusão do chat: {e}")
            raise RuntimeError(f"Erro ao gerar conclusão do chat: {e}")

# Exemplo de uso
if __name__ == "__main__":
    groq_handler = GroqHandler(model_name="llama3-8b-8192")
    messages = [
        {
            "role": "user",
            "content": "Boa tarde, sabe dizer que dia é hoje?",
        }
    ]
    response = groq_handler.generate_chat_completion(messages)
    print(response)