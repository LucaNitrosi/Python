#Costruisci un dizionario ottenuto da quello dell'esercizio precedente (16) invertendo il ruolo di chiave e valore.
#Usa il nuovo dizionario per trovare il nome della nazione, noto il nome della capitale


risposta=""
dizionario = {
   "roma" : "italia" ,
   "berlino" : "germania",
   "parigi" : "francia"
}

while risposta != "stop":
    risposta= input("inserisci il nome di una capitale\n")
    if risposta == "stop":
        print (dizionario)
        break
    if risposta in dizionario:
        nazione= input("quale e la sua nazione?\n")
        if nazione == dizionario[risposta]:
            print("bravo") 
        else: 
            print("sbagliato")
    else:
        n_nazione = input("Inserisci la nazione di questa capitale, non era presente nella lista\n")
        dizionario[risposta]=n_nazione
        print('aggiunta')
