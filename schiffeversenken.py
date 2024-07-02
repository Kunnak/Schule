import random

# Spielfeld erstellen
def erstelle_spielfeld(size):
    spielfeld = [['     '] + [f'[{i + 1:2d} ]' for i in range(size)]]
    # Hinzufügen der Überschrift für die Spalten
    # Hinzufügen der Zeilen
    for i in range(size):
        spielfeld.append(
            [f'[{i + 1:2d} ]'] + ["[   ]"] * size)  # Hier füge ich die Zeilennummerierung hinzu (von 1 bis size)

    return spielfeld

# Spielfeld anzeigen
def anzeigen_spielfeld(spielfeld):
    for row in spielfeld:
        print(' '.join(row))


# Schiffe auf dem Spielfeld platzieren
def schiffe_platzieren(spielfeld, num_ships):
    for _ in range(num_ships):
        row = random.randint(1, len(spielfeld) - 1)
        col = random.randint(1, len(spielfeld) - 1)
        spielfeld[row][col] = "[ 0 ]"


# Überprüfen ob der Spieler ein Schiff getroffen hat
def check_schuss(spielfeld, row, col):
    if spielfeld[row][col] == "[ 0 ]":
        spielfeld[row][col] = "[ X ]"
        return True
    else:
        spielfeld[row][col] = "[ M ]"
        return False

# Spiel-Abbruch-Bedingung
def game_over(spielfeld):
    for row in spielfeld:
        if "[ 0 ]" in row:
            return False
    return True

# Main-Funktion
def spielen(size):
    spielfeld = erstelle_spielfeld(9)

    schiffe_platzieren(spielfeld, 10)

    while not game_over(spielfeld):
        print(" \n")
        anzeigen_spielfeld(spielfeld)
        try:
            print("\n")
            guess_row = int(input("Wähle eine Reihe (1 - " + str(size) + "): [>= 10 for exit]"))
            guess_col = int(input("Wähle eine Spalte (1 - " + str(size) + "): [>= 10 for exit] "))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib ganze Zahlen ein.")
            continue

        if guess_row >= 10 or guess_col >= 10:
            quit()
        if guess_row < 0 or guess_row > size or guess_col < 0 or guess_col > size:
            print("Ungültige Koordinaten. Bitte versuche es erneut.")
            continue

        if check_schuss(spielfeld, guess_row, guess_col):
            print("\n")
            print("Treffer! Gut gemacht.")
        else:
            print("----------------------------------------------------------\n")
            print("Verfehlt. Versuche es noch einmal.")

    print("Glückwunsch! Du hast alle Schiffe versenkt.")


# Starten des Spiels
spielen(9)
