import json

caminho_arquivo = 'faturamento.json'

def processar_faturamento(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as f:
            dados = json.load(f)

        faturamento_diario = [item['valor'] for item in dados['faturamento'] if item['valor'] > 0]

        if not faturamento_diario:
            print("Não há faturamento diário disponível.")
            return

        menor_faturamento = min(faturamento_diario)
        maior_faturamento = max(faturamento_diario)

        total_faturamento = sum(faturamento_diario)
        num_dias_com_faturamento = len(faturamento_diario)
        media_mensal = total_faturamento / num_dias_com_faturamento

        dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

        print(f"Menor valor de faturamento: R${menor_faturamento:,.2f}")
        print(f"Maior valor de faturamento: R${maior_faturamento:,.2f}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o arquivo JSON: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

processar_faturamento(caminho_arquivo)
