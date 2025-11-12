# Code-Tests (2)

In diesem Abschnitt gehen wir einen Schritt weiter mit einigen leistungsfähigen `pytest`-Funktionen. Diese Werkzeuge helfen, Absichten klar auszudrücken, Duplikate zu vermeiden und Test-Suites wartbar zu halten – insbesondere wenn Projekte wachsen. Wir betrachten **Fixtures**, **Parametrisierung**, **temporäre Pfade** und **Monkeypatching**. Jede Funktion löst ein typisches Testproblem: *Setup/Teardown*, *viele Eingaben abdecken*, *Dateisystem isolieren* und *das Verhalten von Abhängigkeiten steuern*.

## Fixtures

### Was ist eine Fixture?

Eine **Fixture** ist eine Funktion, die Zustand für Tests vorbereitet. Sie stellt wiederverwendbares Setup bereit: Datenobjekte, temporäre Verzeichnisse, Konfiguration, Verbindungen – alles, was ein Test benötigt, um zuverlässig und reproduzierbar zu laufen. Pytest erkennt Fixtures am Namen und injiziert sie per Funktionsargument in Tests. Das Lifecycle-Management (inkl. Teardown) übernimmt pytest.

### Verwendung und Beispiel

Deklariere eine Fixture mit `@pytest.fixture`. Jeder Test, der den Namen der Fixture als Parameter angibt, erhält deren Rückgabewert. Pytest steuert den Lebenszyklus automatisch.

```python
import pytest

@pytest.fixture
def sample_data():
    # Arrange: stabile Basis für Tests bereitstellen
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    # Act & Assert
    assert sum(sample_data) == 15
```

**Scopes & Organisation (kurz):** Standardmäßig sind Fixtures **funktional** gescoped (pro Test frisch). Mit `scope="class" | "module" | "session"` kannst du Wiederverwendung konfigurieren. Lege breit genutzte Fixtures in `conftest.py` ab, um sie paketweit verfügbar zu machen – ganz ohne Imports.

> Tipp: Bevorzuge Fixtures gegenüber manuellem Setup im Test. Tests werden kürzer, klarer und weniger fragil.

---

## `pytest.mark.parametrize`

### Zweck

Wenn dasselbe Verhalten für viele Eingaben gelten soll, ermöglicht die **Parametrisierung** einen einzelnen Test, der mit verschiedenen Argumenten mehrfach ausgeführt wird. So bleibt der Testcode DRY und macht sichtbar, was wirklich variiert: die Daten, nicht die Logik.

### Beispiel

```python
import pytest

@pytest.mark.parametrize("test_input,expected", [(3, 9), (5, 25), (10, 100)])
def test_square(test_input, expected):
    assert test_input ** 2 == expected
```

Pytest führt `test_square` dreimal aus – je (Input, Expected)-Paar. Für bessere Lesbarkeit kannst du Fälle benennen:

```python
@pytest.mark.parametrize(
    "test_input,expected",
    [(3, 9), (5, 25), (10, 100)],
    ids=["3^2", "5^2", "10^2"]
)
def test_square(test_input, expected):
    assert test_input ** 2 == expected
```

> Tipp: Nutze Parametrisierung statt Schleifen im Test. Scheitert ein Fall, meldet pytest den konkreten Parameter – das vereinfacht die Analyse.

---

## `tmp_path`

### Verwendung

Die eingebaute Fixture `tmp_path` stellt für jeden Test ein isoliertes temporäres Verzeichnis bereit. Ideal, um Code zu testen, der Dateien liest/schreibt, ohne dein reales Arbeitsverzeichnis zu verändern. Die Pfade sind `pathlib.Path`-Objekte und werden nach dem Test automatisch bereinigt.

### Beispiel

```python
def test_create_file(tmp_path):
    temp_dir = tmp_path / "sub"
    temp_dir.mkdir()
    temp_file = temp_dir / "hello.txt"
    temp_file.write_text("Hello, pytest!")

    # Existiert die Datei?
    assert temp_file.is_file()

    # Inhalt prüfen
    assert temp_file.read_text() == "Hello, pytest!"
```

> Tipp: Bevorzuge `tmp_path` gegenüber fest kodierten Pfaden oder dem Repo-Root. Das verhindert flaky Tests und unbeabsichtigte Dateiveränderungen.

---

## Monkeypatch

### Was sind Monkeypatching und Mocking?

**Monkeypatching** bedeutet, Objekte zur Laufzeit zu verändern (z. B. eine Funktion oder ein Attribut auszutauschen) – nur für die Dauer eines Tests. **Mocking** beschreibt allgemein das Ersetzen realer Abhängigkeiten durch kontrollierbare Stellvertreter. In pytest macht die Fixture `monkeypatch` das ohne zusätzliche Bibliotheken sehr bequem.

### Monkeypatch in Pytest

Du kannst Attribute, Umgebungsvariablen und Dictionary-Einträge ersetzen. Das ist nützlich, wenn Code mit dem OS, mit Nutzereingaben oder externen Diensten interagiert.

#### Beispiel: Klassenmethode ersetzen

```python
class MyClass:
    def method(self):
        return "original"

def test_myclass_method(monkeypatch):
    def mock_method(self):
        return "mocked"

    monkeypatch.setattr(MyClass, "method", mock_method)

    my_object = MyClass()
    assert my_object.method() == "mocked"
```

#### Beispiel: Nutzereingabe simulieren

```python
def get_username():
    return input("Enter username: ")

def test_get_username(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "pytest")
    assert get_username() == "pytest"
```

Mehrere Eingaben in Folge lassen sich ebenfalls simulieren:

```python
def user_input():
    x = input("say something: ")
    if x.lower() == "hello":
        print("hello")
    y = input("something else?")
    return x, y

def test_user_input(monkeypatch):
    user_input_generator = iter(["Hello", "Bye"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_input_generator))
    user_x, user_y = user_input()
    assert user_x == "Hello"
    assert user_y == "Bye"
```

#### Beispiel: Umgebungsvariablen

```python
import os

def get_api_key():
    return os.environ.get("API_KEY", "")

def test_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "secret-123")
    assert get_api_key() == "secret-123"
```

> Tipp: Für umfangreiches Mocking bietet das Plugin `pytest-mock` eine `mocker`-Fixture (Wrapper um `unittest.mock`). Für viele Fälle reicht `monkeypatch` allerdings völlig aus – und ist sehr gut lesbar.

---

## Zusammenfassung

Pytests **Fixtures** halten Setup ordentlich und wiederverwendbar, **Parametrisierung** skaliert einen Test über viele Eingaben, **`tmp_path`** isoliert Dateisystem-Interaktionen, und **Monkeypatching** erlaubt es, externes Verhalten zu steuern. Zusammen machen diese Features Tests klarer, schneller zu schreiben und robuster – genau das, was du brauchst, wenn dein Projekt wächst.
