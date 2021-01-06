x = int(input("quanti voti ha ricevuto il primo candidato? "))
y = int(input("quanti voti ha ricevuto il secondo candidato? "))
pc = (x + y)/100
if x > y:
    print("il primo ha vinto con ", x/pc)
elif x == y:
    print("pari")
else:
    print("il secondo ha vinto con ", y/pc)