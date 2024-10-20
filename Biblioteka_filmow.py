import random

class Film:
    def __init__(self, tytul, rok_wydania, gatunek):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = 0
    
    def play(self):
        self.liczba_odtworzen += 1
    
    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania})"
    
class Serial:
    def __init__(self, tytul, rok_wydania, gatunek, numer_odcinka, numer_sezonu):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
        self.liczba_odtworzen = 0
    
    def play(self):
        self.liczba_odtworzen += 1
   
    def __str__(self):
        return f"{self.tytul} S{self.numer_sezonu:02}E{self.numer_odcinka:02}"

#Lista przechowująca filmy i seriale     
lista_tytulow = []
film_1 = Film("Pulp Fiction", 1994, "Komedia")
lista_tytulow.append(film_1)
serial_1 = Serial("The Simpsons", 1989, "Komedia", 5, 1)
lista_tytulow.append(serial_1)
film_1.play()
for tytuł in lista_tytulow:
    print(tytuł)

#funkcja get_movies, która filtruje listę i zwraca tylko filmy.
def get_movies():
    filmy = [item for item in lista_tytulow if isinstance(item, Film)]
    filmy.sort(key=lambda film: film.tytul)
    return filmy

#funkcja get_series, która filtruję listę i zwraca tylko seriale.
def get_series():
    seriale = [item for item in lista_tytulow if isinstance(item, Serial)]
    seriale.sort(key=lambda serial: serial.tytul)
    return seriale

#funkcja search, która wyszukuje film lub serial po jego tytule
def search(tytuł):
    for item in lista_tytulow:
        if item.tytul == tytuł:
            return item
    return None

#funkcja generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
def generate_views():
    item = random.choice(lista_tytulow)
    item.liczba_odtworzen += random.randint(1, 100)

#funkcja, która uruchomi generate_views 10 razy.
def run_generate_views_10_times():
    for _ in range(10):
        generate_views()

#funkcja top_titles(), która zwraca wybraną ilość najpopularniejszych tytułów z biblioteki.
def top_titles(n, content_type=None):
    if content_type == "film":
        items = get_movies()
    elif content_type == "serial":
        items = get_series()
    else:
        items = lista_tytulow
    items.sort(key=lambda item: item.liczba_odtworzen)
    return items[:n]