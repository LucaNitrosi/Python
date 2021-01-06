stipendi1 = 0
count = 0
while True:
    stipendi = int(input("guadagno dipendente?"))
    if stipendi == -1:
        break
    stipendi1 += stipendi
    count += 1
print(stipendi1 / count)