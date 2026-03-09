import seaborn as sns
import matplotlib.pyplot as plt

def dashboard():
    #Incarcarea dataset-ului
    tips = sns.load_dataset('tips')

    ordinea_zilelor = ['Thur', 'Fri', 'Sat', 'Sun']

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Dashboard Analiza Dataset Tips', fontsize=16)

    #Setarea culorilor pentru scatterplot si crearea acestuia
    colors = {'Male':'blue','Female':'pink'}

    for sex, color in colors.items():
        subset = tips[tips['sex'] == sex]
        axes[0, 0].scatter(subset['total_bill'], subset['tip'], c=color, label=sex, alpha=0.6)
    axes[0, 0].set_title('Total Bill vs Tip (by Sex)')
    axes[0, 0].set_xlabel('Total Bill ($)')
    axes[0, 0].set_ylabel('Tip ($)')
    axes[0, 0].legend()

    # 2. Boxplot (Seaborn) - Distributia Total Bill per Zi
    sns.boxplot(data=tips, x='day', y='total_bill', order=ordinea_zilelor, ax=axes[0, 1], palette='Set2')
    axes[0, 1].set_title('Distribuție Total Bill per Zi')

    # 3. Histograme (Seaborn) - Distributia Tip cu KDE
    sns.histplot(data=tips, x='tip', hue='time', kde=True, ax=axes[1, 0], palette='muted')
    axes[1, 0].set_title('Distribuție Bacsis: Pranz vs Cina')

    # 4. Barplot (Seaborn) - Bacsis mediu per Zi cu CI
    sns.barplot(data=tips, x='day', y='tip', order=ordinea_zilelor, errorbar='ci', ax=axes[1, 1], palette='pastel')
    axes[1, 1].set_title('Media Bacsisului per Zi (cu Interval de Incredere)')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('dashboard_tips.png')
    print("Dashboard-ul a fost salvat ca 'dashboard_tips.png'.")
    plt.show()

if __name__ == "__main__":
    dashboard()