import json
def policz_cene(produkt):
    wartosc = produkt["cena"] * produkt["ilosc"]
    if produkt["ilosc"] > 5:
        produkt["rabat"] = 0.20
    elif produkt["ilosc"] > 3:
        produkt["rabat"] = 0.10
    else:
        produkt["rabat"] = 0
    wartosc = wartosc - (wartosc * produkt["rabat"])
    return wartosc
def drogie_produkty(produkty):
    wynik = []
    for x in produkty:
        cena = policz_cene(x)
        if cena > 100:
            wynik.append(x)
    return wynik
def wartosc_drogich(produkty):
    wartosc = 0
    wartosc_przed_rabatem = 0
    drogie = drogie_produkty(produkty)
    for x in drogie:
        cena = policz_cene(x)
        wartosc_przed_rabatem = wartosc_przed_rabatem + (x["cena"] * x["ilosc"])
        wartosc = wartosc + cena
    return wartosc_przed_rabatem, wartosc
def produkty_duza_ilosc(produkty):
    wynik = []
    for x in produkty:
        if x["ilosc"] > 3:
            wynik.append(x)
    return wynik
def najdrozszy_produkt(produkty):
    najwieksza = produkty[0]

    for x in produkty:
        cena = policz_cene(x)
        cena_najwiekszej = policz_cene(najwieksza)
        if cena > cena_najwiekszej:
            najwieksza = x
    return najwieksza
def raport_najdrozszy(produkty):
    najdrozszy = najdrozszy_produkt(produkty)
    cena = policz_cene(najdrozszy)
    print("Najdroższy produkt:", najdrozszy["nazwa"])
    print("Cena:", cena, "zł")
    print("Ilość:", najdrozszy["ilosc"])
def raport_duza_ilosc(produkty):
    duza_ilosc = produkty_duza_ilosc(produkty)
    suma = 0
    suma_przed_rabatem = 0
    for x in duza_ilosc:
        cena = policz_cene(x)
        suma_przed_rabatem = suma_przed_rabatem + (x["cena"] * x["ilosc"])
        suma = suma + cena
        print(x["nazwa"], "- ilość:", x["ilosc"], "- wartość:", cena, "zł")
    print("Łączna wartość przed rabatem:", suma_przed_rabatem, "zł")
    print("Łączna wartość po rabacie:", suma, "zł")
def najtanszy_produkty(produkty):
    najtanszy = produkty[0]
    for x in produkty:
        cena = policz_cene(x)
        cena_najtanszy = policz_cene(najtanszy)
        if cena < cena_najtanszy:
            najtanszy = x 
    return najtanszy
def najwieksza_ilosc_sztuk(produkty):
    najwiekszy = produkty[0]
    for x in produkty:
        if x["ilosc"] > najwiekszy["ilosc"]:
           najwiekszy = x
    return najwiekszy
def najmniejsza_ilosc_sztuk(produkty):
    najmniejszy = produkty[0]
    for x in produkty:
        if x["ilosc"] < najmniejszy["ilosc"]:
            najmniejszy = x
    return najmniejszy
def raport_magazynu(produkty):
    wynik = len(produkty)
    print("=== PODSUMOWANIE MAGAZYNU ===")
    suma_sztuk = 0
    licznik_dwojek = 0
    licznik_poza_przedzialem = 0
    suma_duzych = 0
    licznik_duzych = 0
    for x in produkty:
        if x["ilosc"] < 2 or x["ilosc"] > 5:
            print("Produkt poza zakresem:", x["nazwa"], "- ilość:", x["ilosc"])
        if x["ilosc"] > 3:
            licznik_duzych = licznik_duzych + 1
            suma_duzych = suma_duzych + x["ilosc"]     
        suma_sztuk = suma_sztuk + x["ilosc"] 
        if x["ilosc"] == 2:
            licznik_dwojek = licznik_dwojek + 1
        if x["ilosc"] < 2 or x["ilosc"] > 5:
            licznik_poza_przedzialem = licznik_poza_przedzialem + 1
    if licznik_duzych > 0:
            srednia_duzych = suma_duzych / licznik_duzych
            print("Średnia dla produktów powyżej 3 sztuk:", srednia_duzych)        
    else:
            print("Brak produktów powyżej 3 sztuk.")          
    print("Liczba produktów z ilością poniżej 2 lub powyżej 5:", licznik_poza_przedzialem)           
    print("Produkty z ilością = 2 sztuk:", licznik_dwojek)          
    print("Produkty z ilością powyżej 3 sztuk:", licznik_duzych)      
    print("Liczba produktów:", wynik)
    print("Łączna liczba sztuk:", suma_sztuk) 
def znajdz_produkt(produkty,nazwa):
    for x in produkty:
        if nazwa.strip().lower() == x["nazwa"].lower():
           return x 
    return None 
produkt = {
    "nazwa": "Pizza",
    "cena": 35,
    "ilosc": 5
}
produkt2 = {
    "nazwa": "Burger",
    "cena": 25,
    "ilosc": 2
}
produkt3 = {
    "nazwa": "Pizza XXL",
    "cena": 50,
    "ilosc": 6
}
produkty = [produkt, produkt2, produkt3]


def zapisz_magazyn(produkty):
    with open("magazyn.json", "w", encoding="utf-8") as plik:
        json.dump(produkty, plik, ensure_ascii=False, indent=4)
def wczytaj_magazyn():
    try:
        with open("magazyn.json", "r", encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return None
zapisane_produkty = wczytaj_magazyn()
if zapisane_produkty is not None:
    produkty = zapisane_produkty            
def raporty(produkty):
    suma = 0 
    suma_sztuk = 0
    suma_przed_rabatem = 0
    print("=== Produkty o wartości powyżej 100 zł ===")
    for x in produkty:
        suma_sztuk = suma_sztuk + x["ilosc"]
        suma_przed_rabatem = suma_przed_rabatem + (x["cena"] * x["ilosc"])
        cena = policz_cene(x)
        wartosc_przed_rabatem = x["cena"] * x["ilosc"]
        suma = suma + cena 
        if cena > 100: 
            print(x["nazwa"], "- wartość przed rabatem:", wartosc_przed_rabatem, "zł")
            print(x["nazwa"], "- wartość po rabacie:", cena, "zł")
    print("Wszystkie sztuki:", suma_sztuk)       
    print("Łączna wartość wszystkich produktów:", suma, "zł")
    print("Łączna wartość wszystkich produktów przed rabatem:", suma_przed_rabatem, "zł")
    drogie = drogie_produkty(produkty)
    duza_ilosc = produkty_duza_ilosc(produkty)
    suma = 0 
    raport_duza_ilosc(produkty)
    raport_najdrozszy(produkty)
    print("Produkty o wartości powyżej 100 zł:")
    for x in drogie:
        wartosc_przed_rabatem = x["cena"] * x["ilosc"]
        wartosc_po_rabacie = policz_cene(x)
        print("-", x["nazwa"], "- ilość:", x["ilosc"], "- przed rabatem:", wartosc_przed_rabatem, "zł - po rabacie:", wartosc_po_rabacie, "zł")
    suma_drogich_przed, suma_drogich_po = wartosc_drogich(produkty)
    print("Łączna wartość drogich produktów przed rabatem:", suma_drogich_przed, "zł")
    print("Łączna wartość drogich produktów po rabacie:", suma_drogich_po, "zł")
    print("Produkty z ilością powyżej 3 sztuk:")
    for x in duza_ilosc:
        wartosc_przed_rabatem = x["cena"] * x["ilosc"]
        wartosc_po_rabacie = policz_cene(x)
        print("-", x["nazwa"], "- ilość:", x["ilosc"], "- przed rabatem:", wartosc_przed_rabatem, "zł - po rabacie:", wartosc_po_rabacie, "zł")
    najtanszy = najtanszy_produkty(produkty)
    print("Najtańszy produkt:", najtanszy["nazwa"])
    wynik = najwieksza_ilosc_sztuk(produkty)
    print("Największa ilość:", wynik["nazwa"], "- ilość sztuk:", wynik["ilosc"])
    wynik = najmniejsza_ilosc_sztuk(produkty)
    print("Najmniejsza ilość:", wynik["nazwa"], "- ilość sztuk:", wynik["ilosc"])
    wynik = len(produkty)
    print("Liczba różnych produktów:", wynik)
    raport_magazynu(produkty)
def dodaj_produkt(produkty):
    nazwa = input("Podaj nazwę produktu: ").strip()
    if nazwa == "":
        print("Nie wpisano nazwy produktu")
        return
    while True:
        try:
           cena = float(input("Podaj cenę produktu: "))
           if cena < 0:
               print("Cena nie może być ujemna")
               continue
           break
        except ValueError:
            print("Cena musi być liczbą!")
    while True:
        try:
            ilosc = int(input("Podaj ilość produktu: "))
            if ilosc <= 0:
                print("Ilość musi być większa od zera")
                continue
            break
        except ValueError:
            print("Ilość musi być liczbą całkowitą!")    
    nowy_produkt = {
        "nazwa": nazwa,
        "cena": cena,
        "ilosc": ilosc
        }
    for x in produkty:
        if x["nazwa"].lower() == nowy_produkt["nazwa"].lower() and x["cena"] == nowy_produkt["cena"]:
            x["ilosc"] = x["ilosc"] + nowy_produkt["ilosc"]
            zapisz_magazyn(produkty)
            print("Zwiększono ilość produktu:", x["nazwa"])
            return
    produkty.append(nowy_produkt)
    zapisz_magazyn(produkty)   
    print("Dodano produkt:", nazwa)    
def main():
    szukana_nazwa = input("Jakiego produktu szukasz? ")
    szukana_nazwa = szukana_nazwa.strip()
    if szukana_nazwa == "":
        print("Nie wpisano nazwy produktu")
    else:
        znaleziony = znajdz_produkt(produkty, szukana_nazwa)
        if znaleziony is not None:
            print("Znaleziono produkt:", znaleziony["nazwa"])
            print("Cena za sztuke:", znaleziony["cena"])
            print("Ilosc z magazyna:", znaleziony["ilosc"])
            wartosc_produktu = znaleziony["cena"] * znaleziony["ilosc"]
            wartosc_po_rabacie = policz_cene(znaleziony)
            print("Wartość wszystkich sztuk:", wartosc_produktu, "zł")
            print("Rabat:", znaleziony["rabat"] * 100, "%")
            print("Wartość po rabacie:", wartosc_po_rabacie, "zł")
        else:
            print("Nie znaleziono produktu")
#main()
licznik_bledow = 0            
while True:
    wybor = input("Co chcesz uruchomić? 1 - wyszukiwarka, 2 - raporty, 3 - dodaj produkt, 0 - wyjście: ")
    if wybor == "0":
        if licznik_bledow == 0:
            print("Brawo! Nie popełniono żadnych błędów!")
        elif 1 <= licznik_bledow <= 3:
            print("Zdarza się, następnym razem będzie lepiej!")
        else:
            print("Sprawdź dostępne opcje menu.")
        break
    elif wybor == "1":
        main()
    elif wybor == "2":
        raporty(produkty)
    elif wybor == "3":
        dodaj_produkt(produkty)    
    else:
        print("Nie ma takiej opcji")
        licznik_bledow = licznik_bledow + 1
plik = open("test.txt", "w", encoding="utf-8")
plik.write("Sok, 7 zł, 4 sztuki")
plik.close()        