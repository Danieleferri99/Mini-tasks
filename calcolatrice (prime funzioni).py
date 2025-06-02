def presentati(eta):
    print(f"ciao {nome}, hai {eta} anni")
def raddoppia(num1):
    return (num1 * 2)

nome = input("come ti chiami? ")
eta = input("quanti anni hai? ")
presentati(eta)
num1 = int(input("scegli un numero, te lo raddoppio "))
raddoppia(num1)
risultato = raddoppia(num1)

print(risultato)