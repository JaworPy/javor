# written by Martin Javorský from skygis.cz   mailto: martin.javorsky@gmail.com
# Tento Python script si nechá na vstupu zadat datum narození z formátu rodného čísla,
# zkontroluje zda zadané datum existuje, včetně přestupných roků
# a vypíše všechny možné kombinace pro doplnění čtyřmístné koncovky za "YYMMDD",
# tak aby splňovalo podmínku dělitelnosti jedenácti beze zbytku
# Více o rodných číslech zde: https://www.mvcr.cz/clanek/rady-a-sluzby-dokumenty-rodne-cislo.aspx

print("Kombinace pro číslo za lomítkem rodného čísla")
r = int(input("Zadej ročník ve tvaru YY: "))
m = int(input("Zadej měsíc ve tvaru MM (u žen přičíst 50): "))
d = int(input("Zadej den ve tvaru DD: "))
print()
z = ((r + m + d) % 11)
pocet = 0
zz = 0
print(z)
if (z == 0):
    z = z + 11
else:
    zz = z
rr = str(r) if r > 9 else f"0{r}"
mm = str(m) if m > 9 else f"0{m}"
dd = str(d) if d > 9 else f"0{d}"
if ((0 <= r <= 99) and ((1 <= m <= 12) or (51 <= m <= 62)) and ((1 <= d <= 28) or (d < 31 and m in [4, 6, 9, 11,54,56,59,61]) or (d==31 and m in[1,3,5,7,8,10,12,51,53,55,57,58,60,62]) or (d==29 and m in [2,52] and r%4 == 0)) ):
    print(f"Pro rodné číslo začínající {rr}{mm}{dd} existují tyto kombinace čtyřčíslí za lomítkem: ")
    for j in range(100):
        for i in range(100):
             jj = f"0{j}" if j < 10 else j
             ii = f"0{i}" if i < 10 else i                
             if ((i + j) % 11 == 11 - z):
                pocet += 1
                print(f"{jj}{ii}")
    print(f"Celkem existuje {pocet} kombinací\nZbytek po dělení je {zz}")
else:
    print("Chyba v zadání")