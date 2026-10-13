





class Task():
    """_summary_
    class uklada task dela vsechny operace s nim.

    """    
    def __init__(self,id,title ,popis, zadavatel, stav ,technik, coment=None ):
        self.title=input(title)
        self.popis=input(popis)
        self.zadavatel=input(zadavatel)
        self.stav=(stav)
        self.coment=(coment)
        self.id=(id)
        self.technik=technik

    def info(self):
        """_summary_
        fuknce vipise promene ve fukci abychpm o ni vedeli info

        Returns:
            _type_: _description_
        """        
        return f"{self.title}, {self.id},{self.popis},{self.zadavatel},{self.coment}"

    def zisk_hodnot(self):
        """_summary_
        nacte hodnoty od uzivatele a overi jejich typ
        returns: overene hodnoty
        """    
        while True:
            try: 
                title=str(input("zadej nazev"))
                popis=str(input("zadej popis"))
                coment=str(input("zadej komentar"))

                if coment==" ":
                    coment==None
                    #overuje kdyz je komentar nepoviny ze kdyz je zadny tak to ho nebude vyzadovat

                return title,popis,coment
            except ValueError:
                continue



    def zaloz_task(self,title,popis,coment):
        task=Task(self.zisk_hodnot())
        #patri do task manageru na sem
    
    def zmena_statusu(self,status):
        """_summary_
        vypise povolene statusy z kterych se pak vybere pozadovany a zmeni puvodni status na ten druhy
        """        
        while True:
            povolene_statusy=["hotovo","probiha","ceka","opravuje se"]
            print(povolene_statusy)
            new_status=input("vyber status")
            if new_status!=povolene_statusy:
                print("neplatny status")
                continue
            else:
                self.status=new_status
                return f"status byl zmenen na {new_status}"


    def zmena_technika(self,technik):
        while True:

            new_technik1=input("zadej jmeno noveho technika")
            new_technik2=input("zadej znovu jmeno technika")
            if new_technik1==new_technik2:

                technik=new_technik1
                return technik
            else:
                print("jmena se neshoduji")
                continue


    def pridat_popis(self,popis):
        print(f"minuly popis je{self.popis}")
        new_popis=str(input("pridej popis"))
        popis=popis+new_popis
        return popis