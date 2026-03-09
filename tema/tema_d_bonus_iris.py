import seaborn as sns
import matplotlib.pyplot as plt

def iris():
    iris = sns.load_dataset('iris')

    #PairPlot complet pentru iris cu hue si diag_kind ca in cerinta
    pair = sns.pairplot(iris,hue='species',diag_kind='kde')
    pair.fig.suptitle('Analiza pairplot pentru dataset-ul iris')
    pair.savefig('iris_pairplot.png')

    #Figura cu 4 subploturi
    fig, axes = plt.subplots(1, 4, figsize=(18, 6))
    fig.suptitle('Distribuția Variabilelor Iris (Violin Plots)', fontsize=16)

    features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

    for i, feature in enumerate(features):
        sns.violinplot(data=iris, x='species', y=feature, hue='species', 
                    ax=axes[i], palette='magma', legend=False)
        axes[i].set_title(feature.replace('_', ' ').title())

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('iris_violinplots.png')
    print("Figurile Iris au fost salvate ca PNG.")
    plt.show()
if __name__ == "__main__":
    iris()


# D. (Bonus) Raport comparativ Iris
# Creați un script Python care:

# 2. Creează o figură separată cu 4 subploturi (1×4), câte un violinplot pentru fiecare variabilă numerică din
# Iris (sepal_length, sepal_width, petal_length, petal_width), cu hue='species' și split=False.
# 3. Adăugați un titlu general și salvați ambele figuri ca fișiere PNG.