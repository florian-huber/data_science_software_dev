# Warum brauchen wir Testing?

Software kann korrekt aussehen, sauber formatiert sein, ohne Fehlermeldung laufen – und trotzdem **falsche Ergebnisse liefern**.

Testing ist deshalb ein zentraler Bestandteil der Softwareentwicklung. Tests sollen uns systematisch dabei helfen herauszufinden,

- ob Software die festgelegten Anforderungen erfüllt,
- ob typische und ungewöhnliche Eingaben korrekt verarbeitet werden,
- ob Fehlerfälle sinnvoll behandelt werden,
- und ob bereits funktionierender Code nach einer Änderung immer noch funktioniert.

Dabei geht es nicht darum, zu beweisen, dass ein Programm vollkommen fehlerfrei ist. Tests liefern vielmehr **Evidenz dafür, dass sich Software in den von uns geprüften Situationen so verhält, wie wir es erwarten**.

---

## Die Notwendigkeit des Testens

Softwarefehler sind nicht nur kleine Unannehmlichkeiten.

Sie können falsche wissenschaftliche Ergebnisse erzeugen, Systeme zum Absturz bringen, Sicherheitslücken verursachen oder im Extremfall komplette technische Systeme zerstören.

### Ariane 5 – 1996

Am 4. Juni 1996 endete der erste Flug der europäischen Ariane-5-Rakete kurz nach dem Start mit der Zerstörung der Rakete.

Die Untersuchung führte den Ausfall auf Spezifikations- und Designfehler in der Software des inertialen Referenzsystems zurück. Besonders interessant für uns: Der offizielle Untersuchungsbericht stellte ausdrücklich fest, dass die durchgeführten Reviews und Tests das relevante Verhalten nicht ausreichend geprüft hatten und der Fehler durch angemessene Analyse und Tests hätte erkannt werden können.

**Lehre daraus:** Code, der in einem vorherigen System funktioniert hat, funktioniert nicht automatisch unter neuen Bedingungen. Annahmen und Randbedingungen müssen getestet werden.

Quelle: ESA, *Ariane 501 – Inquiry Board Report*, 1996.

### CrowdStrike – 2024

Am 19. Juli 2024 veröffentlichte CrowdStrike ein Konfigurationsupdate für seinen Falcon-Sensor auf Windows-Systemen. Das Update führte weltweit zu Abstürzen von Windows-Rechnern.

In der später veröffentlichten Analyse beschreibt CrowdStrike unter anderem einen Fehler im **Content Validator**: Problematische Daten bestanden die Validierung und wurden anschließend ausgeliefert. Beim Verarbeiten dieser Daten kam es zu einem Speicherzugriffsfehler und schließlich zum Windows-Absturz.

**Lehre daraus:** Tests müssen nicht nur den eigentlichen Programmcode betrachten. Auch Updates, Konfigurationen, Daten und die Systeme, die diese validieren, können Fehler enthalten.

Quelle: CrowdStrike, *Preliminary Post Incident Review*, 2024.

### Fehler sind normal

Eine häufig zitierte Schätzung aus der Software-Engineering-Literatur liegt bei ungefähr **15–50 Fehlern pro 1000 Zeilen ausgeliefertem Code**.

Diese Zahl sollte nicht als exaktes Naturgesetz verstanden werden. Sie hängt stark von Projekt, Entwicklungsmethode und Definition eines Fehlers ab. Interessant ist vielmehr die Größenordnung:

> Auch professionell entwickelte Software enthält Fehler.

Die Schätzung wird unter anderem in einer wissenschaftlichen Diskussion über Fehler in Forschungssoftware aufgegriffen.

Die Konsequenz ist deshalb nicht:

> „Wir müssen einfach besser programmieren.“

Sondern:

> **Wir müssen davon ausgehen, dass wir Fehler machen – und Prozesse entwickeln, mit denen wir diese Fehler entdecken.**

Testing ist einer dieser Prozesse.

---

## Verschiedene Arten von Fehlern

Nicht jeder Programmfehler sieht gleich aus.

### Syntaxfehler

Der Python-Code ist grammatikalisch ungültig:

```python
if x > 5
    print(x)
```

Python kann diesen Code nicht ausführen.

Solche Fehler sind meist relativ leicht zu erkennen, weil Python unmittelbar eine Fehlermeldung erzeugt.

### Exceptions / Laufzeitfehler

Der Code ist syntaktisch korrekt und startet, scheitert aber bei bestimmten Eingaben:

```python
result = 10 / 0
```

Python meldet:

```text
ZeroDivisionError
```

Auch solche Fehler sind zumindest sichtbar.

### Semantische Fehler

Gefährlicher sind Fehler, bei denen das Programm vollständig durchläuft, aber das Ergebnis falsch ist:

```python
def celsius_to_fahrenheit(celsius):
    return celsius * 5 / 9 + 32
```

Der Code läuft.

Es gibt keine Exception.

Aber die Formel ist falsch.

Gerade solche Fehler motivieren automatisierte Tests:

```python
assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
```

---

## Testebenen

Software kann auf unterschiedlichen Ebenen getestet werden.

Sehr vereinfacht können wir von einem kompletten System immer weiter hineinzoomen:

```text
komplettes Programm
        │
        ▼
   Systemtest
        │
        ▼
mehrere Komponenten
        │
        ▼
 Integrationstest
        │
        ▼
 einzelne Funktion
        │
        ▼
    Unit Test
```

### Systemtests

Testen ein größeres Programm als Ganzes.

Beispielsweise könnten wir bei unserem ASCII-Plot-Projekt prüfen:

```bash
uv run python -m ascii_plotter.cli data/points.csv
```

und kontrollieren, ob das vollständige Programm erfolgreich ausgeführt wird.

### Integrationstests

Testen, ob mehrere Komponenten korrekt zusammenarbeiten.

Zum Beispiel:

```text
CSV einlesen
    ↓
Daten verarbeiten
    ↓
Plot erzeugen
```

### Unit Tests

Testen kleine, möglichst klar abgegrenzte Einheiten des Codes.

Typische Units sind:

- eine Funktion,
- eine Methode,
- manchmal eine kleine Klasse.

In dieser Veranstaltung konzentrieren wir uns zunächst auf **Unit Tests**.
