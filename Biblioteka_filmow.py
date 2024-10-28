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

class Serial(Film):
    def __init__(self, tytul, rok_wydania, gatunek, numer_odcinka, numer_sezonu):
        super().__init__(tytul, rok_wydania, gatunek)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
    def __str__(self):
        return f"{self.tytul} S{self.numer_sezonu:02}E{self.numer_odcinka:02}"

# Definicja funkcji
def filter_by_type(items, type_class):
    filtered_items = [item for item in items if type(item) is type_class]
    filtered_items.sort(key=lambda item: item.tytul)
    return filtered_items

#funkcja get_movies, która filtruje listę i zwraca tylko filmy.
def get_movies(items):
    return filter_by_type(items, Film)

#funkcja get_series, która filtruję listę i zwraca tylko seriale.
def get_series(items):
    return filter_by_type(items, Serial)

#funkcja search, która wyszukuje film lub serial po jego tytule.
def search(tytuł, items):
    for item in items:
        if item.tytul == tytuł:
            return item
    return None

#funkcja generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
def generate_views(items):
    item = random.choice(items)
    item.liczba_odtworzen += random.randint(1, 100)

#funkcja, która uruchomi generate_views 10 razy.
def run_generate_views_10_times(items):
    for _ in range(10):
        generate_views(items)

#funkcja top_titles(), która zwraca wybraną ilość najpopularniejszych tytułów z biblioteki.
def top_titles(items, n, content_type=None):
    if content_type == "film":
        items = get_movies(items)
    elif content_type == "serial":
        items = get_series(items)
    items.sort(key=lambda item: item.liczba_odtworzen, reverse=True)
    return items[:n]

#Główna część programu
if __name__ == "__main__":
    lista_tytulow = []
    film_1 = Film("Pulp Fiction", 1994, "Komedia")
    film_2 = Film("Lśnienie", 1980, "Horror")
    film_3 = Film("Szeregowiec Ryan", 1998, "Dramat")
    serial_1 = Serial("The Simpsons", 1989, "Komedia", 5, 1)
    serial_2 = Serial("Dexter", 2006, "Kryminał", 3, 5)
    serial_3 = Serial("Gra o tron", 2011, "Fantasy", 7, 7)
    serial_4 = Serial("Gambit królowej", 2020, "Dramat", 1, 3)
    lista_tytulow.extend([film_1, film_2, film_3, serial_1, serial_2, serial_3, serial_4])
    
     #Sprawdzenie działania fukcji get_movies
    print("Filmy:")
    filmy = get_movies(lista_tytulow)
    for film in filmy:
        print(film)

    #Sprawdzenie działania fukcji get_series
    print("\nSeriale:")
    seriale = get_series(lista_tytulow)
    for serial in seriale:
        print(serial)
