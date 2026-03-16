# Profiling in Python

In dieser Session schauen wir uns an, wie wir die **Laufzeit von Python-Code messen** können. Profiling hilft uns zu verstehen, *wo* unser Programm Zeit verbringt, damit wir gezielt optimieren können – und nicht nur raten.

------

## Warum Profiling wichtig ist

In vielen Python- und Data-Science-Projekten arbeiten wir mit **großen Datensätzen** oder **rechenintensiven Algorithmen**. Manchmal ist der Code „schnell genug“, manchmal ganz offensichtlich nicht. Profiling hilft dir zu entscheiden:

- *Wo* verbringt mein Programm die meiste Zeit?
- *Welche* Funktionen oder Code-Stellen sind die eigentlichen Flaschenhälse?
- *Welche* Optimierung wird wirklich einen Effekt haben?

Typische Fehler ohne Profiling:

- Du optimierst Code, der sowieso schon schnell ist, während das eigentliche Problem woanders liegt.
- Du wechselst zu einem komplexeren Algorithmus oder Library, „weil es schneller sein sollte“ – ohne zu messen.
- Du verlässt dich auf Intuition statt auf Messdaten.

**Faustregel:**
 Nicht raten, wie schnell etwas ist – **erst messen, dann optimieren**.

------

## Das Modul `time` verwenden

Das Modul `time` bietet einfache Funktionen, um Zeiten zu messen. Es ist oft das erste Werkzeug, wenn man nur ein grobes Gefühl für die Laufzeit bekommen möchte.

Ein typisches Muster:

```python
import time

def integer_sum(count_to: int):
    total = 0
    for i in range(int(count_to)):
        total += i
    return total

start_time = time.time()
integer_sum(1_000_000)
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")
```

**Erklärung:**

- `time.perf_counter()` liefert eine hochaufgelöste Zeitmessung und ist gut geeignet, um kurze Dauer zu messen.
   (Es ist für Benchmarks in der Regel **besser als** `time.time()`.)
- Wir speichern die Zeit **vor** und **nach** dem Funktionsaufruf und bilden die Differenz.
- Das Ergebnis ist eine **einzelne Messung** der Laufzeit.

**Einschränkungen:**

- Es wird nur ein Lauf gemessen – das ist anfällig für Rauschen (z.B. wenn dein Rechner gerade beschäftigt ist).
- Man kann leicht versehentlich Dinge mitmessen, die man nicht möchte (z.B. Printing, Datenaufbau).
- Gut für schnelle, grobe Checks – aber nicht ideal für präzise Vergleiche.

------

## Das Modul `timeit` verwenden

Das Modul `timeit` ist für **zuverlässige Micro-Benchmarks** gedacht. Es:

- führt deinen Code viele Male aus,
- versucht Rauschen zu reduzieren,
- liefert eine Gesamtzeit, aus der du Durchschnittswerte berechnen kannst.

Ein einfaches Beispiel:

```python
import timeit

code_to_test = """
total = 0
for i in range(int(1e5)):
    total += i
"""

execution_time = timeit.timeit(stmt=code_to_test, number=100)
print(f"Average execution time: {execution_time / 100:.6f} seconds")
```

**Erklärung:**

- `timeit.timeit(stmt, number)` führt den String `stmt` **`number`-mal** aus und gibt die *Gesamtzeit* zurück.
- Wir teilen durch `number`, um die **durchschnittliche Zeit pro Lauf** zu erhalten.
- Ein String ist für kleine Beispiele praktisch; in größeren Projekten benchmarkt man meist direkt eine Funktion.

Beispiel mit Funktion statt String:

```python
import timeit

code_to_test = """
total = 0
for i in range(int(1e5)):
    total += i
"""

execution_time = timeit.timeit(stmt=code_to_test, number=100)
print(f"Average execution time: {execution_time / 100:.6f} seconds")
```

Vorteile:

- Der Code bleibt **normaler Python-Code**,
- du bekommst Editor-Unterstützung (Linting, Autocomplete),
- längere Beispiele sind leichter wartbar.

------

## Jupyter-Notebook-Magics

In Jupyter-Notebooks gibt es praktische **Magic-Befehle**, die `time` und `timeit` für dich kapseln:

- `%time` / `%%time` – einzelne Messung,
- `%timeit` / `%%timeit` – mehrere Messungen, ähnlich wie `timeit.timeit()`.

### Line- vs. Cell-Magics

- `%time` oder `%timeit` am Anfang einer **einzelnen Zeile**:

  ```python
  %time
  
  integer_sum(1_000_000)
  ```

- `%%time` oder `%%timeit` am Beginn einer **Zelle**:

  ```python
  %%time
  
  result = integer_sum(1_000_000)
  result2 = integer_sum(1_000_000)
  ```

`%timeit` (und `%%timeit`) wird:

- den Code mehrfach ausführen,
- die **beste** oder **mittlere** Laufzeit anzeigen,
- zusätzlich die **Standardabweichung** ausgeben.

Du kannst die Anzahl der Durchläufe steuern:

```python
%%timeit -n 10 -r 5

integer_sum(1000_000)
```

- `-n 10`: 10 Loops pro Messung
- `-r 5`: 5 Wiederholungen der gesamten Messung

Insgesamt wird die Funktion hier also `10 * 5 = 50` Mal ausgeführt.

------

## Praxisaufgabe: Minimum in einer Liste finden

Jetzt wenden wir diese Werkzeuge auf eine einfache, aber typische Aufgabe an:

> **Finde den kleinsten Wert in einer großen Liste von Zufallszahlen.**

Wir implementieren drei Methoden:

1. Eine manuelle **for-Schleife**,
2. Die eingebaute Funktion **`min()`**,
3. Eine Lösung auf Basis von **NumPy**.

Anschließend messen und vergleichen wir die Laufzeiten.

### Setup: Erzeugen einer großen Zufallsliste

```python
import random

random.seed(42)  # Experiment reproduzierbar machen

random_list = [random.randint(0, 1_000_000) for _ in range(1_000_000)]
```

**Erklärung:**

- `random.seed(42)` sorgt dafür, dass wir bei jedem Lauf die gleichen Zufallszahlen erhalten – praktisch für reproduzierbare Experimente.
- Wir erzeugen eine Liste mit 1.000.000 Integern im Bereich `0` bis `1_000_000`.

------

### Methode 1: For-Schleife

```python
def find_min_loop(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value
```

**Erklärung:**

- Wir initialisieren `min_value` mit dem **ersten Element** der Liste.
- Wir laufen einmal über die Liste und aktualisieren `min_value`, wenn wir einen kleineren Wert finden.
- Zeitkomplexität: **O(n)** (jedes Element wird genau einmal betrachtet).

------

### Methode 2: Eingebaute Funktion `min()`

```python
def find_min_builtin(lst):
    return min(lst)
```

**Erklärung:**

- Die eingebaute Funktion `min()` läuft ebenfalls in **O(n)**.
- Sie ist in **C implementiert** und in der Regel deutlich schneller als unsere Python-Schleife.
- Außerdem ist sie lesbarer und weniger fehleranfällig.

------

### Methode 3: NumPy verwenden

```python
import numpy as np

def find_min_numpy(lst):
    np_array = np.array(lst)
    return np.min(np_array)
```

**Erklärung:**

- Wir konvertieren die Python-Liste zunächst in ein `numpy.ndarray`.
- Dann verwenden wir `np.min()`, um das Minimum zu berechnen.
- NumPy-Operationen sind in C implementiert und oft sehr schnell auf großen Arrays.

Aber: Wir müssen den **Konvertierungsaufwand** berücksichtigen:

- Das Erzeugen des NumPy-Arrays (`np.array(lst)`) kostet bereits Zeit.
- Wenn wir `find_min_numpy()` nur einmal aufrufen, kann der Konvertierungs-Overhead dafür sorgen, dass diese Methode *langsamer* als `min(lst)` ist.
- NumPy lohnt sich besonders, wenn:
  - die Daten **bereits** in einem NumPy-Array vorliegen oder
  - wir viele Operationen auf demselben Array ausführen.

------

## Performance vergleichen

Jetzt verwenden wir `timeit`, um die drei Ansätze zu messen.

> **Hinweis:** Im Notebook kann man stattdessen `%%timeit` verwenden.
>  Hier nutzen wir `timeit.timeit()`, damit der Code auch als Skript funktioniert.

Stelle sicher, dass die Funktionen und `random_list` bereits definiert sind.

### Messung Methode 1: For-Schleife

```python
import timeit

execution_time_loop = timeit.timeit(
    stmt='find_min_loop(random_list)',
    setup='from __main__ import find_min_loop, random_list',
    number=10,
)

print(f"Average execution time (loop): {execution_time_loop / 10:.6f} seconds")
```

### Messung Methode 2: Eingebaute Funktion `min()`

```python
execution_time_builtin = timeit.timeit(
    stmt='find_min_builtin(random_list)',
    setup='from __main__ import find_min_builtin, random_list',
    number=10,
)

print(f"Average execution time (builtin): {execution_time_builtin / 10:.6f} seconds")
```

### Messung Methode 3: NumPy

```python
execution_time_numpy = timeit.timeit(
    stmt='find_min_numpy(random_list)',
    setup='from __main__ import find_min_numpy, random_list, np',
    number=10,
)

print(f"Average execution time (NumPy): {execution_time_numpy / 10:.6f} seconds")
```

### Ergebnisse interpretieren

Typischerweise wirst du etwas in dieser Art beobachten:

- Die eingebaute Funktion `min()` ist **am schnellsten**,
- die manuelle for-Schleife ist **langsamer**,
- die NumPy-Variante ist:
  - sehr schnell, wenn die Daten bereits ein NumPy-Array sind,
  - aber langsamer als `min()`, wenn man die Kosten für die Konvertierung der Liste mit einrechnet.

Wichtige Erkenntnis:

> Alle drei Methoden haben die gleiche asymptotische Komplexität **O(n)**,
>  aber **Konstanten** machen einen großen Unterschied – und in C implementierte Built-ins sind oft deutlich schneller als reines Python.

------

## Fortgeschrittenes Profiling mit `cProfile` und `snakeviz`

Timing ist super, wenn du ganze Funktionen oder Alternativen vergleichen möchtest. Aber was, wenn du ein **größeres Programm** hast und wissen willst, *welche inneren Funktionen* langsam sind?

Dafür nutzen wir **Profiler** wie `cProfile`, die zeigen:

- wie oft Funktionen aufgerufen werden,
- wie viel Zeit jede Funktion benötigt,
- wie viel Zeit in Unteraufrufen steckt.

Mit `snakeviz` können wir die Ergebnisse dann visualisieren.

------

### Den Beispielcode verstehen

Wir profilieren folgendes Skript, das grob den Ablauf simuliert:

- Datengenerierung,
- Validierung/Filterung,
- Suche nach Zielwerten,
- langsames Ausgeben des Ergebnisses im Terminal.

```python
import random
import time

def generate():
    data = [random.randint(0, 99) for _ in range(1, 100000)]
    data = validate(data)
    return data

def validate(data, chance_percent=50):
    data = [x for x in data if random.randint(1, 100) > chance_percent]
    return data

def search_function(data, targets=[42, 17]):
    counter = 0
    for value in data:
        if value in targets:
            counter += 1
    return counter

def ascii_renderer(result):
    message = f"I found the targets {result} times!"
    for char in message:
        time.sleep(0.01)
        print(char, end="")
    print()  # For newline after the message.

def main():
    data = generate()
    result = search_function(data)
    ascii_renderer(result)

if __name__ == "__main__":
    main()
```

Was machen die Funktionen?

- `generate()`
   Erzeugt eine Liste zufälliger Integer und ruft `validate()` zur Filterung auf.
- `validate(data, chance_percent)`
   Behält jedes Element mit einer Wahrscheinlichkeit von `(100 - chance_percent)%`.
   Bei `chance_percent=50` bleibt grob die Hälfte der Werte übrig.
- `search_function(data, targets)`
   Zählt, wie viele Einträge in `data` gleich einem der Zielwerte sind.
- `ascii_renderer(result)`
   Gibt eine Nachricht Zeichen für Zeichen mit kleiner Pause (`sleep`) aus.
   Das simuliert eine langsame Ausgabeoperation.

------

### Docstrings ergänzen und Code aufräumen

Wir versehen den Code mit Docstrings und machen ihn etwas klarer:

```python
import random
import time

def generate():
    """
    Generate a list of random integers between 0 and 99, validate it, and return the data.

    Returns:
        list[int]: A validated list of random integers.
    """
    data = [random.randint(0, 99) for _ in range(1, 100000)]
    data = validate(data)
    return data

def validate(data, chance_percent=50):
    """
    Filter the data list based on a random chance.

    Args:
        data (list[int]): The list of integers to validate.
        chance_percent (int, optional): Percentage chance to filter out elements.
            Higher values remove more elements. Defaults to 50.

    Returns:
        list[int]: The filtered list of integers.
    """
    data = [x for x in data if random.randint(1, 100) > chance_percent]
    return data

def search_function(data, targets=[42, 17]):
    """
    Count how many times target values appear in the data list.

    Args:
        data (list[int]): The list of integers to search.
        targets (list[int], optional): Target integers to search for.
            Defaults to [42, 17].

    Returns:
        int: The count of target values found in the data.
    """
    counter = 0
    for value in data:
        if value in targets:
            counter += 1
    return counter

def ascii_renderer(result):
    """
    Print a message character by character with a delay.

    Args:
        result (int): The result count to include in the message.
    """
    message = f"I found the targets {result} times!"
    for char in message:
        time.sleep(0.01)
        print(char, end="")
    print()  # For newline after the message.

def main():
    """
    Orchestrate the program: generate data, search, and render the result.
    """
    data = generate()
    result = search_function(data)
    ascii_renderer(result)

if __name__ == "__main__":
    main()
```

**Warum vor dem Profiling aufräumen?**

- Das Profil zeigt dir, welche Funktion langsam ist – dann sollten Funktionsnamen und Docstrings so klar sein, dass du sofort verstehst, was dort passiert.
- Sauberer Code macht es leichter, Profiling-Ergebnisse zu interpretieren und sinnvolle Optimierungen vorzunehmen.

------

### Profiling mit `cProfile`

`cProfile` ist ein in Python eingebauter Profiler, der Funktionsaufrufe und Laufzeiten misst.

#### `cProfile` von der Kommandozeile ausführen

Speichere das Skript als `profile_example.py` und führe im Terminal aus:

```bash
python -m cProfile profile_example.py
```

Dadurch wird dein Skript mit dem Profiler ausgeführt und eine Tabelle mit Profiling-Daten ausgegeben.

#### Ausgabe interpretieren

Eine typische Ausgabe könnte so aussehen:

```text
         50007 function calls in 1.215 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    1.215    1.215 profile_example.py:42(main)
        1    0.197    0.197    1.210    1.210 profile_example.py:8(generate)
        1    0.167    0.167    1.013    1.013 profile_example.py:15(validate)
    99999    0.846    0.000    0.846    0.000 profile_example.py:16(<listcomp>)
        1    0.001    0.001    0.004    0.004 profile_example.py:22(search_function)
    49996    0.004    0.000    0.004    0.000 profile_example.py:24(<listcomp>)
        1    0.000    0.000    0.000    0.000 profile_example.py:33(ascii_renderer)
       32    0.000    0.000    0.000    0.000 {built-in method time.sleep}
```

Bedeutung der Spalten:

- **ncalls** – Anzahl der Aufrufe der Funktion.
- **tottime** – Zeit in dieser Funktion **ohne** die Zeit der Unterfunktionen.
- **percall** (tottime) – `tottime / ncalls`.
- **cumtime** – kumulierte Zeit in dieser Funktion **inklusive** Unterfunktionen.
- **percall** (cumtime) – `cumtime / ncalls`.
- **filename:lineno(function)** – Position, an der die Funktion definiert ist.

#### Ergebnis interpretieren – welche Teile brauchen am längsten?

Schau dir die Zeilen mit den größten `cumtime`- und/oder `tottime`-Werten an:

- `main` hat `cumtime ~ 1.215s` – das ist im Wesentlichen die Gesamt-Laufzeit des Programms.
- `generate` hat eine große `cumtime` – hier und in den darunter aufgerufenen Funktionen passiert viel.
- Die List-Comprehension in `validate` (`<listcomp>`) hat eine hohe `tottime` – dort wird viel CPU-Zeit verbraten (Filtern der Daten).
- In dieser Beispielausgabe sind `ascii_renderer` und `time.sleep` sehr günstig (nahe 0), was an Zahlen und Auflösung liegt. Wenn wir `time.sleep(0.01)` aber z.B. auf `time.sleep(0.1)` erhöhen, wird `time.sleep` plötzlich zum dominanten Kostenfaktor.

Typische Frage an dieser Stelle:

> **Welche Funktion oder Code-Stelle sollten wir zuerst optimieren?**

Mögliche Antworten:

- Die **List-Comprehension in `validate`** – sie wird sehr oft aufgerufen und braucht viel Zeit.
- Wenn `time.sleep` mehr Zeit verbraucht, könnte man die Pause verkleinern oder im Produktivcode ganz entfernen.

Wichtige Erkenntnis:

> Profiling zeigt dir *genau*, wo Zeit verbrannt wird.
>  Du musst nicht raten, welche Funktion langsam ist – du kannst es **aus der Tabelle ablesen**.

------

### Visualisierung mit `snakeviz`

Texttabellen sind mächtig, aber manchmal ist es leichter, Performance-Daten **grafisch** zu sehen.

`snakeviz` kann Profildaten einlesen und als **interaktive Visualisierung** darstellen.

#### Installation

```bash
pip install snakeviz
```

#### Profildaten erzeugen

Anstatt die Statistiken direkt auszugeben, schreiben wir sie in eine Datei:

```bash
python -m cProfile -o profile_data.prof profile_example.py
```

- Mit `-o profile_data.prof` speichern wir die Profiling-Daten in einer Datei.

#### Profil visualisieren

Starte nun `snakeviz`:

```bash
snakeviz profile_data.prof
```

Es sollte sich ein Browser-Fenster (oder Tab) öffnen mit:

- einem **Sunburst-Diagramm** oder **Icicle-Plot** und
- einer Tabelle mit Funktionsstatistiken.

#### Visualisierung interpretieren

Im Sunburst-Diagramm:

- In der **Mitte** ist typischerweise die Startfunktion (z.B. `main`).
- Jede „Scheibe“ bzw. jeder Segment-Ring entspricht einem Funktionsaufruf.
- Die **Größe** eines Segments entspricht der dort verbrachten Zeit.
  - Große Segmente = viel Zeit = interessant für Optimierungen.
- Durch Klicken auf ein Segment kannst du hineinzoomen und Details sehen.

Fragen, die du dir stellen kannst:

- Welches Segment ist **am größten**?
- Liegt die meiste Zeit in:
  - der Datengenerierung?
  - der Validierung/Filterung?
  - der Suche?
  - der Ausgabe / dem Rendering?

Danach kannst du entscheiden, wo sich Optimierungen lohnen:

- Algorithmus austauschen,
- effizientere Datenstruktur verwenden,
- unnötige Arbeit vermeiden,
- langsame I/O-Operationen aus dem „Hot Path“ entfernen usw.

------

## Fazit

Kurze Zusammenfassung:

- **Einfache Zeitmessung**
  - `time.perf_counter()` für schnelle, manuelle Messungen,
  - `timeit` für zuverlässige Micro-Benchmarks,
  - Jupyter-Magics `%time` und `%timeit` für bequemes Messen im Notebook.
- **Fortgeschrittenes Profiling**
  - `cProfile` liefert Funktionsstatistiken: Aufrufzahlen, Laufzeiten, kumulierte Zeiten.
  - `snakeviz` macht diese Daten als Visualisierung leichter zugänglich.
- **Typischer Optimierungs-Workflow**
  1. **Messen** – mit Timing/Profiling echte Flaschenhälse finden.
  2. **Verstehen** – analysieren, *warum* diese Stelle langsam ist (Algorithmus, Datenstruktur, I/O, …).
  3. **Ändern** – verbesserten Ansatz implementieren.
  4. **Nochmals messen** – prüfen, ob es wirklich schneller wurde und ob der Flaschenhals sich verschoben hat.

**Wichtige Punkte:**

- Nicht blind optimieren – **zuerst profilieren**.
- Eingebaute Funktionen und gut optimierte Libraries (z.B. NumPy) sind oft schneller als selbstgeschriebene Schleifen.
- Sauberer, gut dokumentierter Code erleichtert das Interpretieren von Profiling-Ergebnissen.
- Profiling und Optimierung sind **iterative Prozesse** – du wiederholst den Zyklus, wenn sich dein Code oder deine Daten ändern.