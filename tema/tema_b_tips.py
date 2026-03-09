import seaborn as sns

def tips():
    #Incarcarea bazei de date
    tp = sns.load_dataset('tips')

    #Afisarea dimensiunii dataset-ului cat si tipurile de date si statisticile descriptive
    print(f"Dimensiunea dataset-ului tips: {tp.size}")
    print(f"Tipurile de date si statisticile descriptive: {tp.describe()}")

    print("#" * 60)

    #Afisarea bacsisului mediu per zi si per sex
    print(f"Bacsisul mediu per zi a saptamanii:\n{tp.groupby(['day']).mean(numeric_only=True)}")
    print(f"\nBacsisul mediu per sex:\n{tp.groupby(['sex']).mean(numeric_only=True)}")

    print("#" * 60)

    #Crearea unei copii a dataset-ului si crearea unei coloane noi
    copy_tp = tp.copy()
    copy_tp['procent_bacsis'] = (copy_tp['tip'] / copy_tp['total_bill'] * 100)

    #Afisarea coloanei create
    print(f"Coloana procent_bacsis:\n{copy_tp['procent_bacsis']}")

    print("#" * 60)

    #Afisarea celor 5 cele mai generoase mese
    print(f"5 cele mai generoase mese:\n{copy_tp['procent_bacsis'].nlargest(5)}")

    print("#" * 60)
    #Afisarea numarului de mese servite per zi si a cate mese de tip smoker au fost servite
    print(f"Cate mese au fost servite per ziL:\n{tp.groupby(['day']).size()}")
    print(f"Cate mese au fost servite per categorie de fumatori:\n{tp.groupby(['smoker']).size()}")

if __name__ == "__main__":
    tips()
