lucky_numbers = []

string = (f"\nGlückliche Zahlen sind eine besondere Kategorie von natürlichen Zahlen, die durch eine\n"
          f"spezielle iterative Prozedur definiert werden. Hier ist die formelle Definition:\n"
          f"Eine Zahl) 𝑛 n ist eine glückliche Zahl (engl. 'happy number'), wenn die folgende Prozedur irgendwann\n"
          f"die Zahl 1 ergibt: Ersetze die Zahl durch die Summe der Quadrate ihrer Ziffern. Wiederhole den Vorgang\n"
          f"mit der neuen Zahl. Wenn diese Iteration irgendwann die Zahl 1 ergibt, dann ist die ursprüngliche Zahl\n"
          f" 𝑛 n eine glückliche Zahl. Falls der Prozess in einer Schleife endet, die nicht die Zahl 1 enthält, \n"
          f"ist 𝑛 n keine glückliche Zahl (sondern eine 'unglückliche Zahl'). Hier ist ein Beispiel zur Verdeutlichung:\n"
          f"\nNehmen wir die Zahl 19: \n"
          f"Berechne die Summe der Quadrate der Ziffern: 1² + 9² = 1 + 81 = 82\n"
          f"Wiederhole den Vorgang mit 82: 8² + 2² = 64 + 4 = 68\n"
          f"Wiederhole den Vorgang mit 68: 6² + 8² = 36 + 64 = 100\n"
          f"Wiederhole den Vorgang mit 100: 1² + 0² + 0² = 1\n"
          f"\nDa wir am Ende 1 erreichen, ist 19 eine glückliche Zahl.\n"
          f"\n-----------------------------------------------------------------------------------------------------------\n")

print(string)

anzahl = int(input("Aus wie vielen Zahlen wollen Sie glückliche Zahlen suchen ?: "))
for i in range(1, anzahl + 1):
    lucky_numbers.append(i)
x = 2
while x < len(lucky_numbers):
    for i in range(len(lucky_numbers)):
        if ((i + 1) % x) == 0:
            lucky_numbers[i] = "x"
    j = 0
    for i in lucky_numbers:
        if i == "x":
            lucky_numbers.pop(j)
        j += 1
    for b in lucky_numbers:
        if x < b:
            x = b
            break

print(f"Von {anzahl} Zahlen sind das die Glücklichen Zahlen:\n")
enum_numbers = enumerate(lucky_numbers)
for nr, zahl in enum_numbers:
    print(f"Nr.{nr}: {zahl}")
