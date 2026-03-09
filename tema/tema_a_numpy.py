import numpy as np

def numpy():
    #Fixarea seed-ului pentru reproductibilitate si crearea matricelor A si B pe dimensiunele cerute
    np.random.seed(42)
    A = np.random.randint(1,11,size=(4,3))
    B = np.random.randint(1,11,size=(3,5))

    #Afisarea matricelor A si B
    print("Matricea A: ")
    print(A)
    print("Matricea B: ")
    print(B)

    print("#"*60)

    #Afisarea produsului matriceal C=A@B calculat prin intermediul lui numpy
    C = A@B
    print("Produsul matriceal C=A@B: ")
    print(C)

    print("#"*60)

    #Afisarea sumei tuturor elementelor din C, media pe fiecare coloana si valoarea maxima
    #Am utilizat din numpy, sum, mean si max
    print(f"Suma tuturor elementelor din C:  {np.sum(C)}")
    print(f"Media pe fiecare coloana:  {np.mean(C,axis=0)}")
    print(f"Valoarea maxima globala: {np.max(C)}")

    print("#"*60)

    #Crearea matricei random M de dimensiune 3x3 si afisarea acesteia
    M = np.random.randint(1,11,size=(3,3))
    print("Matricea M: ")
    print(M)
    
    #Afisarea inversei, determinantului si verificarea daca matricea inversa este aproape de cea identitate
    print(f"Inversa matricei M: {np.linalg.inv(M)}")
    print(f"Determinantul matricei M: {np.linalg.det(M)}")
    print(f"Verificare apropiere matrice identitate: {np.allclose(np.linalg.inv(M),np.eye(3))}")

if __name__ == "__main__":
    numpy()