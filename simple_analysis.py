import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
dados = pd.read_csv('data.csv')

# Mostrar primeiras linhas dos dados
print("Primeiras linhas do dataset:")
print(dados.head())

# Gerar gráfico simples
plt.figure(figsize=(10,6))
plt.bar(dados['Categoria'], dados['Quantidade'], color='skyblue')

plt.title('Gráfico Simples de Categorias')
plt.xlabel('Categoria')
plt.ylabel('Quantidade')

# Salvar gráfico
plt.savefig('imagens/grafico.png')

print("\n✅ Gráfico gerado com sucesso na pasta imagens!")
