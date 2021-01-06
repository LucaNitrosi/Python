a = []
b = []
while True:
    nome = input("parole da contare? (premi 0)")
    a.append(nome)
    if nome == "0":
        break
    b.append(len(nome))
print(b)