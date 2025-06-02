def saluta_utente(nome):
    print(f"ciao {nome} benvenuto nel supermercato! ")
def prezzo_totale(articolo1, articolo2, articolo3):
    return (articolo1 + articolo2 + articolo3)
def prezzo_scontato(risultato, sconto):
    return risultato - ((risultato * sconto) / 100)

nome = input("come ti chiami? ")
saluta_utente
articolo1 = float(input("indicami il prezzo di 3 articoli "))
articolo2 = float(input("un altro "))
articolo3 = float(input("un ultimo "))
sconto = 10
risultato = prezzo_totale(articolo1, articolo2, articolo3)
sconto_finale = prezzo_scontato(risultato, sconto)

if risultato > 100:
    print("il prezzo è stato scontato del 10%, per un totale di: ",sconto_finale)
else:
    print("il prezzo è di: ",risultato)

