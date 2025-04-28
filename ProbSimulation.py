import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Configuração
np.random.seed(42)

# -----------------------------
# 1) Simulação da moeda (50 lançamentos)
# -----------------------------
lancamentos_moeda = np.random.choice([0, 1], size=50)
lancamentos_texto = ["cara" if x == 0 else "coroa" for x in lancamentos_moeda]

# Frequências
freq_absoluta_moeda = pd.Series(lancamentos_texto).value_counts()
freq_relativa_moeda = freq_absoluta_moeda / 50

# Diferença em relação ao valor esperado (0.5)
diferenca_moeda = freq_relativa_moeda - 0.5

print("Tabela de Frequência da Moeda:")
print(pd.DataFrame({
    "Frequência Absoluta": freq_absoluta_moeda,
    "Frequência Relativa": freq_relativa_moeda,
    "Diferença (Relativa - Esperado)": diferenca_moeda
}))
print("\n")

# -----------------------------
# 3) Simulação do dado (80 lançamentos)
# -----------------------------
lancamentos_dado = np.random.choice([1,2,3,4,5,6], size=80)

# Frequências
freq_abs_dado = pd.Series(lancamentos_dado).value_counts().sort_index()
freq_rel_dado = freq_abs_dado / 80

print("Tabela de Frequência do Dado:")
print(pd.DataFrame({
    "Frequência Absoluta": freq_abs_dado,
    "Frequência Relativa": freq_rel_dado
}))
print("\n")

# Média e variância
media_dado = np.mean(lancamentos_dado)
variancia_dado = np.var(lancamentos_dado, ddof=1)

print(f"Média dos lançamentos do dado: {media_dado:.2f}")
print(f"Variância dos lançamentos do dado: {variancia_dado:.2f}")
print("\n")

# Gráfico das Frequências Relativas do dado
plt.figure(figsize=(8,5))
freq_rel_dado.plot(kind='bar', color='skyblue')
plt.title('Frequência Relativa dos Lançamentos do Dado')
plt.xlabel('Face do Dado')
plt.ylabel('Frequência Relativa')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# Frequências esperadas
freq_esperada_dado = np.repeat(80/6, 6)

# Gráfico comparativo: Observado vs Esperado
plt.figure(figsize=(8,5))
plt.bar(freq_abs_dado.index - 0.2, freq_abs_dado, width=0.4, label='Observado', color='lightcoral')
plt.bar(freq_abs_dado.index + 0.2, freq_esperada_dado, width=0.4, label='Esperado', color='lightgreen')
plt.title('Frequência Observada vs Frequência Esperada (Dado)')
plt.xlabel('Face do Dado')
plt.ylabel('Frequência Absoluta')
plt.legend()
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# -----------------------------
# e) Simulação de 2 moedas honestas, 200 vezes
# -----------------------------
moedas_duplas = np.random.choice([0,1], size=(200,2))
somas_moedas = moedas_duplas.sum(axis=1)

# Frequência e distribuição
dist_prob_empirica = pd.Series(somas_moedas).value_counts(normalize=True).sort_index()

print("Distribuição de Probabilidade Empírica (Soma de 2 Moedas):")
print(dist_prob_empirica)
print("\n")

# Gráfico da distribuição empírica
plt.figure(figsize=(6,4))
dist_prob_empirica.plot(kind='bar', color='plum')
plt.title('Distribuição Empírica da Soma de Duas Moedas')
plt.xlabel('Soma (X)')
plt.ylabel('Probabilidade')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# Distribuição teórica
dist_teorica = pd.Series({0: 0.25, 1: 0.5, 2: 0.25})

# Gráfico comparativo: Empírico vs Teórico
plt.figure(figsize=(6,4))
plt.bar(dist_prob_empirica.index - 0.15, dist_prob_empirica, width=0.3, label='Empírico', color='mediumslateblue')
plt.bar(dist_teorica.index + 0.15, dist_teorica, width=0.3, label='Teórico', color='lightseagreen')
plt.title('Distribuição Empírica vs Teórica (Soma de 2 Moedas)')
plt.xlabel('Soma (X)')
plt.ylabel('Probabilidade')
plt.legend()
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()
