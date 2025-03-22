import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

renda_fam = [
    5, 6.8, 9, 3, 17, 13, 11.2, 5.4, 13, 16, 16, 16.3, 11.7, 12, 4, 3, 9, 13, 12, 9, 2, 1, 3, 4, 2, 
    8, 1, 19.3, 12.5, 19, 19, 2, 5.5, 5, 2, 7, 2, 3.2, 9.5, 1.5, 5, 18, 6, 9, 2, 1, 16, 10, 9.4, 4.5
]

renda_fam_sorted = sorted(renda_fam)

Q1 = np.percentile(renda_fam_sorted, 25)
Q2 = np.percentile(renda_fam_sorted, 50)
Q3 = np.percentile(renda_fam_sorted, 75)

Q1, Q2, Q3

def classificar_renda(renda):
    if renda <= Q1:
        return 'Baixa'
    elif Q1 < renda <= Q2:
        return 'MediaBaixa'
    elif Q2 < renda <= Q3:
        return 'MediaAlta'
    else:
        return 'Alta'


renda_fam_classificada = [classificar_renda(renda) for renda in renda_fam_sorted]

renda_fam_classificada

renda_media_geral = np.mean(renda_fam)

renda_media_por_subgrupo = {
    "Baixa": np.mean([renda for i, renda in enumerate(renda_fam) if renda_fam_classificada[i] == 'Baixa']),
    "MediaBaixa": np.mean([renda for i, renda in enumerate(renda_fam) if renda_fam_classificada[i] == 'MediaBaixa']),
    "MediaAlta": np.mean([renda for i, renda in enumerate(renda_fam) if renda_fam_classificada[i] == 'MediaAlta']),
    "Alta": np.mean([renda for i, renda in enumerate(renda_fam) if renda_fam_classificada[i] == 'Alta']),
}

renda_media_geral, renda_media_por_subgrupo

dados = {
    "Renda": renda_fam,
    "Subgrupo": renda_fam_classificada
}

import pandas as pd
df = pd.DataFrame(dados)

plt.figure(figsize=(10, 6))
sns.boxplot(x="Subgrupo", y="Renda", data=df)
plt.title('Box Plot da Renda Geral e por Subgrupo de Renda')
plt.xlabel('Subgrupo de Renda')
plt.ylabel('Renda Familiar')
plt.show()
