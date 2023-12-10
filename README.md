# Projeto-Final-Processamento-de-Imagens
## Projeto de Extração e Classificação de Características em Imagens
O projeto será composto pela implementação de script Python para classificação de imagens raio-X dividias em duas classes: covid e normal.

# Equipe: Jhonatan Sampaio

Este é um script em Python para processamento de imagens usando momentos de Hu e classificação com um classificador SVM. O script é projetado para trabalhar com conjuntos de dados divididos em conjuntos de treinamento e teste.

# Momentos de Hu
Os momentos de Hu são descritores de forma invariantes a rotação, escala e translação de uma imagem. Eles são derivados dos momentos estatísticos da imagem e são amplamente utilizados em processamento de imagem para caracterizar a forma de objetos. Os momentos de Hu capturam informações sobre a distribuição espacial de intensidades na imagem e são especialmente úteis para representar características globais da forma.

No contexto deste projeto, os momentos de Hu são extraídos de imagens para criar um conjunto de características que serve como entrada para um classificador SVM (Support Vector Machine). Este classificador é treinado para reconhecer padrões nos momentos de Hu e, posteriormente, é utilizado para classificar imagens de teste.

Referências
Hu, M. K. "Visual Pattern Recognition by Moment Invariants." (1962)
## Requisitos

- Python 3
- Bibliotecas Python: numpy, opencv-python, scikit-learn, progress, entre outras. 
## Como usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/jhosampaio/Projeto-Final-Processamento-de-Imagens.git
   cd Projeto-Final-Processamento-de-Imagens

2. Configure seu ambiente virtual
   python -m venv venv
   source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'

3. Instale as dependências:
   pip install -r requirements.txt
4. Adicione as images: Para esse projeto foram usadas essas: [Kaggle](https://www.kaggle.com/datasets/tarandeep97/covid19-normal-posteroanteriorpa-xrays)

Coloque suas imagens de treinamento em ./images_split/train/.  
Coloque suas imagens de teste em ./images_split/test/.

5. Execute!

