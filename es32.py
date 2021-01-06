'''Implementa l'algoritmo per il calcolo della soluzione di un'equazione di primo grado ax + b = 0.
Il processo risolutivo dipende dai valori assunti dai coefficienti a e b secondo la tabella che segue
per a == 0 e b == 0: indeterminata
per a == 0 e b != 0: impossibile
per a != 0 e b == 0: x = 0
per a != 0 e b != 0: x = -b/a'''

a = int(input("metti il parametro [a] "))
b = int(input("metti il parametro [b] "))
print("L'equazione è: ax + b = 0\nL'equazione risulta: x = -b/a")

if a == 0 and b == 0:
    print("L'equazione è indeterminata perchè risulta: x = -( 0 / 0 )")
elif a == 0 and b != 0:
    print("L'equazione è impossibile perchè risulta: x = -(",b,"/ 0 )")
elif a != 0 and b == 0:
    print("L'equazione è determinata perchè risulta: x = 0")
else:
    print("L'equazione è determinata perchè risulta: x = ", -(b/a))