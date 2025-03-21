import os
import base64
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional
import logging

class GenerativeModelHandler:
    def __init__(self, model_name: str):
        self.model_name: str = model_name
        self.model: Optional[genai.GenerativeModel] = None
        self.api_key: Optional[str] = None
        self._load_env_variables()
        self._configure_api()
        self._initialize_model()

    def _load_env_variables(self) -> None:
        load_dotenv()
        self.api_key = os.getenv('API_KEY_GEMINI')
        if not self.api_key:
            raise ValueError("API Key não encontrada nas variáveis de ambiente")

    def _configure_api(self) -> None:
        genai.configure(api_key=self.api_key)

    def _initialize_model(self) -> None:
        try:
            self.model = genai.GenerativeModel(self.model_name)
        except Exception as e:  
            raise RuntimeError(f"Erro ao inicializar o modelo: {e}")

    def generate_content_from_image(self, image_path: str, prompt: str) -> str:
        try:
            with open(image_path, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

            response = self.model.generate_content([
                {"mime_type": "image/png", "data": image_base64},
                prompt
            ])

            return response.text
        except Exception as e:
            logging.error(f"Erro ao processar a imagem: {e}")
            raise RuntimeError(f"Erro ao processar a imagem: {e}")