import os
import shutil
from pathlib import Path

print("=" * 70)
print("📂 SEPARANDO DADOS DE TREINO E VALIDAÇÃO")
print("=" * 70)

# Configurações
PORCENTAGEM_VALIDACAO = 0.2  # 20% para validação, 80% para treino
DIR_TREINO = 'data/train'
DIR_VALIDACAO = 'data/validation'

def criar_pastas_validacao():
    """Cria a estrutura de pastas para validação"""
    print("\n[1/4] Criando pastas de validação...")
    
    pastas = [
        'data/validation',
        'data/validation/cats',
        'data/validation/dogs'
    ]
    
    for pasta in pastas:
        os.makedirs(pasta, exist_ok=True)
        print(f"   ✅ {pasta}")
    
    print("✅ Pastas criadas!")

def contar_imagens():
    """Conta quantas imagens existem em cada categoria"""
    print("\n[2/4] Contando imagens...")
    
    try:
        cats_treino = [f for f in os.listdir(f'{DIR_TREINO}/cats') 
                       if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        dogs_treino = [f for f in os.listdir(f'{DIR_TREINO}/dogs') 
                       if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        print(f"   🐱 Gatos no treino: {len(cats_treino)}")
        print(f"   🐶 Cachorros no treino: {len(dogs_treino)}")
        
        return cats_treino, dogs_treino
    
    except FileNotFoundError as e:
        print(f"\n❌ ERRO: Pasta não encontrada!")
        print(f"   {e}")
        print(f"\n💡 Certifique-se que as imagens estão em:")
        print(f"   - {DIR_TREINO}/cats/")
        print(f"   - {DIR_TREINO}/dogs/")
        return None, None

def mover_para_validacao(arquivos, categoria, num_validacao):
    """Move arquivos para a pasta de validação"""
    import random
    
    # Embaralhar para pegar imagens aleatórias
    random.shuffle(arquivos)
    
    # Selecionar imagens para validação
    arquivos_validacao = arquivos[:num_validacao]
    
    print(f"\n   Movendo {len(arquivos_validacao)} imagens de {categoria}...")
    
    movidos = 0
    erros = 0
    
    for arquivo in arquivos_validacao:
        origem = f'{DIR_TREINO}/{categoria}/{arquivo}'
        destino = f'{DIR_VALIDACAO}/{categoria}/{arquivo}'
        
        try:
            shutil.move(origem, destino)
            movidos += 1
            if movidos % 100 == 0:
                print(f"      {movidos}/{len(arquivos_validacao)} movidos...")
        except Exception as e:
            erros += 1
    
    print(f"   ✅ {movidos} imagens movidas")
    if erros > 0:
        print(f"   ⚠️  {erros} erros")
    
    return movidos

def separar_dados():
    """Função principal para separar os dados"""
    
    # Criar pastas
    criar_pastas_validacao()
    
    # Contar imagens
    cats_treino, dogs_treino = contar_imagens()
    
    if cats_treino is None or dogs_treino is None:
        return False
    
    # Calcular quantas imagens mover
    num_cats_validacao = int(len(cats_treino) * PORCENTAGEM_VALIDACAO)
    num_dogs_validacao = int(len(dogs_treino) * PORCENTAGEM_VALIDACAO)
    
    print("\n[3/4] Movendo imagens para validação...")
    print(f"   📊 {PORCENTAGEM_VALIDACAO * 100:.0f}% dos dados irão para validação")
    print(f"   🐱 Gatos: {num_cats_validacao} imagens")
    print(f"   🐶 Cachorros: {num_dogs_validacao} imagens")
    
    # Mover gatos
    print(f"\n   🐱 Processando gatos...")
    cats_movidos = mover_para_validacao(cats_treino, 'cats', num_cats_validacao)
    
    # Mover cachorros
    print(f"\n   🐶 Processando cachorros...")
    dogs_movidos = mover_para_validacao(dogs_treino, 'dogs', num_dogs_validacao)
    
    # Resumo final
    print("\n[4/4] Verificando resultado final...")
    
    # Contar novamente
    cats_treino_final = len([f for f in os.listdir(f'{DIR_TREINO}/cats') 
                             if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    dogs_treino_final = len([f for f in os.listdir(f'{DIR_TREINO}/dogs') 
                             if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    
    cats_val_final = len([f for f in os.listdir(f'{DIR_VALIDACAO}/cats') 
                          if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    dogs_val_final = len([f for f in os.listdir(f'{DIR_VALIDACAO}/dogs') 
                          if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    
    print("\n" + "=" * 70)
    print("📊 RESUMO FINAL")
    print("=" * 70)
    print("\n📁 TREINO:")
    print(f"   🐱 Gatos: {cats_treino_final} imagens")
    print(f"   🐶 Cachorros: {dogs_treino_final} imagens")
    print(f"   📊 Total: {cats_treino_final + dogs_treino_final} imagens")
    
    print("\n📁 VALIDAÇÃO:")
    print(f"   🐱 Gatos: {cats_val_final} imagens")
    print(f"   🐶 Cachorros: {dogs_val_final} imagens")
    print(f"   📊 Total: {cats_val_final + dogs_val_final} imagens")
    
    print("\n" + "=" * 70)
    print("✅ SEPARAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 70)
    print("\n📝 PRÓXIMO PASSO:")
    print("   python classificador_simples.py")
    print("=" * 70)
    
    return True

if __name__ == "__main__":
    try:
        sucesso = separar_dados()
        if not sucesso:
            print("\n❌ Falha ao separar dados. Verifique os erros acima.")
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {e}")
        print("\n💡 Dica: Certifique-se que você tem as imagens em:")
        print("   data/train/cats/")
        print("   data/train/dogs/")