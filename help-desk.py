from modules.task import Task
import os


class Help_desk():
    def __init__(self):
        self.tasks=[]
        id
        self.next_id=1
    
    
    
    
    def novy_task(self):
        """
        vytvori task s pouzitim funkce zisk hondot z tridy task
        

        Args:
            uzivatel zada udaje do funkce zisk hodnot
        result: vytvoreny novy task a pridan na seltnam tasku a zvetso se next id o 1
        """        
        id=self.next_id
        self.next_id+=1
        title,popis,coment = self.zisk_hodnot()
        ukol=Task(id,title,popis,coment)
        self.tasks.append(ukol)
        print("task zalozen")
    
    def seznam(self):
        """ vypise na radky po sobe vsechny tasky
        """        
        for task in self.tasks:
            print(task)
    
    def delete_dle_id(self,id):
        return 
    