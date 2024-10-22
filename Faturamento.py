import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

valores_validos = [item for item in dados if item['valor'] > 0]

menor_item = min(valores_validos, key=lambda x: x['valor'])
maior_item = max(valores_validos, key=lambda x: x['valor'])

soma_valores = sum(item['valor'] for item in valores_validos)
media_mensal = soma_valores / len(valores_validos)

dias_acima_da_media = [item for item in valores_validos if item['valor'] > media_mensal]

print(f"Menor faturamento ocorrido do mês: \n\nDia: {menor_item['dia']}\n{menor_item['valor']}\n")
print(f"Maior faturamento ocorrido do mês: \n\nDia: {maior_item['dia']}\n{maior_item['valor']}\n")
print(f"Média mensal do faturamento: \n\n{media_mensal:.2f}\n")

print("Dias com faturamento acima da média:")
for item in dias_acima_da_media:
    print(f"Dia: {item['dia']} Faturamento: {item['valor']:.2f}")


