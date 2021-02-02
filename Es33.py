# in un laboratorio di analisi i pazienti sono sottoposti ad esame
# secondo l'ordine di arrivo (usa una struttura di coda per memorizzare i nomi):
# srivi il programma che registri i nomi dei pazienti man mano che arrivano.
# visualizza poi il primo paziente che deve essere sottoposto all'esame.

pazienti = []
paziente = ""
while paziente != "stop" :
    paziente = (input("inserire nome del paziente \n"))
    pazienti.append(paziente)
if paziente == "stop" :
    print (pazienti[0])



