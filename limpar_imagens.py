import os
from PIL import Image
from pathlib import Path

print("=" * 70)
print("🔍 VERIFICANDO E LIMPANDO IMAGENS CORROMPIDAS")
print("=" * 70)

# Pastas para verificar
diretorios = [
    'data/train/cats',
    'data/train/dogs',
    'data/validation/cats',
    'data/validation/dogs'
]

def verificar_imagem(caminho):
    """
    Tenta abrir a imagem. Retorna True se OK, False se corrompida.
    """
    try:
        img = Image.open(caminho)
        img.verify()  # Verifica se a imagem está OK
        
        # Tenta carregar novamente (verify() fecha o arquivo)
        img = Image.open(caminho)
        img.load()  # Força o carregamento completo
        
        # Verifica se tem pelo menos 10x10 pixels
        if img.size[0] < 10 or img.size[1] < 10:
            return False, "Imagem muito pequena"
        
        return True, "OK"
    
    except Exception as e:
        return False, str(e)

def limpar_diretorios():
    """
    Verifica todas as imagens e remove as corrompidas
    """
    total_verificadas = 0
    total_removidas = 0
    total_ok = 0
    
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            print(f"\n⚠️  Pasta não encontrada: {diretorio}")
            continue
        
        print(f"\n📁 Verificando: {diretorio}")
        print("   " + "-" * 66)
        
        # Listar arquivos de imagem
        arquivos = [f for f in os.listdir(diretorio) 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
        
        print(f"   Total de arquivos: {len(arquivos)}")
        
        removidas_neste_dir = 0
        
        for i, arquivo in enumerate(arquivos):
            caminho_completo = os.path.join(diretorio, arquivo)
            total_verificadas += 1
            
            # Mostrar progresso a cada 500 imagens
            if (i + 1) % 500 == 0:
                print(f"   Verificadas: {i + 1}/{len(arquivos)}...")
            
            # Verificar imagem
            ok, mensagem = verificar_imagem(caminho_completo)
            
            if not ok:
                print(f"   ❌ Removendo: {arquivo}")
                print(f"      Motivo: {mensagem}")
                
                try:
                    os.remove(caminho_completo)
                    total_removidas += 1
                    removidas_neste_dir += 1
                except Exception as e:
                    print(f"      ⚠️  Erro ao remover: {e}")
            else:
                total_ok += 1
        
        if removidas_neste_dir == 0:
            print(f"   ✅ Todas as {len(arquivos)} imagens estão OK!")
        else:
            print(f"   ⚠️  Removidas: {removidas_neste_dir} imagens")
            print(f"   ✅ Restantes: {len(arquivos) - removidas_neste_dir} imagens")
    
    # Resumo final
    print("\n" + "=" * 70)
    print("📊 RESUMO DA LIMPEZA")
    print("=" * 70)
    print(f"\n   🔍 Total verificadas: {total_verificadas}")
    print(f"   ✅ Imagens OK: {total_ok}")
    print(f"   ❌ Imagens removidas: {total_removidas}")
    
    if total_removidas > 0:
        print(f"\n   ⚠️  {total_removidas} imagens corrompidas foram removidas!")
        print(f"   💡 Porcentagem removida: {(total_removidas/total_verificadas)*100:.2f}%")
    else:
        print(f"\n   🎉 Nenhuma imagem corrompida encontrada!")
    
    # Contar imagens finais
    print("\n" + "=" * 70)
    print("📁 CONTAGEM FINAL")
    print("=" * 70)
    
    for diretorio in diretorios:
        if os.path.exists(diretorio):
            arquivos = [f for f in os.listdir(diretorio) 
                       if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
            print(f"   {diretorio}: {len(arquivos)} imagens")
    
    print("\n" + "=" * 70)
    print("✅ LIMPEZA CONCLUÍDA!")
    print("=" * 70)
    print("\n📝 PRÓXIMO PASSO:")
    print("   python classificador_simples.py")
    print("=" * 70)

def main():
    """Função principal"""
    try:
        limpar_diretorios()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário!")
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()