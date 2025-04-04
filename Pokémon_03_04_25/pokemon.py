import pandas as pd
import random

pokemon_data = pd.read_csv('Pokémon_03_04_25/pokemon.csv')
punti_utente = 100

probabilita_rarita = {
    'Comune': 0.7,
    'Non Comune': 0.2,
    'Rara': 0.09,
    'Ultra Rara': 0.01
}

def sbusto():
    pacchetto = []
    punti_guadagnati = 0
    for i in range(5):
        rarita_scelta = random.choices(list(probabilita_rarita.keys()),weights=probabilita_rarita.values(),k=1)[0]

        carta = pokemon_data[pokemon_data['Rarità'] == rarita_scelta].sample(n=1).iloc[0]
        pacchetto.append(carta)

        if rarita_scelta == 'Comune':
            punti_guadagnati += 1
        elif rarita_scelta == 'Non Comune':
            punti_guadagnati += 10
        elif rarita_scelta == 'Rara':
            punti_guadagnati += 30
        elif rarita_scelta == 'Ultra Rara':
            punti_guadagnati += 104

    return pacchetto, punti_guadagnati



def mostra_collezione(pacchetto):
        print("Collezione:")
        collezione = pd.DataFrame(pacchetto)
        for carta in collezione():
            print(carta)


def salva_collezione(pacchetto):
    collezione = pd.DataFrame(pacchetto)
    collezione.to_csv('collezione.csv')
    print("Collezione salvata in collezione.csv")


while True:
    print("cosa vuoi fare?")
    print("1. Apri un pacchetto")
    print("2. Esci")
    print("3. mostra punti guadagnati")
    print("4. mostra collezione")
    print("5. salva collezione")
    scelta = int(input("Inserisci la tua scelta: "))
    if scelta == 1:
        if punti_utente >= 10:
            punti_utente -= 10
            pacchetto, punti_guadagnati = sbusto() 
            punti_utente += punti_guadagnati 
            print("Hai aperto un pacchetto!")
            for carta in pacchetto:
                print(carta)
            print(f"Hai guadagnato {punti_guadagnati} punti!")
            print(f"Punti totali: {punti_utente}")
        else:
            print("Non hai abbastanza punti per aprire un pacchetto.")

    elif scelta == 2:
        print("addio!")
        break

    elif scelta == 3:
        print(f"Hai {punti_utente} punti.")

    elif scelta == 4:
        mostra_collezione(pacchetto)

    elif scelta == 5:
        salva_collezione(pacchetto)

    else:
        print("inserisci un valore valido")
