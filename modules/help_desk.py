
from task import Task
import os


class Help_desk():
    def __init__(self):
        self.tasks=[]
        self.next_id=1
    
    def aha(self):
        task=self.najdi_dle_id(id)
    
    
        
    
    def novy_task(self,title,popis,coment=None):
        """
        vytvori task s pouzitim funkce zisk hondot z tridy task
        

        Args:
            uzivatel zada udaje do funkce zisk hodnot
        result: vytvoreny novy task a pridan na seltnam tasku a zvetso se next id o 1
        """       
        if title=="":
            print("zadejte nazev")
            return None 
        id=self.next_id
        self.next_id+=1
        
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


    def zmena_statusu(self,id,new_status):
        """Změní stav úkolu na jeden z povolených stavů."""
        task=self.najdi_dle_id(id)
        if new_status not in Task.POVOLENE_STATUSY:
            print("Neplatný status.")
            return None
    
        task.zmena_statusu(new_status)
        return f"Status byl změněn na {new_status}"





def pridat_popis(self,id,new_popis):
        """Přidá nový text k dosavadnímu popisu."""
        task=self.najdi_dle_id(id)
        task.vypis_popis()
        task.pridat_popis(new_popis)
        
        return task.vypis_popis()
        

def zmena_technika(self,id, new_technik1,new_technik2):
        """Změní technika po dvojím zadání jeho jména."""
        task=self.najdi_dle_id(id)
        if new_technik1=="":
            print("neplatne jmeno technika")
            return False
        if new_technik1 == new_technik2:
            task.ulozeni_technika(new_technik1)
            return f"technik zmenen na {new_technik1}"

        print("Jména se neshodují.")