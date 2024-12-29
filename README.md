# Sklep Zoologiczny - Aplikacja Backendowa i Mobilna

## Opis projektu

Projekt jest kompletnym rozwiązaniem dla sklepu zoologicznego, który oferuje:
- Rejestrację i logowanie użytkowników,
- Przeglądanie produktów, zwierząt i roślin,
- Dodawanie produktów do koszyka oraz składanie zamówień,
- Wysyłanie powiadomień e-mail o wysłanych zakupach i odbiorze osobistym.

Projekt składa się z trzech głównych części:
1. **Backend**: API oparte na Flasku w Pythonie, które realizuje logikę biznesową.
2. **Frontend**: Aplikacja internetowa w React, która komunikuje się z backendem.
3. **Aplikacja mobilna Android**: Aplikacja na system Android, która umożliwia użytkownikom przeglądanie produktów i składanie zamówień.

Projekt korzysta z **Docker** oraz **Docker Compose** do uruchomienia backendu oraz bazy danych PostgreSQL w kontenerach.

## Struktura projektu

Projekt ma następującą strukturę katalogów:




### Wymagania

- **Docker** i **Docker Compose** muszą być zainstalowane na Twoim systemie.
- **Python 3.x** (jeśli chcesz uruchomić backend lokalnie bez Docker).
- **Android Studio** do uruchomienia aplikacji mobilnej.
- **Node.js** i **npm** do uruchomienia aplikacji frontendowej.

### Uruchomienie projektu

#### 1. Uruchomienie całego projektu za pomocą Docker Compose

Aby uruchomić cały projekt, przejdź do katalogu, w którym znajduje się plik `docker-compose.yml`, a następnie wykonaj następujące polecenia:

```bash
# Budowanie i uruchamianie kontenerów
docker-compose up --build
```