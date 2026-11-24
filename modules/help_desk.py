
from task import Task
import os


class Help_desk():
    def __init__(self):
        self.tasks=[]
        self.next_id=1
    
    
    def zisk_hodnot():
            """Načte hodnoty od uživatele."""
            while True:
                title = input("Zadej název: ")
                popis = input("Zadej popis: ")
                coment = input("Zadej komentář (nepovinný): ")
    
                if title=="":
                    print("zadejte nazev")
                    continue
            
                Task.zmena_hodnot(title, popis, coment)
                return f"hotovo problem {title} ulozen"
    
        
    
    def novy_task(self):
        """
        vytvori task s pouzitim funkce zisk hondot z tridy task
        

        Args:
            uzivatel zada udaje do funkce zisk hodnot
        result: vytvoreny novy task a pridan na seltnam tasku a zvetso se next id o 1
        """        
        id=self.next_id
        self.next_id+=1
        title,popis,coment = Task.zisk_hodnot()
        ukol=Task(id,title,popis,"uzivatelů","zalozen","technik",coment)
        self.tasks.append(ukol)
        print("task zalozen")
    
    def seznam(self):
        """ vypise na radky po sobe vsechny tasky
        """        
        for task in self.tasks:
            print(task)
    

    def najdi_dle_id(self,id):
        """Vrátí úkol podle ID, pokud existuje."""

        for task in self.tasks:
            if task.id == id:
                return task
            
            
    def delete_dle_id(self, id):
        """Odstraní úkol podle ID."""

        task = self.najdi_dle_id(id)

        if task is None:
            print("Task s tímto ID neexistuje.")
            return False

        self.tasks.remove(task)
        print("Task byl odstraněn.")
        return True
    






    def zmena_status_dle_id(self,id):
        """_summary_ porovna zda se id nachai v listu a kdyz ho najde tak tomnu tasku zmeni status
        

        Args:
            id (_type_): _description_

        Returns:
            _type_: _description_
        """        
        for task in self.tasks:
            if task.id ==id :
                self.zmena_statusu()
                return f"status zmenen"
            continue

        return f"id neni"


    def zmena_statusu(self, stav=None):
            """Změní stav úkolu na jeden z povolených stavů."""
            povolene_statusy = ["hotovo", "probiha", "ceka", "opravuje se"]
    
            while True:
                print(povolene_statusy)
                new_status = input("Vyber status: ")
    
                if new_status not in povolene_statusy:
                    print("Neplatný status.")
                    continue
    
                Task.zmena_statusu(new_status)
                return f"Status byl změněn na {new_status}"





def pridat_popis(self):
        """Přidá nový text k dosavadnímu popisu."""
        Task.vypis_popis()
        new_popis = input("Přidej popis: ")
        Task.pridat_popis(new_popis)
        
        return Task.vypis_popis()
        

def zmena_technika(self, technik=None):
        """Změní technika po dvojím zadání jeho jména."""
        while True:
            new_technik1 = input("Zadej jméno nového technika: ")
            new_technik2 = input("Zadej znovu jméno technika: ")

            if new_technik1 == new_technik2:
                Task.ulozeni_technika(new_technik1)
                return f"technik zmenen na {new_technik1}"

            print("Jména se neshodují.")