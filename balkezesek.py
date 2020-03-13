with open("balkezesek.csv", 'r', encoding='latin2') as balkezesek_fejlec:
    fejlec = balkezesek_fejlec.readline()
    matrix=[sor.strip().split(';') for sor in balkezesek_fejlec]
    
#3feladat
print(f' 3.feladat: {len(matrix)}')

#4.feladat

print(f' 4.feladat:')
jatekosok=[print(f'      {sor[0]}, {float(sor[4])*2.54 :.1f} cm') for sor in matrix if sor[2][:7]=="1999-10"]

#5.feladat
while True:
    evszam= int(input("Kérek egy 1990 és 1999 közötti évszámot!:"))
    if (1989 < evszam < 2000):
        break
    else: print(f"Hibás adat!", end=" ")
    
#6.feladat
suly = [float(sor[3]) for sor in matrix if sor[1][:4] <= str(evszam) <= sor[2][:4]]
atlag = sum(suly)/len(suly)
print(f' 6.feladat: {atlag :.2f} font')
