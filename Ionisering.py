import numpy as np
import matplotlib.pyplot as mp
ph = 0
ionliste = []
phliste = []
def kommatilpunkt(tall):
    punkt = float(tall.replace(",","."))
    return punkt

print("Skriv \"stopp\" for å avslutte.")
while True:
    phliste.clear()
    ionliste.clear()
    ph = 0
    pka = input("Skriv inn pKa verdi: ")
    if pka == "stopp":
        break
    try:
        pka = kommatilpunkt(pka)
        steg = 0.1
        n = int((14-0)/steg)
        for i in range(0,n+1):
            h = 10**(-ph)
            ka = 10**(-float(pka))
            ha = ((h**2)/ka) + h
            ionp = (h/ha)*100
            phliste.append(ph)
            ionliste.append(ionp)
            ph += steg
        a = np.array(ionliste)
        b = np.array(phliste)

        mp.plot(b,a)
        mp.title("Estimat av Ionisering")
        mp.xlabel("pH")
        mp.ylabel("Ionisering (%)")
        mp.grid(linewidth = 1)
        mp.ylim((-2,102))
        mp.xlim((0,14))
        mp.show()

    except ValueError:
        print("Ugyldig pKa verdi, tast inn ny: ")



