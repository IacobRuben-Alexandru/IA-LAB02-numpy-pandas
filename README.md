# Laborator 02 - Inteligență Artificială
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![NumPy](https://img.shields.io/badge/NumPy-v1.2x-blue?logo=numpy)
![Pandas](https://img.shields.io/badge/Pandas-v1.x-blue?logo=pandas)
![Seaborn](https://img.shields.io/badge/Seaborn-v0.1x-blue?logo=python)

Acest repository conține rezolvarea temei pentru Laboratorul 02, axată pe utilizarea bibliotecilor NumPy, Pandas, Matplotlib și Seaborn pentru procesarea și vizualizarea datelor.

---

## 📋 Cuprins
1. [Sarcina A: Operații matriceale cu NumPy](#sarcina-a-operații-matriceale-cu-numpy)
2. [Sarcina B: Analiza dataset-ului Tips cu Pandas](#sarcina-b-analiza-dataset-ului-tips-cu-pandas)
3. [Sarcina C: Dashboard de vizualizare](#sarcina-c-dashboard-de-vizualizare)
4. [Sarcina D: (Bonus) Raport comparativ Iris](#sarcina-d-bonus-raport-comparativ-iris)
5. [Sarcina E: (Bonus) Google Colaboratory](#sarcina-e-bonus-google-colaboratory)

---

## 🔢 Sarcina A: Operații matriceale cu NumPy
Implementarea include:
* **Generare:** Matricele $A (4 \times 3)$ și $B (3 \times 5)$ cu valori întregi între 1 și 10 și seed pentru reproductibilitate.
* **Calcul:** Produsul matriceal $C = A @ B$.
* **Statistici:** Afișarea sumei elementelor, mediei pe coloane (`axis=0`) și a valorii maxime globale din $C.
* **Bonus:** Generarea unei matrice pătratice $M (3 \times 3)$, calcularea inversei și a determinantului, cu validarea identității prin `np.allclose`.

## 🐼 Sarcina B: Analiza dataset-ului Tips cu Pandas
Analiză exploratorie folosind setul de date `tips`:
* Afișarea dimensiunii, tipurilor de date și a statisticilor descriptive.
* Calcularea bacșișului mediu per zi și per sex.
* Crearea coloanei `procent_bacsis` ($tip / total\_bill \times 100$).
* Identificarea top 5 cele mai generoase mese.
* Agregarea numărului de mese servite per zi și per categorie de fumători.

## 📊 Sarcina C: Dashboard de vizualizare
Generarea unei figuri Matplotlib (grilă 2x2) salvată ca `dashboard_tips.png`:
1. **Scatter:** `total_bill` vs `tip`, colorat după sex (filtrare manuală în buclă).
2. **Boxplot:** Distribuția `total_bill` per zi (Thur → Sun).
3. **Histogramă:** Distribuția `tip` cu `hue='time'` și KDE.
4. **Barplot:** Bacșișul mediu per zi cu intervale de încredere (`errorbar='ci'`).

## 🌸 Sarcina D: (Bonus) Raport comparativ Iris
Generarea vizualizărilor avansate pentru dataset-ul Iris:
* **Pairplot:** Toate variabilele cu `hue='species'` și KDE pe diagonală.
* **Violinplots:** O figură separată cu 4 subploturi (1x4) pentru fiecare variabilă numerică, segmentată după specie.
* Toate figurile sunt salvate ca fișiere PNG.

## ☁️ Sarcina E: (Bonus) Google Colaboratory
Proiectul este documentat și pregătit pentru utilizare în **Google Colab**, profitând de:
* **Code cells:** Pentru execuția scripturilor Python.
* **Markdown cells:** Pentru documentație text și formule matematice.

---

## 🛠️ Instalare
Pentru a rula local, instalați dependințele necesare:
```bash
pip install numpy pandas matplotlib seaborn
