print("🚀 INICIANDO CLASSIFICADOR DE GATOS E CACHORROS")
print("=" * 70)

# Imports
print("\n[ETAPA 1/6] Importando bibliotecas...")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Reduz logs do TensorFlow

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
print("✅ Bibliotecas importadas!")

# Configurações
IMG_SIZE = 150
BATCH_SIZE = 32
EPOCHS = 10  # Reduzido para 10 para ser mais rápido

print("\n[ETAPA 2/6] Preparando dados...")
print(f"   Tamanho das imagens: {IMG_SIZE}x{IMG_SIZE}")
print(f"   Batch size: {BATCH_SIZE}")
print(f"   Épocas de treinamento: {EPOCHS}")

# Geradores de dados
DIRETORIO_TREINO = 'data/train'
DIRETORIO_VALIDACAO = 'data/validation'

print(f"\n   Carregando de: {DIRETORIO_TREINO}")

# Gerador de treino com augmentação
treino_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True
)

# Gerador de validação (apenas normalização)
validacao_datagen = ImageDataGenerator(rescale=1./255)

# Carregar imagens
treino_generator = treino_datagen.flow_from_directory(
    DIRETORIO_TREINO,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

validacao_generator = validacao_datagen.flow_from_directory(
    DIRETORIO_VALIDACAO,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

print("✅ Dados preparados!")
print(f"   Classes encontradas: {list(treino_generator.class_indices.keys())}")

# Criar modelo
print("\n[ETAPA 3/6] Criando modelo de rede neural...")

modelo = keras.Sequential([
    # Camada 1
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    layers.MaxPooling2D(2, 2),
    
    # Camada 2
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    
    # Camada 3
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    
    # Camada 4
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    
    # Camadas finais
    layers.Flatten(),
    layers.Dropout(0.5),
    layers.Dense(512, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

modelo.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

print("✅ Modelo criado!")
print("\n📊 Arquitetura do modelo:")
modelo.summary()

# Treinar
print("\n[ETAPA 4/6] INICIANDO TREINAMENTO...")
print("⏰ Isso pode demorar de 10 minutos a 1 hora dependendo do seu computador")
print("💡 Você verá o progresso de cada época abaixo:\n")

# Callback para mostrar progresso
class ProgressCallback(keras.callbacks.Callback):
    def on_epoch_begin(self, epoch, logs=None):
        print(f"\n{'='*70}")
        print(f"📍 ÉPOCA {epoch + 1}/{EPOCHS}")
        print(f"{'='*70}")
    
    def on_epoch_end(self, epoch, logs=None):
        print(f"\n✅ Época {epoch + 1} concluída!")
        print(f"   📈 Acurácia Treino: {logs['accuracy']:.4f} ({logs['accuracy']*100:.2f}%)")
        print(f"   📊 Acurácia Validação: {logs['val_accuracy']:.4f} ({logs['val_accuracy']*100:.2f}%)")
        print(f"   📉 Loss Treino: {logs['loss']:.4f}")
        print(f"   📉 Loss Validação: {logs['val_loss']:.4f}")

historico = modelo.fit(
    treino_generator,
    epochs=EPOCHS,
    validation_data=validacao_generator,
    callbacks=[ProgressCallback()],
    verbose=1
)

print("\n✅ TREINAMENTO CONCLUÍDO!")

# Salvar modelo
print("\n[ETAPA 5/6] Salvando modelo...")
modelo.save('classificador_gatos_cachorros.keras')
print("✅ Modelo salvo como: classificador_gatos_cachorros.keras")

# Gerar gráficos
print("\n[ETAPA 6/6] Gerando gráficos de resultados...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico de acurácia
epochs_range = range(1, EPOCHS + 1)
ax1.plot(epochs_range, historico.history['accuracy'], 'b-o', label='Treino', linewidth=2)
ax1.plot(epochs_range, historico.history['val_accuracy'], 'r-o', label='Validação', linewidth=2)
ax1.set_title('Acurácia do Modelo', fontsize=14, fontweight='bold')
ax1.set_xlabel('Época', fontsize=12)
ax1.set_ylabel('Acurácia', fontsize=12)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_ylim([0, 1])

# Gráfico de perda
ax2.plot(epochs_range, historico.history['loss'], 'b-o', label='Treino', linewidth=2)
ax2.plot(epochs_range, historico.history['val_loss'], 'r-o', label='Validação', linewidth=2)
ax2.set_title('Perda do Modelo', fontsize=14, fontweight='bold')
ax2.set_xlabel('Época', fontsize=12)
ax2.set_ylabel('Perda', fontsize=12)
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('resultados_treinamento.png', dpi=300, bbox_inches='tight')
print("✅ Gráfico salvo como: resultados_treinamento.png")

# Resultado final
print("\n" + "=" * 70)
print("🎉 PROJETO CONCLUÍDO COM SUCESSO!")
print("=" * 70)

acuracia_final = historico.history['val_accuracy'][-1]
print(f"\n📊 RESULTADO FINAL:")
print(f"   🎯 Acurácia Final: {acuracia_final:.4f} ({acuracia_final*100:.2f}%)")

if acuracia_final > 0.90:
    print("   🌟 EXCELENTE! Seu modelo está muito bom!")
elif acuracia_final > 0.75:
    print("   👍 BOM! Resultado satisfatório!")
elif acuracia_final > 0.60:
    print("   👌 RAZOÁVEL. Pode melhorar com mais dados!")
else:
    print("   ⚠️  Acurácia baixa. Tente adicionar mais imagens!")

print(f"\n📁 ARQUIVOS GERADOS:")
print(f"   ✅ classificador_gatos_cachorros.keras (modelo treinado)")
print(f"   ✅ resultados_treinamento.png (gráficos)")

print(f"\n📝 PRÓXIMO PASSO:")
print(f"   python testar_imagem.py data/validation/cats/cat_001.jpg")

print("\n" + "=" * 70)
print("🐱🐶 Obrigado por usar o Classificador de Gatos e Cachorros! 🐶🐱")
print("=" * 70)