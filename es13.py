'''Verifica se un numero è pari o dispari (un numero è pari quando il resto della divisione intera per 2 è 0)'''

Nuinserito = int(input("Inserisci un numero intero. Il numero è: "))
if Nuinserito%2 == 0:
    print("Il numero inserito, (", Nuinserito, "), è pari")
else:
    print("Il numero inserito, (", Nuinserito, "), è dispari")