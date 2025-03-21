import os
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
TIMESTAMP = datetime.now().strftime("%Y%m%d%H%M%S")
PROCESSED_DIR = os.path.join(BASE_DIR, 'processed_images')
OUTPUT_DOCX = os.path.join(BASE_DIR, "resumo_analises_imagens.docx")
OUTPUT_MD = os.path.join(BASE_DIR, "resumo_analises_imagens.md")
TASK_PROMPT = (
    "Descreva em português de forma muito resumida e objetiva, sem ser repetitivo, qual o passo dos tópicos da aula que a imagem representa na criação de um agente no Copilot Studio. "
    "Se for uma configuração, explique que tipo de parâmetro ou ajuste está sendo realizado (exemplo: configuração de comportamento, adição de frases-gatilho, ou personalização de resposta). "
    "Se for um teste de conversação com o agente, explique que tipo de interação está sendo realizada "
    "(exemplo: teste de resposta, validação de ação, ou simulação de conversa). "
    "Não descrever textos que não fazem parte de configuração ou testes nas imagens, apenas forneça uma explicação sobre se é a configuração ou teste. "
    "Dar enfase nos processos marcados em vermelho e com setas vermelhas, pois são explicações passo a passo, mas nem todas as imagens tem."
    "Se houver texto em inglês, traduza-o para português, sendo breve e direto."
    "Tópicos da Aula"
    "Criar um Copilot em branco"
    "Customizar um tópico"
    "Personalizar uma mensagem de erro de tópico"
    "Aumentar e diminuir a qualidade da resposta com GenAI"
)