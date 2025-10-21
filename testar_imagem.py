import sys
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

def testar_imagem(caminho_imagem, caminho_modelo='classificador_gatos_cachorros.keras'):
    """
    Testa uma imagem usando o modelo treinado
    """
    print("=" * 70)
    print("🔮 TESTANDO IMAGEM COM O MODELO")
    print("=" * 70)
    
    # Carregar modelo
    print("\n📦 Carregando modelo...")
    try:
        modelo = keras.models.load_model(caminho_modelo)
        print("✅ Modelo carregado!")
    except Exception as e:
        print(f"❌ Erro ao carregar modelo: {e}")
        print("Certifique-se que o arquivo 'classificador_gatos_cachorros.keras' existe!")
        return
    
    # Carregar imagem
    print(f"\n🖼️  Carregando imagem: {caminho_imagem}")
    try:
        img = image.load_img(caminho_imagem, target_size=(150, 150))
        print("✅ Imagem carregada!")
    except Exception as e:
        print(f"❌ Erro ao carregar imagem: {e}")
        return
    
    # Preprocessar
    print("\n🔧 Preprocessando imagem...")
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    
    # Fazer predição
    print("🧠 Fazendo predição...")
    predicao = modelo.predict(img_array, verbose=0)[0][0]
    
    # Interpretar resultado
    if predicao > 0.5:
        classe = "🐶 CACHORRO"
        confianca = predicao * 100
        cor = 'brown'
    else:
        classe = "🐱 GATO"
        confianca = (1 - predicao) * 100
        cor = 'orange'
    
    # Mostrar resultado
    print("\n" + "=" * 70)
    print("📊 RESULTADO DA PREDIÇÃO")
    print("=" * 70)
    print(f"\n   Classe: {classe}")
    print(f"   Confiança: {confianca:.2f}%")
    
    if confianca > 90:
        print(f"   Certeza: 🟢 MUITO ALTA")
    elif confianca > 70:
        print(f"   Certeza: 🟡 ALTA")
    elif confianca > 50:
        print(f"   Certeza: 🟠 MODERADA")
    else:
        print(f"   Certeza: 🔴 BAIXA (modelo incerto)")
    
    print("\n" + "=" * 70)
    
    # Visualizar resultado
    plt.figure(figsize=(10, 6))
    
    # Imagem
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.axis('off')
    plt.title('Imagem Original', fontsize=14, fontweight='bold')
    
    # Gráfico de probabilidade
    plt.subplot(1, 2, 2)
    categorias = ['Gato', 'Cachorro']
    probabilidades = [(1 - predicao) * 100, predicao * 100]
    cores = ['orange', 'brown']
    
    bars = plt.bar(categorias, probabilidades, color=cores, alpha=0.7, edgecolor='black')
    plt.ylabel('Probabilidade (%)', fontsize=12)
    plt.title('Probabilidades', fontsize=14, fontweight='bold')
    plt.ylim(0, 100)
    
    # Adicionar valores nas barras
    for bar, prob in zip(bars, probabilidades):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{prob:.1f}%',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.suptitle(f'PREDIÇÃO: {classe}', fontsize=16, fontweight='bold', color=cor)
    plt.tight_layout()
    
    # Salvar resultado
    nome_saida = f"resultado_{caminho_imagem.split('/')[-1].split('\\')[-1]}"
    plt.savefig(nome_saida, dpi=150, bbox_inches='tight')
    print(f"💾 Resultado salvo como: {nome_saida}")
    
    plt.show()

def main():
    """Função principal"""
    if len(sys.argv) < 2:
        print("=" * 70)
        print("❌ ERRO: Você precisa fornecer o caminho da imagem!")
        print("=" * 70)
        print("\n📖 USO CORRETO:")
        print("   python testar_imagem.py caminho/para/imagem.jpg")
        print("\n📝 EXEMPLOS:")
        print("   python testar_imagem.py data/validation/cats/cat_001.jpg")
        print("   python testar_imagem.py minha_foto.jpg")
        print("   python testar_imagem.py C:\\Users\\Nome\\Desktop\\gato.jpg")
        print("=" * 70)
        return
    
    caminho = sys.argv[1]
    testar_imagem(caminho)

if __name__ == "__main__":
    main()