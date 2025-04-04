lista=["ciao","grazie"]

def aggiungi():
    x=input("Inserisci un elemento da aggiungere: ")
    lista.append(x)

def visualizza():
    for i in range(len(lista)):
        print(f"{i+1}. {lista[i]}")

def rimuovi():
    visualizza()
    indice = int(input("Che numero vuoi rimuovere? "))
    if 1 <= indice <= len(lista):
        lista.pop(indice-1)
    else:
        print("Indice non valido.")

def conta():
    print(f"Numero di elementi nella lista: {len(lista)}")

def svuota():
    lista.clear()
    print("Lista svuotata.")

while True:
    print("\nMenu:")
    print("1. Aggiungi")
    print("2. Rimuovi")
    print("3. Conta")
    print("4. Svuota")
    print("0. Esci")
    scelta = int(input("Scegli un'opzione: "))
    if scelta == 1:
        aggiungi()
    elif scelta == 2:
        rimuovi()
    elif scelta == 3:
        conta()
    elif scelta == 4:
        svuota()
    elif scelta == 0:
        print("Uscita dal programma.")
        break
    else:
        print("Opzione non valida. Riprova.")