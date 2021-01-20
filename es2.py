'''Data la parabola y = ax² + bx + c, definisci due funzioni per calcolarne i punti significativi: vertice e fuoco.
Le due funzioni ricevono come parametri a, b, c e restituiscono il valore calcolato'''

def fuoco(a, b, c):
    delta = b**2 - 4*a*c
    x_F = -b/2*a
    y_F = (1-delta)/4*a
    return x_F, y_F

def vertice(a, b, c):
    delta = b**2 - 4*a*c
    x_V = -b/2*a
    y_V = -delta/4*a
    return x_V, y_V

def inizio():
    a = int(input("Definisci il valore a: "))
    b = int(input("Definisci il valore b: "))
    c = int(input("Definisci il valore c: "))
    ris_F = fuoco(a, b, c)
    ris_V = vertice(a, b, c)
    print("Le coordinate del vertice della parabola: ", ris_V)
    print("Le coordinate del fuoco della parabola: ", ris_F)
   
inizio()