class SportActivity:
    def __init__(self, name, max_participants, duration_hours, days_and_times, required_experience="Keine"):
        self.name = name
        self.max_participants = max_participants
        self.duration_hours = duration_hours
        self.days_and_times = days_and_times
        self.required_experience = required_experience

    def display_info(self):
        print("Aktivität:", self.name)
        print("Maximale Teilnehmerzahl:", self.max_participants)
        print("Kursdauer:", self.duration_hours, "Stunden")
        print("Termine:", self.days_and_times)
        print("Erforderliche Vorkenntnisse:", self.required_experience)
        print()

def main():
    global auswahl
    mountainbike = SportActivity("Mountainbike fahren", 10, 2, "Montag bis Freitag ab 18 Uhr")
    klettern = SportActivity("Klettern", 6, 2, "Dienstag 20 bis 22 Uhr", "Vorkenntnisse erforderlich")
    aerobic_i = SportActivity("Aerobic Stufe I (Anfänger)", 15, 1, "Montag 17 bis 18 Uhr")
    aerobic_ii = SportActivity("Aerobic Stufe II (mit Vorkenntnissen)", 12, 1, "Mittwoch 9 bis 10 Uhr")
    aerobic_iii = SportActivity("Aerobic Stufe III (Experten)", 10, 1, "Freitag 20 bis 21 Uhr")
    zumba = SportActivity("Zumba", 20, 1, "Donnerstag 20 bis 21 Uhr")
    billard = SportActivity("Billard", 8, None, "Freitag ab 18 Uhr")
    bowling = SportActivity("Bowling", 24, None, "Montag ab 19 Uhr")
    yoga = SportActivity("Yoga", 15, 2, "Mittwoch 18 bis 20 Uhr")

    if auswahl == "mountainbike":
        mountainbike.display_info()
    if auswahl == "klettern":
        klettern.display_info()
    if auswahl == "aerobic1":
        aerobic_i.display_info()
    if auswahl == "aerobic2":
        aerobic_ii.display_info()
    if auswahl == "aerobic3":
        aerobic_iii.display_info()
    if auswahl == "zumba":
        zumba.display_info()
    if auswahl == "billard":
        billard.display_info()
    if auswahl == "bowling":
        bowling.display_info()
    if auswahl == "yoga":
        yoga.display_info()

print("\n")
print("Die Aktivitäten stehen zur Verfügung:    [Auswahlmöglichkeiten]")
print("\n")
print("Mountainbike fahren                      [mountainbike]")
print("Klettern                                 [klettern]")
print("Aerobic Stufe 1 (für Anfänger)           [aerobic1]")
print("Stufe 2 (mit Vorkenntnissen)             [aerobic2")
print("Stufe 3 (Experten)                       [aerobic3]")
print("Zumba                                    [zumba]")
print("Billard                                  [billard]")
print("Bowling                                  [bowling]")
print("Yoga                                     [yoga]")
print("\n")

auswahl = input("Welche Aktivität wollen Sie sich angucken ?: ").lower()
main()
