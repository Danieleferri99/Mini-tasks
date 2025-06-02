name = (input("come ti chiami?"))
eta = int(input("quanti anni hai?"))

if eta <18:
    print("accesso negato: sei minorenne")
else:
    vip = input("hai un invito vip? (si/no) ")
    if vip.lower() =="no":
        print("accesso negato: non hai l'invito")
    elif vip.lower() =="si":
        print("benvenuto nell'area vip")
        
