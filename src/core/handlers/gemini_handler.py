from services.gpt_services import GenerativeModelHandler

class GeminiHandler:
    def __init__(self, model_name):
        self.handler = GenerativeModelHandler(model_name)

    def generate_content(self, img_path, prompt):
        return self.handler.generate_content_from_image(img_path, prompt)