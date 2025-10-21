# 🐱🐶 Classificador de Gatos e Cachorros

Projeto de Machine Learning usando Redes Neurais Convolucionais (CNN) para classificar imagens de gatos e cachorros com **alta precisão**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📊 Resultados

- **Acurácia:** 84.82% (coloque sua acurácia aqui!)
- **Dataset:** 25.000 imagens (Kaggle Dogs vs Cats)
- **Arquitetura:** CNN com 4 camadas convolucionais

## 🖼️ Demonstração

<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/f6f6c777-7ad0-4c9c-a7ce-ca6363f0f1c3" />

## 🎯 Funcionalidades

- ✅ Treinamento de modelo CNN do zero
- ✅ Data Augmentation para melhor generalização
- ✅ Validação com métricas detalhadas
- ✅ Visualização de resultados (gráficos e matriz de confusão)
- ✅ Predição em novas imagens
- ✅ Scripts auxiliares (limpeza de dados, separação treino/validação)

## 🚀 Como Usar

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/classificador-gatos-cachorros.git
cd classificador-gatos-cachorros
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Baixe o dataset
Baixe o dataset do Kaggle: [Dogs vs. Cats](https://www.kaggle.com/c/dogs-vs-cats/data)

Organize as imagens assim:

data/
├── train/
│   ├── cats/
│   └── dogs/
└── validation/
├── cats/
└── dogs/

### 4. (Opcional) Limpe imagens corrompidas
```bash
python limpar_imagens.py
```

### 5. Treine o modelo
```bash
python classificador_simples.py
```

### 6. Teste com suas imagens
```bash
python testar_imagem.py caminho/para/sua/imagem.jpg
```

## 📁 Estrutura do Projeto

classificador-gatos-cachorros/
├── classificador_simples.py    # Script principal de treinamento
├── testar_imagem.py            # Script para testar o modelo
├── separar_dados.py            # Separa dados treino/validação
├── limpar_imagens.py           # Remove imagens corrompidas
├── setup_projeto.py            # Configuração inicial
├── requirements.txt            # Dependências
├── README.md                   # Este arquivo
├── .gitignore                  # Arquivos ignorados pelo git
└── data/                       # Dados (não versionado)
├── train/
└── validation/

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **TensorFlow/Keras** - Deep Learning
- **NumPy** - Computação numérica
- **Matplotlib** - Visualização de dados
- **Pillow** - Processamento de imagens
- **Scikit-learn** - Métricas de avaliação

## 📈 Arquitetura do Modelo
Camada                  Output Shape         Parâmetros
Conv2D (32 filtros)     (148, 148, 32)       896
MaxPooling2D            (74, 74, 32)         0
Conv2D (64 filtros)     (72, 72, 64)         18,496
MaxPooling2D            (36, 36, 64)         0
Conv2D (128 filtros)    (34, 34, 128)        73,856
MaxPooling2D            (17, 17, 128)        0
Conv2D (128 filtros)    (15, 15, 128)        147,584
MaxPooling2D            (7, 7, 128)          0
Flatten                 (6272)               0
Dropout (0.5)           (6272)               0
Dense (512)             (512)                3,211,776
Dense (1)               (1)                  513
Total: ~3.5M parâmetros

## 📊 Métricas de Avaliação

- **Acurácia:** 84.82%
- **Precisão:** XX.XX%
- **Recall:** XX.XX%
- **F1-Score:** XX.XX%

## 🎓 Aprendizados

- Implementação de CNNs do zero
- Técnicas de Data Augmentation
- Transfer Learning (próxima etapa)
- Avaliação de modelos de classificação

## 🔮 Próximas Melhorias

- [ ] Implementar Transfer Learning (VGG16, ResNet)
- [ ] Criar interface web com Streamlit
- [ ] Adicionar mais categorias de animais
- [ ] Deploy em nuvem (Heroku, AWS, etc.)
- [ ] Criar API REST
- [ ] App mobile

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Seu Nome**
- GitHub: [@maricarminate](https://github.com/maricarminate)
- LinkedIn: [Mariana Carminate](www.linkedin.com/in/mariana-santos-carminate-0a0893133)

## 🙏 Agradecimentos

- Dataset fornecido por [Kaggle - Dogs vs. Cats](https://www.kaggle.com/c/dogs-vs-cats)
- Inspirado em projetos da comunidade de ML

---

⭐ Se este projeto te ajudou, considere dar uma estrela!
