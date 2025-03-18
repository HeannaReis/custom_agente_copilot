import os
import base64
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional
import logging
import base64

class GenerativeModelHandler:
    def __init__(self, model_name: str):
        self.model_name: str = model_name
        self.model: Optional[genai.GenerativeModel] = None
        self.api_key: Optional[str] = None
        self._load_env_variables()
        self._configure_api()
        self._initialize_model()

    def _load_env_variables(self) -> None:
        """Carregar variáveis do arquivo .env"""
        load_dotenv()
        self.api_key = os.getenv('API_KEY_GEMINI')
        if not self.api_key:
            raise ValueError("API Key não encontrada nas variáveis de ambiente")

    def _configure_api(self) -> None:
        """Configurar a chave da API"""
        genai.configure(api_key=self.api_key)

    def _initialize_model(self) -> None:
        """Inicializar o modelo generativo"""
        try:
            self.model = genai.GenerativeModel(self.model_name)
        except Exception as e:  
            raise RuntimeError(f"Erro ao inicializar o modelo: {e}")

    def generate_content(self, prompt: str, title: str, description: str) -> str:
        """Gerar conteúdo com base no prompt, título e descrição"""
        try:
            request_data = f'''
                "prompt": {prompt},
                "title": {title},
                "description": {description}
            '''
            print(f"Enviando requisição para a API GenAI: {request_data}")

            response = self.model.generate_content(request_data)
            return response.text
        except Exception as e:
            raise RuntimeError(f"Erro ao gerar conteúdo: {e}")

    def generate_content_with_image_data(self, image_path: str, prompt: str) -> str:
        """Gerar conteúdo a partir de uma imagem e um prompt dinâmico"""
        try:
            # Lê a imagem e converte para Base64
            with open(image_path, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

            # Envia a requisição para a API Gemini com a imagem em Base64 e o prompt fornecido
            response = self.model.generate_content([
                {"mime_type": "image/png", "data": image_base64},  # A imagem em Base64
                prompt  # O prompt dinâmico passado como argumento
            ])

            return response.text
        except Exception as e:
            logging.error(f"Erro ao processar a imagem: {e}")
            raise RuntimeError(f"Erro ao processar a imagem: {e}")
