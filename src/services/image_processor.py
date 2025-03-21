import os
import time
import shutil
from core.config import ASSETS_DIR, PROCESSED_DIR, TASK_PROMPT
from core.handlers.gemini_handler import GeminiHandler
from services.document_service import DocumentService
from utils.file_utils import list_images
from services.markdown_service import MarkdownService

class ImageProcessor:
    def __init__(self):
        self.gemini_handler = GeminiHandler("gemini-2.0-flash-exp")
        self.document_service = DocumentService()
        self.markdown_service = MarkdownService()
        os.makedirs(PROCESSED_DIR, exist_ok=True)

    def process_images(self):
        images = list_images(ASSETS_DIR)
        if not images:
            print("❌ Nenhuma imagem encontrada em 'assets/'.")
            return

        for idx, image_name in enumerate(images, start=1):
            print(f"\n🔄 Processando imagem {idx}/{len(images)}: {image_name}")
            summary = self._process_image(image_name)
            self.document_service.add_image_summary(image_name, summary)
            self.markdown_service.add_image_summary(image_name, summary)
            self.document_service.save_document()
            self.markdown_service.save_markdown()
            self._move_image(image_name)
            if idx < len(images):
                print("⏳ Aguardando alguns segundos para próxima requisição...")
                time.sleep(7)

    def _process_image(self, image_name):
        img_path = os.path.join(ASSETS_DIR, image_name)
        try:
            response_text = self.gemini_handler.generate_content(img_path, TASK_PROMPT)
            print(f"✅ Resumo gerado para '{image_name}':\n{response_text}")
            return response_text
        except Exception as e:
            print(f"❌ Erro ao processar '{image_name}': {str(e)}")
            return f"Erro ao processar imagem: {str(e)}"

    def _move_image(self, image_name):
        origem = os.path.join(ASSETS_DIR, image_name)
        destino = os.path.join(PROCESSED_DIR, image_name)
        shutil.move(origem, destino)
        print(f"📂 Imagem '{image_name}' movida para '{PROCESSED_DIR}'.")