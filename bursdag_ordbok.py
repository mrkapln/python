"""
Det finnes en ordbok som brukeren kan fylle navnet og bursdag til vennene.
Programmet ber brukeren navn og bursdag så lenge brukeren svarer "ja" ved bruk av while-løkker.
Navnene skal settes som nøkkelverdi, og bursdagene skal settes som innholdverdi i ordboken
Progarammet skal fortsette å be navn så lenge brukeren vil ha å legge til et navn til

for-løkken skal skrive ut alle nøkkelverdier og innholdverdier
"""

venner = {}

svar = "ja"
while svar == "ja":     # funker så lenge brukeren svarer 'ja'
    venn = input("Skriv inn en venn :")
    bursdag = int(
        input("Når har " + venn.capitalize() + " bursdag? eks:(mmdd): "))   # capitalize hjelper å skrive første bokstav stor
    if bursdag < 1232:      # Dersom brukeren skriver et gyldig input som er mindre enn 1232
        # 'bursdag' vil settes som innholdverdi til 'nøkkelverdi' venn i ordboken til 'venner'
        venner[venn] = bursdag
        # lower vil gjøre alle bokstavene små
        svar = input("Vil du legge inn flere venner? ja/nei:").lower()
    else:
        print("Dessverre, ugyldig bursdag, skriv som 1227 for 27 desember!")

for v in venner:        # vil skrive ut hva inneholder i ordboken
    print(v, ":", venner[v])
