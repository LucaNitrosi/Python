risposta=""
dizionario = {
    "italia": "roma",
    "germania": "berlino",
    "francia": "parigi"
}

while risposta != "stop":
    risposta= input("inserisci il nome di una nazione\n")
    if risposta == "stop":
        print (dizionario)
        break
    if risposta in dizionario:
        capitale = input("quale e la sua capitale?\n")
        if capitale == dizionario[risposta]:
            print("bravo") 
        else: 
            print("sbagliato")
    else:
        Ccapitale = input("Inserisci la capitale di questa nazione, non era presente nella lista\n")
        dizionario[risposta]=Ccapitale
        print('aggiunta')