




class Task:
    """Třída ukládá úkol a provádí operace, které se ho týkají."""
    POVOLENE_STATUSY = ["hotovo", "probiha", "ceka", "opravuje se"]
        
    
    def __init__(self, id, title, popis, zadavatel, stav, technik=None, coment=None):
        self.title = title
        self.popis = popis
        self.zadavatel = zadavatel
        self.stav = stav
        self.coment = coment
        self.id = id
        self.technik = technik

    def info(self):
        """Vrátí informace o úkolu."""
        return f"{self.title}, {self.id}, {self.popis}, {self.zadavatel}, {self.coment},{self.stav}"

    
    def zmena_hodnot(self,title,popis,coment):
        """ulozi hodnoty od uživatele."""
        
        self.title = title
        self.popis = popis
        self.coment = coment


    def zmena_statusu(self, new_status):
        """Změní stav úkolu na jeden z povolených stavů."""
        
        self.stav = new_status
        
        
        
    def __str__(self):
        return f"[{self.id}] {self.title} | {self.stav}"

    def ulozeni_technika(self, new_technik):
        """Změní technika po dvojím zadání jeho jména."""
        self.technik = new_technik
        return 


    def pridat_popis(self, new_popis):
        """Přidá nový text k dosavadnímu popisu."""
        self.popis = self.popis + "\n" + new_popis
        

    
    def vypis_popis(self):
        """_summary_ vypise dosavadni popis
        """        
        return f"popis je: {self.popis}"
