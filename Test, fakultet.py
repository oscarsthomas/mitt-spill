import time

def Intro():
    print("Du er en nylig utdannet politi mann, og venter på ditt første oppdrag")
    print("Du blir undertrykt av de andre eldre politi mennene fordi du ikke")
    print("har fått gjort noen store oppdrag enda.")
    time.sleep(2)
    print("Du får beskjed at det er en farlig kriminell som er på rømmen fra")
    print("fengselet. Ingen av de eldre politimennene ønsker å ta oppdraget")
    time.sleep(2)
    
def fvalg():
    x = ""
    while x != "1" and x != "2":
        x = input("Ønsker du å ta oppdraget (1), eller tør du heller ikke å ta oppdraget (2)? ")
    return x
    
def vei1():
    print()
    print("Forbryteren har vært på frifot nå i 12 timer.")
    
def valg11():
    x = ""
    while x!= "1" and x != "2":
        print("Hvordan ønsker du å finne informasjon om forbryteren?")
        x = input("Ønsker du å se på filene hans (1), eller spørre kolegaer (2)? ")
    return x
    
def vei11():
    print("Du ser på filene hans, og ser at han egentlig er uskyldig og velger å la han gå")
    
def vei12():
    print("Du hører fra kolegaene dine at han drepte 26 politi-menn før han ble tatt inn")
    print("og velger derfor å slutte å forfølge han")

def vei2():
    print()
    print("Du gir opp oppdraget, og lar politiskjefen ta over.")
    time.sleep(2)
    print("Du finner ut senere at dette var like greit, siden det")
    print("nå har gått 2 år siden han kom seg ut, og han har ikke kommet tilbake")
    



spilleIgjen = "ja"
while spilleIgjen == "ja" or spilleIgjen == "j":     
    Intro()
    valg = fvalg()
    if valg == "1":
        vei1()
        valg1 = valg11()
        if valg1 == "1":
            vei11()
        else:
            vei12()
    else:
        vei2()
    spilleIgjen = input("Vil du spille igjen? (ja eller j for å starte igjen)")