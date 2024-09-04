faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento.values())

participacao_estado = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()}

estado_maior_faturamento = max(faturamento, key=faturamento.get)
maior_faturamento = faturamento[estado_maior_faturamento]

print(f"Faturamento total: R${faturamento_total:,.2f}")
print("\nParticipação de cada estado no faturamento total:")
for estado, participacao in participacao_estado.items():
    print(f"{estado}: {participacao:.2f}%")

print(f"\nEstado com o maior faturamento: {estado_maior_faturamento} com R${maior_faturamento:,.2f}")
