




class Task:
    """Třída ukládá úkol a provádí operace, které se ho týkají."""

    def __init__(self, id, title, popis, zadavatel, stav, technik, coment=None):
        self.title = title
        self.popis = popis
        self.zadavatel = zadavatel
        self.stav = stav
        self.coment = coment
        self.id = id
        self.technik = technik

    def info(self):
        """Vrátí informace o úkolu."""
        return f"{self.title}, {self.id}, {self.popis}, {self.zadavatel}, {self.coment}"

    def zisk_hodnot(self):
        """Načte hodnoty od uživatele."""
        while True:
            try:
                title = input("Zadej název: ")
                popis = input("Zadej popis: ")
                coment = input("Zadej komentář (nepovinný): ")

                if coment == "":
                    coment = None

                return title, popis, coment

            except ValueError:
                continue


    def zmena_statusu(self, stav=None):
        """Změní stav úkolu na jeden z povolených stavů."""
        povolene_statusy = ["hotovo", "probiha", "ceka", "opravuje se"]

        while True:
            print(povolene_statusy)
            new_status = input("Vyber status: ")

            if new_status not in povolene_statusy:
                print("Neplatný status.")
                continue

            self.stav = new_status
            return f"Status byl změněn na {new_status}"

    def zmena_technika(self, technik=None):
        """Změní technika po dvojím zadání jeho jména."""
        while True:
            new_technik1 = input("Zadej jméno nového technika: ")
            new_technik2 = input("Zadej znovu jméno technika: ")

            if new_technik1 == new_technik2:
                self.technik = new_technik1
                return self.technik

            print("Jména se neshodují.")

    def pridat_popis(self, popis):
        """Přidá nový text k dosavadnímu popisu."""
        print(f"Minulý popis je: {self.popis}")
        new_popis = input("Přidej popis: ")
        self.popis = self.popis + "\n" + new_popis
        return self.popis
