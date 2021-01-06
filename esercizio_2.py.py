nomi = []
voti = []
for x in range(2):
    a = input("nome candidato?")
    b = int(input("quanti voti ha?"))
    nomi.append(a)
    voti.append(b)
nomi.sort()
voti.sort()
voti.reverse()
print(nomi)
print(voti)