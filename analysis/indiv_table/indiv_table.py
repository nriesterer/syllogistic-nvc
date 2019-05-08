import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_df = pd.read_csv('individuals.csv', sep=';')

rules = data_df["Rule"].unique()
models = list(data_df["Model"].unique())
indiv_table = np.zeros((len(models), len(rules)))

for model, elem in data_df.groupby("Model"):
    idx = models.index(model)

    indiv_table[idx, 0] = elem[elem["Rule"] == "PartNeg"]["Num persons"].values[0]
    indiv_table[idx, 1] = elem[elem["Rule"] == "EmptyStart"]["Num persons"].values[0]
    indiv_table[idx, 2] = elem[elem["Rule"] == "FiguralRule"]["Num persons"].values[0]
    indiv_table[idx, 3] = elem[elem["Rule"] == "ParticularityRule"]["Num persons"].values[0]
    indiv_table[idx, 4] = elem[elem["Rule"] == "NegativityRule"]["Num persons"].values[0]

sns.set(style='white', palette="colorblind")

palette = sns.light_palette('C0')

plot = sns.heatmap(indiv_table.T, annot=True, square=True, cbar=False, linewidths=1, cmap=palette)
plot.set_xticklabels(models, rotation=70)
plot.set_yticklabels(rules, rotation=0)

plt.tight_layout()
plt.savefig('indiv_table.pdf')
plt.show()
