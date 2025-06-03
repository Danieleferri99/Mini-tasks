
nomi = []
counter = 0 

print("inserisci nomi, dopo di che digitare 'fine'. ")
while True:
    nome = input(". ")
    if nome == "fine":
        break
    counter += 1
    nomi.append(nome)

lunghezza = len(nome)

print(f"i tuoi nomi sono: {counter} ")
for nome in nomi:
    print(f"- {nome}")
    if len(nome) > 10: 
        print(f"il tuo nome '{nome}' è troppo lungo è di {lunghezza} caratteri, arrivederci ")
    
        
