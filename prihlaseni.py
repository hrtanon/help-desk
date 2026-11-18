from sprava_uzivatelu import Sprava_uzivatelu



class Uzivatel():
    def __init__(self,jmeno,prijmeni,heslo,role=None):
        self.jmeno=jmeno
        self.prijmeni=prijmeni
        self.heslo=heslo 
        self.role=role
        


    def vytvoreni_hesla(self):
        """_summary_ vytvori heslo overi ze neni prazne pole a overi ze bylo zadano dvakrat

        Returns:
            _type_: _description_
        """        
        while True:

            heslo=input("zadej heslo")
            if heslo=="":
                print(f"heslo nemuze byt prazdne")
                continue

            heslo2=input("zadej heslo znovu")
            if heslo==heslo2:
                print("heslo bylo ulozeno")
                self.heslo=heslo
                return heslo
            else:
                print("chyba zkuste to znovu")
                continue


    def zmena_hesla(self):
        """_summary_ overi zda heslo ktere zada zadatel tady v tehlke funkci se shoduji s ulozenym v listu
        pak vola vytvoreni hesla 

        Returns:
            _type_: _description_
        """        
        while True:
                jmeno=input("zadej jmeno")
                heslo=input("zadej heslo")
                for uzivatel in self.uzivatele:
                    if uzivatel.jmeno==jmeno:
                            if heslo==uzivatel.heslo:
                                heslo==self.vytvoreni_hesla()
                                uzivatel.heslo=heslo
                                return "heslo bylo ulozeno"
                    
                    else:
                        print("chyba zkuste to znovu")
                        continue


