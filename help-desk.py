from modules.task import Task
import os


class Help_desk():
    def __init__(self):
        self.tasks=[]
        id
        self.next_id=1
    
    
    
    
    def novy_task(self,jmeno,):
        id=self.next_id
        self.next_id+=1
        title,popis,coment = self.zisk_hodnot()
        ukol=Task(id,title,popis,coment)
        self.tasks.append(ukol)
        print("task zalozen")
    
    
    