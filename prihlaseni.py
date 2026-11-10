from sprava_uzivatelu import Sprava_uzivatelu



class Uzivatel():
    def __init__(self,jmeno,prijmeni,heslo,role=None):
        self.jmeno=jmeno
        self.prijmeni=prijmeni
        self.heslo=heslo 
        self.role=role
        


    def vytvoreni_hesla(self):
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


    def zalozeni_uzivatele(self):
    
        jmeno=input("zadej jmeno")
        prijmeni=input("zadej prijmeni")
        heslo=self.vytvoreni_hesla()
        uzivatel=Uzivatel(jmeno,prijmeni,heslo,"zakaznik")
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


    def zmena_hesla(self):
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


