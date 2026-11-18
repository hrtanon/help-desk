
from modules.help_desk import Help_desk


helpdesk = Help_desk()

while True:
    print("\n--- HELP DESK ---")
    print("1. Nový úkol")
    print("2. Seznam úkolů")
    print("3. Vyhledat úkol")
    print("4. Smazat úkol")
    print("5. Konec")

    volba = input("Vyber možnost: ")

    if volba == "1":
        helpdesk.novy_task()

    elif volba == "2":
        helpdesk.seznam()

    elif volba == "3":
        try:
            id = int(input("Zadej ID úkolu: "))
            task = helpdesk.najdi_dle_id(id)

            if task is None:
                print("Task nebyl nalezen.")
            else:
                print(task.info())

        except ValueError:
            print("ID musí být číslo.")

    elif volba == "4":
        try:
            id = int(input("Zadej ID úkolu ke smazání: "))
            helpdesk.delete_dle_id(id)

        except ValueError:
            print("ID musí být číslo.")

    elif volba == "5":
        print("Ukončuji HelpDesk.")
        break

    else:
        print("Neplatná volba.")
