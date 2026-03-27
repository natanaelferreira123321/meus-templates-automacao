import os

# Simulação de dados que viriam do sistema AMPLA (Atualizado: Empilhadeira)
dados_manutencao = [
    {"ativo": "Empilhadeira 01", "falha": "Elétrica", "minutos": 45},
    {"ativo": "Transportador de Correia", "falha": "Mecânica", "minutos": 120},
    {"ativo": "Empilhadeira 01", "falha": "Instrumentação", "minutos": 30},
    {"ativo": "Britador Primário", "falha": "Motor Queimado", "minutos": 200},
]

def calcular_downtime_total(dados):
    # Soma todos os minutos de parada da lista
    return sum(item['minutos'] for item in dados)

def gerar_relatorio_final(total):
    # Cria um arquivo de texto com o resultado
    with open("relatorio_paradas.txt", "w", encoding="utf-8") as f:
        f.write(f"--- RELATÓRIO DE MANUTENÇÃO AUTOMATIZADO ---\n")
        f.write(f"Tempo total de indisponibilidade: {total} minutos.\n")
        f.write(f"Status dos Ativos: Verificado via Pipeline GitHub Actions.\n")
        f.write(f"Equipamento em destaque: Empilhadeira 01\n")

# --- BLOCO DE TESTES (O que a Pipeline confere) ---
def rodar_testes_de_qualidade():
    print("Iniciando validação dos dados de manutenção...")
    
    total = calcular_downtime_total(dados_manutencao)
    
    # Teste 1: O cálculo está correto? (45+120+30+200 = 395)
    assert total == 395, f"Erro no cálculo! Esperado 395, obtido {total}"
    
    # Teste 2: O sistema gerou o relatório?
    gerar_relatorio_final(total)
    assert os.path.exists("relatorio_paradas.txt"), "Falha ao gerar o arquivo de relatório!"

if __name__ == "__main__":
    try:
        rodar_testes_de_qualidade()
        print("✅ TESTE PASSOU: Relatório da Empilhadeira 01 gerado com sucesso!")
    except AssertionError as error:
        print(f"❌ FALHA NA VALIDAÇÃO: {error}")
        exit(1)
