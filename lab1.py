import numpy as np

# funkcija racunanja vrijednosti korijena iz kvadratne jednadzbe
def sqrt(a, b, c):
    return (b ** 2 - 4 * a * c) ** (1 / 2)

# funkcija racunanja pomocu formule za opce rjesenje homogene rekurzivne relacije
def formula(lam1, lam2, a0, a1, n):
    # ako je n jednak 0 trazimo clan a0
    if n == 0:
        return a0
    # ako je n jednak 1 trazimo clan a1
    elif n == 1:
        return a1
    # ako je vrijednost n veca od 1 tada trazimo clan preko formule
    elif n > 1:
        # zadana jednadzba je an2 = lam1 * an1 + lam2 * an
        # karakteristicna jednadzba je x**2 - x * lam1 - lam2 = 0

        # koeficijenti uz varijable u karakteristicnoj jednadzbi u obliku ax^2 + bx + c = 0
        a = 1
        b = -lam1
        c = -lam2

        # nultocke x1 i x2 karakteristicne jednadzbe
        x1 = (-b - sqrt(a, b, c)) / (2 * a)
        x2 = (-b + sqrt(a, b, c)) / (2 * a)

        # dobivamo izraze λ1 i λ2 za jednadzbu an = λ1 * nultocka1**n + λ2 * n * nultocka2**n
        if x1 == x2:
            # definiramo matricu A
            A = np.array([[x1 ** 0, 0 * (x2 ** 0)],
                          [x1 ** 1, 1 * (x2 ** 1)]])
            # definiramo matricu B
            B = np.array([[a0],
                          [a1]])
            # rijesimo sustav linearnih jednadzbi i spremamo rjesenja λ1 i λ2 u matricu C
            C = np.linalg.solve(A, B)

            # racunamo vrijednost n-tog clan
            an = C[0] * (x1 ** n) + C[1] * (x2 ** n) * n

        # dobivamo izraze λ1 i λ2 za jednadzbu an = λ1 * nultocka1**n + λ2 * nultocka2**n
        else:
            # definiramo matricu A
            A = np.array([[x1 ** 0, (x2 ** 0)],
                          [x1 ** 1, (x2 ** 1)]])
            # definiramo matricu B
            B = np.array([[a0],
                          [a1]])
            # rijesimo sustav linearnih jednadzbi i spremamo rjesenja λ1 i λ2 u matricu C
            C = np.linalg.solve(A, B)

            # racunamo vrijednost n-tog clan
            an = C[0] * (x1 ** n) + C[1] * (x2 ** n)

        return an

# funkcija racunanja pomocu rekurzije
def rekurzija(lam1, lam2, a0, a1, n):
    # ako je n jednak 0 trazimo clan a0
    if n == 0:
        return a0
    # ako je n jednak 1 trazimo clan a1
    elif n == 1:
        return a1
    # ako je vrijednost n veca od 1 tada trazimo clan preko rekurzije
    elif n > 1:
        an = (lam1 * rekurzija(lam1, lam2, a0, a1, n - 1) + lam2 * rekurzija(lam1, lam2, a0, a1, n - 2))
        return an

# dobivanje vrijednosti parametara preko ispisa i upisa
lam1 = int(input("Unesite prvi koeficijent λ_1 rekurzivne relacije: "))
lam2 = int(input("Unesite drugo koeficijent λ_2 rekurzivne relacije: "))
a0 = int(input("Unesite vrijednost nultog clana niza a_0: "))
a1 = int(input("Unesite vrijednost prvog clana niza a_1: "))
n = int(input("Unesite redni broj n trazenog clana niza: "))

# an racunanjem formule za opce rjesenje homogene rekurzivne relacije
an_for = int(formula(lam1, lam2, a0, a1, n))
print("Vrijednost n-tog clana niza pomocu formule: ", an_for)

# an računanjem odgovarajućeg člana niza rekurzivno
an_rek = int(rekurzija(lam1, lam2, a0, a1, n))
print("Vrijednost n-tog clana niza iz rekurzije: ", an_rek)