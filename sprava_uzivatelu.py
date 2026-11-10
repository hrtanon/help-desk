import random
from prihlaseni import Uzivatel



class Sprava_uzivatelu():
    def __init__(self):
        self.uzivatele=[]



    # cilem je ted vytvorit fuknci pro administratory kdy vygeneruje nahodne heslo pro techniky podle ktreho se se poprve prihlasi abych je odlisil od uzivatele







    def zalozeni_uzivatele(self):
            zakaznik=zakaznik
            jmeno=input("zadej jmeno")
            prijmeni=input("zadej prijmeni")
            heslo=self.vytvoreni_hesla()
            uzivatel=Uzivatel(jmeno,prijmeni,heslo,zakaznik)
            self.uzivatele.append(uzivatel)
            print("uzivatel zaregistrovan")
    
    
    def prihlaseni(self):
        """_summary_ overuje zda zadavane udaje se nachazi v listu uzivatele
        pokud ano vrati true jinak cykli
    
        Returns:
            _type_: _description_
            """        
        while True:
            jmeno=input("zadej jmeno")
            
            for uzivatel in self.uzivatele:
                if uzivatel.jmeno==jmeno:
                    prijmeni=input("zadej prijmeni")
                    if uzivatel.prijmeni==prijmeni:
                        heslo=input("zadej heslo")
                        if uzivatel.heslo==heslo:
                            print("jste prihlaseni")
                            return True
                        else:
                            print("spatne heslo")
                            continue
                    else:
                        print("spatne prijmeni")
                        continue
            else:
                print("spatne jmeno")
                continue



    def generace_hesla(self):
        admin=admin   #sahuioasfhuasuhfoisndýgfinsaudiluhgasdgfhsaoídáfzhsagfhsghsahg
        if self.role==admin:
            for i in range(0,5):

                a=random.randint(0,99)
                nahodne_heslo+=a
                return nahodne_heslo

        else: 
            print("nemate opravneni")




    def prihlaseni_technika(self):
            """_summary_ overuje zda zadavane udaje se nachazi v listu technika
            pokud ano vrati true jinak cykli
        
            Returns:
                _type_: _description_
                """ 
            technik=technik #asfuhasfhdafsadjigopsadvnsapodifhuewsuhofgsbdvoausd365109948796410       
            while True:
                jmeno=input("zadej jmeno")
                
                for uzivatel in self.uzivatele:
                    if uzivatel.jmeno==jmeno:
                        prijmeni=input("zadej prijmeni")
                        if uzivatel.prijmeni==prijmeni:
                            heslo=input("zadej heslo")
                            if uzivatel.heslo==heslo:
                                print("jste prihlaseni")
                                self.role=technik
                                return True
                            else:
                                print("spatne heslo")
                                continue
                        else:
                            print("spatne prijmeni")
                            continue
                    else:
                        print("spatne jmeno")
                        continue
    