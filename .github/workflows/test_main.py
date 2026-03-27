import os

# --- ESPAÇO PARA SUA LÓGICA (CALCULADORA, AMPLA, BIBLIOTECA) ---
def minha_logica():
    # Exemplo: Simular um calculo ou criacao de arquivo
    return True

# --- BLOCO DE TESTES (O QUE A PIPELINE CONFERE) ---
def rodar_testes():
    print("Iniciando inspeção de qualidade...")
    
    # Teste 1: A lógica básica está funcionando?
    assert minha_logica() is True, "Falha na lógica principal!"
    
    # Teste 2: Verificar se algum arquivo importante foi gerado
    # Exemplo: if os.path.exists('banco.db'): print("Banco OK")

if __name__ == "__main__":
    try:
        rodar_testes()
        print("✅ TUDO OK: Pode seguir com a produção!")
    except AssertionError as error:
        print(f"❌ ERRO DETECTADO: {error}")
        exit(1) # Isso avisa a Pipeline para ficar vermelha
