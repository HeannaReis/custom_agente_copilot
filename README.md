# Projeto: Criando um Copiloto com Fluxo de Conversa Personalizado no Microsoft Copilot Studio

## Descrição do Projeto
Este projeto foi desenvolvido como parte do curso **"Criando um Copiloto com Fluxo de Conversa Personalizado no Microsoft Copilot Studio"**. O desafio era documentar o passo a passo da criação de agentes no Copilot Studio, seguindo as diretrizes das aulas. Para isso, foi criada uma aplicação que utiliza **OCR (Reconhecimento Óptico de Caracteres)** e **engenharia de prompt** para gerar uma documentação automatizada dos prints capturados durante o processo de criação dos agentes.

## Objetivo do Projeto
A aplicação tem como objetivo **automatizar a documentação** do processo de criação de agentes no Copilot Studio, gerando uma documentação detalhada e explicativa das imagens capturadas durante esse processo, tudo de forma automatizada utilizando Inteligência Artificial.

## Benefícios do Projeto
- **Automatização da Documentação**: A aplicação automatiza a criação de documentos descritivos, economizando tempo e esforço manual.
- **Consistência e Precisão**: Utilizando OCR e engenharia de prompt, a aplicação garante que os resumos sejam consistentes e precisos.
- **Facilidade de Uso**: Com uma interface simples e clara, a aplicação pode ser utilizada por desenvolvedores de todos os níveis de experiência.
- **Flexibilidade**: A geração de documentos em dois formatos (**Word e Markdown**) permite que os usuários escolham o formato que melhor se adapta às suas necessidades.
- **Melhoria na Comunicação**: Documentos bem estruturados e detalhados melhoram a comunicação dentro das equipes e com stakeholders.

## Markdown Gerado
O arquivo Markdown gerado pela aplicação contém os links das imagens processadas e já serve como um **pré-README** da aplicação, pronto para ser conferido e publicado.

## Passo a Passo para Utilizar a Aplicação

### 1. Clone o Repositório
Clone o repositório da aplicação do GitHub para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/custom_agente_copilot
cd custom_agente_copilot
```

### 2. Instale as Dependências
Certifique-se de ter o **Python** instalado. Em seguida, instale as dependências necessárias utilizando o **pip**:

```bash
pip install -r requirements.txt
```

### 3. Configure o Arquivo `.env`
No diretório raiz do projeto, crie um arquivo `.env` e adicione a chave da API GPT Gemini 2.0:

```plaintext
GEMINI_API_KEY=your_api_key_here
```
> ⚠️ **Atenção**: Para utilizar esta aplicação, é necessário obter uma chave de API da Google AI Studio.  
> Você pode obter a sua chave em [Google AI Studio](https://aistudio.google.com/).

### 4. Configure os Diretórios
Certifique-se de que os diretórios `assets` e `processed_images` estejam configurados corretamente. Coloque as imagens que deseja processar dentro do diretório `assets`.

### 5. Execute a Aplicação
Execute o script principal para iniciar o processamento das imagens:

```bash
python src/main.py
```

### 6. Verifique os Resultados
Após a execução, verifique os arquivos gerados `resumo_analises_imagens.docx` e `resumo_analises_imagens.md` no diretório principal do projeto. Esses arquivos conterão os resumos das imagens processadas, com o arquivo **Markdown** já contendo os links das imagens.

### 7. Personalize se Necessário
Se necessário, você pode personalizar os prompts e outras configurações no arquivo `config.py` para atender às suas necessidades específicas.

## Impacto na Vida das Pessoas
A aplicação desenvolvida tem um impacto significativo na vida das pessoas, especialmente para **desenvolvedores e equipes que trabalham com documentação visual**. Ao automatizar a análise e documentação de imagens, a aplicação economiza tempo e esforço, permitindo que os profissionais se concentrem em tarefas mais importantes e estratégicas. Além disso, a **consistência e precisão** dos resumos gerados melhoram a qualidade da documentação, facilitando a comunicação e a colaboração dentro das equipes.



## Conteúdo do Curso
### Apresentação do Desafio
### Criar um Copilot em branco
### Customizar um tópico
### Personalizar uma mensagem de erro de tópico
### Aumentar e diminuir a qualidade da resposta com GenAI
### Entendendo o Desafio


# Guia de Criação de Agentes no Copilot Studio

# Resumo das Análises das Imagens

## 1. Imagem: custom_agent_1.png
![Tela Inicial de Criação do Agente](/processed_images/custom_agent_1.png)  
A imagem representa a tela inicial de criação de um novo agente no Copilot Studio. O usuário pode criar um novo agente do zero ou explorar agentes pré-definidos para diversas finalidades, como viagens seguras, perguntas e respostas do site e navegador de equipes.

## 2. Imagem: custom_agent_2.png
![Configuração do Objetivo Principal do Agente](/processed_images/custom_agent_2.png)  
A imagem representa uma etapa de configuração na criação de um agente no Copilot Studio, onde o usuário está definindo o objetivo principal do agente. O sistema confirma o nome do agente ("Microsoft Consultant Agent") e solicita que o usuário especifique qual é o principal objetivo do agente.

## 3. Imagem: custom_agent_3.png
![Configuração do Agente com Regras de Comportamento](/processed_images/custom_agent_3.png)  
A imagem demonstra a configuração do agente Microsoft Consultant Agent no Copilot Studio. Nela, são definidos o objetivo do agente, que é atuar como um assistente especializado para desenvolvedores, utilizando exclusivamente a documentação oficial da Microsoft, e suas regras de comportamento.

## 4. Imagem: custom_agent_4.png
![Exemplo de Estilo de Resposta do Agente](/processed_images/custom_agent_4.png)  
A imagem mostra exemplos de estilo de resposta configurados para um agente no Copilot Studio. São mostradas perguntas e respostas personalizadas para o agente, incluindo um exemplo que compara a criação de uma entidade personalizada à montagem de uma pizza.

## 5. Imagem: custom_agent_5.png
![Finalização da Configuração do Agente](/processed_images/custom_agent_5.png)  
A imagem representa a etapa final da configuração de um agente no Copilot Studio, onde as regras e o comportamento foram definidos e o nome do agente ("Microsoft Consultant Agent") foi confirmado. O próximo passo é clicar em "Criar" para finalizar a criação do agente.

## 6. Imagem: custom_agent_6.png
![Configuração do Agente com Descrição e Instruções](/processed_images/custom_agent_6.png)  
A imagem representa uma etapa de Teste Inicial do agente no Copilot Studio. Especificamente, o comportamento definido na descrição e as instruções do agente, incluindo como ele deve responder, o tom a ser utilizado e como utilizar analogias para facilitar o entendimento.

## 7. Imagem: custom_agent_7.png
![Configuração do Agente com Teste](/processed_images/custom_agent_7.png)  
Continuidade do teste acima.

## 8. Imagem: custom_agent_8.png
![Edição de Frases-Gatilho](/processed_images/custom_agent_8.png)  
A imagem mostra a tela de edição das frases-gatilho de um tópico no Microsoft Copilot Studio. O usuário está no processo de adicionar ou modificar as frases que iniciarão a conversa com o agente.

## 9. Imagem: custom_agent_9.png
![Adicionar Frases-Gatilho](/processed_images/custom_agent_9.png)  
A imagem demonstra a etapa de adicionar frases-gatilho (phrases) para um tópico específico no Copilot Studio. O usuário está adicionando frases ou perguntas que os usuários podem usar para acionar este tópico.

## 10. Imagem: custom_agent_10.png
![Adicionar Nó ao Gatilho do Tópico](/processed_images/custom_agent_10.png)  
A imagem representa a adição de um nó ao gatilho do tópico no Copilot Studio. As frases abaixo são os gatilhos para o fluxo da conversa. Ao clicar no "+", o usuário adicionará um novo elemento ao fluxo da conversa.

## 11. Imagem: custom_agent_11.png
![Adicionar Respostas Generativas](/processed_images/custom_agent_11.png)  
A imagem representa a etapa de adicionar uma ação avançada do tipo "Respostas generativas" ao fluxo de diálogo do agente no Copilot Studio.

## 12. Imagem: custom_agent_12.png
![Configuração de Respostas Generativas](/processed_images/custom_agent_12.png)  
A imagem mostra uma etapa de configuração de um nó "Criar respostas generativas" no Copilot Studio. O usuário está selecionando a variável "Activity.Text" como entrada para o nó.

## 13. Imagem: custom_agent_13.png
![Fluxo de Conversa com Mensagem](/processed_images/custom_agent_13.png)  
A imagem representa a criação de um fluxo de conversa no Copilot Studio. Mais especificamente, mostra a adição de um nó de mensagem para responder ao usuário com o texto "Tópico de criação e Gerenciamento de Menus encerrado".

## 14. Imagem: custom_agent_14.png
![Guia para Criar e Gerenciar Ações](/processed_images/custom_agent_14.png)  
Testes do Agente após tópicos e IA Generativa adicionados.

## 15. Imagem: custom_agent_15.png
![Adicionar e Configurar Ações](/processed_images/custom_agent_15.png)  
Testes do Agente após tópicos e IA Generativa adicionados.

## 16. Imagem: custom_agent_16.png
![Gerenciamento de Ações](/processed_images/custom_agent_16.png)  
Testes do Agente após tópicos e IA Generativa adicionados.

## 17. Imagem: custom_agent_17.png
![Teste e Documentação das Ações](/processed_images/custom_agent_17.png)  
Testes do Agente após tópicos e IA Generativa adicionados.

## 18. Imagem: custom_agent_18.png
![Reutilização de Ações](/processed_images/custom_agent_18.png)  
Testes do Agente após tópicos e IA Generativa adicionados.

# Personalizar uma mensagem de Erro de tópico.

Create generative answers from knowledge sources.
Esse tópico do sistema é disparado quando o bot precisa conectar o usuário ou exige que o usuário entre no serviço


## Imagem: custom_topic_message_1.png
![custom_topic_message_1.png](/processed_images/custom_topic_message_1.png)

A imagem mostra a seção de "Tópicos" no Copilot Studio, especificamente os "Tópicos do Sistema". Os tópicos do sistema são necessários para que o agente funcione corretamente, e não podem ser excluídos. Os tópicos em destaque são:

*   **Conversational boosting:** Este tópico é ativado para criar respostas generativas a partir de fontes de conhecimento.

*   **Fallback:** Este tópico é ativado quando o enunciado do usuário não corresponde a nenhum tópico existente.

## Imagem: custom_topic_2.png
![custom_topic_2.png](/processed_images/custom_topic_2.png)

A imagem representa a configuração de um tópico no Copilot Studio, especificamente nas "Propriedades de Criar respostas generativas". Está sendo ajustada a permissão para que a IA utilize seus próprios conhecimentos gerais (versão preliminar). Além disso, a imagem indica a necessidade de salvar as alterações realizadas.


## Imagem: custom_quality_1.png
![custom_quality_1.png](/processed_images/custom_quality_1.png)

A imagem demonstra a configuração das propriedades de "Criar respostas generativas" no Copilot Studio. Especificamente, o ajuste destacado em vermelho é a opção para "Pesquisar somente fontes selecionadas" nas fontes de conhecimento. Isso controla se o agente deve buscar respostas apenas nas fontes de dados especificamente configuradas ou em todas as fontes disponíveis.


## Imagem: custom_topic_3.png
![custom_topic_3.png](/processed_images/custom_topic_3.png)

A imagem mostra a configuração para aumentar e diminuir a qualidade da resposta com GenAI no Microsoft Copilot Studio. Especificamente, as configurações destacadas em vermelho permitem:

1.  **Fontes de conhecimento:**  Habilitar ou desabilitar a pesquisa apenas nas fontes de dados selecionadas.
2.  **Dados clássicos:**  Permitir ou impedir que a IA utilize seus próprios conhecimentos gerais para gerar respostas (recurso em versão preliminar).

## Imagem: custom_prompt_4.png
![custom_prompt_4.png](/processed_images/custom_prompt_4.png)

A imagem representa a configuração do nível de moderação de conteúdo e a personalização do prompt para a criação de respostas generativas em um tópico do Copilot Studio. O usuário pode selecionar o nível de moderação (neste caso, "Alto") e personalizar o prompt com variáveis e linguagem clara, definindo como o agente responderá às entradas dos usuários.


## Imagem: custom_agent_topic_5.png
![custom_agent_topic_5.png](/processed_images/custom_agent_topic_5.png)

A imagem representa a configuração do nível de moderação de conteúdo de um tópico, com a opção "Personalizar" selecionada e o nível definido como "Alto". Também mostra a área para personalizar o prompt com variáveis para uma linguagem clara.


## Imagem: custom_agent_topic_6.png
![custom_agent_topic_6.png](/processed_images/custom_agent_topic_6.png)

A imagem representa a configuração da IA Generativa no Copilot Studio, onde se define como o agente deve interagir com as pessoas. As opções são: "Clássico" (usar os tópicos criados) ou "Generativa" (usar a IA generativa para responder). Também se ajusta a rigorosidade da moderação de conteúdo, variando de "Baixo" (mais criativo) a "Alto" (mais preciso). Um aviso indica que o uso da IA generativa para selecionar tópicos/ações está disponível apenas para agentes em inglês.


