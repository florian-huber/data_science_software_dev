# Working from the Shell: Terminal, Bash und die Kommandozeile

Viele Werkzeuge, die wir im weiteren Verlauf des Kurses verwenden, werden über eine **Kommandozeile** bedient: Git, Python, `uv`, Test- und Linting-Tools, Server, Container und Continuous-Integration-Systeme.

Das Terminal ist deshalb kein nostalgischer Umweg um eine grafische Oberfläche herum. Es ist eine gemeinsame, textbasierte Schnittstelle, über die sich Arbeitsschritte **präzise, wiederholbar und dokumentierbar** ausführen lassen.

> **Ziel dieses Kapitels:** Ihr sollt euch sicher in einem Projektverzeichnis bewegen, Dateien und Ordner verwalten und Programme bzw. Entwicklungswerkzeuge aus der Shell starten können. Es geht **nicht** darum, Bash-Spezialist:innen zu werden.

## Lernziele

Nach diesem Kapitel solltet ihr insbesondere:

- erklären können, was **Terminal**, **Shell**, **Bash** und **CLI** bedeuten,
- mit `pwd`, `ls` und `cd` sicher im Dateisystem navigieren,
- mit `mkdir`, `touch`, `cp`, `mv` und `rm` Dateien und Verzeichnisse verwalten,
- mit `echo` und `cat` einfache Textausgaben und Dateien erzeugen bzw. ansehen,
- relative und absolute Pfade unterscheiden können,
- Python-Code und andere Kommandozeilenprogramme ausführen können,
- einfache Shell-Skripte starten und deren Zweck verstehen,
- gefährliche Dateioperationen erkennen und bewusst ausführen.

---

## Warum überhaupt eine Kommandozeile?

Wer bisher hauptsächlich mit Jupyter Notebooks, VS Code oder grafischen Dateimanagern gearbeitet hat, kann zunächst den Eindruck bekommen, dass die Kommandozeile ein unnötiger zusätzlicher Weg ist. In Software- und Data-Science-Projekten hat sie aber einige entscheidende Vorteile.

### 1. Viele Entwicklungswerkzeuge sind CLI-Programme

Git ist ein gutes Beispiel:

```bash
git status
```

Auch Python-Tools werden häufig so gestartet:

```bash
python analysis.py
uv run pytest
uv run ruff check .
```

Eine grafische Oberfläche kann solche Befehle teilweise verstecken oder vereinfachen. Die Kommandozeile zeigt dagegen direkt, **welcher Befehl tatsächlich ausgeführt wird**.

### 2. Befehle lassen sich exakt wiederholen

Eine Anweisung wie

> „Führe im Projektverzeichnis `uv run pytest` aus.“

ist eindeutig. Ein Ablauf wie

> „Klicke links auf das Symbol, öffne dort das Menü, wähle ...“

hängt dagegen stark von Betriebssystem, Editor und Programmversion ab.

### 3. Server und CI-Systeme arbeiten meist ohne grafische Oberfläche

Ein Cloud-Server oder ein CI-Runner besitzt häufig gar keinen Desktop. Dort werden dieselben Befehle ausgeführt, die wir lokal im Terminal verwenden.

Das ist für den Kurs ein wichtiger Zusammenhang:

```text
lokales Terminal  ->  dieselben Tools  ->  CI / Server
```

### 4. Kleine Abläufe können automatisiert werden

Mehrere Befehle können in einer Textdatei gespeichert und später gemeinsam ausgeführt werden. Solche **Shell-Skripte** werden uns im Kapitel noch begegnen.

---

# Terminal, Shell, Bash und CLI

Die Begriffe werden im Alltag häufig durcheinander verwendet. Für die praktische Arbeit reicht folgende Unterscheidung.

## Terminal

Das **Terminal** ist das Programm bzw. Fenster, in dem wir textbasierte Befehle eingeben und deren Ausgabe sehen.

Beispiele sind:

- Terminal unter macOS,
- verschiedene Terminal-Programme unter Linux,
- Windows Terminal,
- das integrierte Terminal in VS Code.

## Shell

Die **Shell** ist das Programm, das unsere eingegebenen Befehle interpretiert und ausführt.

Bekannte Shells sind beispielsweise:

- Bash,
- zsh,
- PowerShell.

## Bash

**Bash** steht für *Bourne Again Shell* und ist eine sehr verbreitete Unix-Shell. Viele Beispiele in Softwareentwicklung, Linux, Serverbetrieb und CI verwenden Bash oder eine sehr ähnliche Syntax.

Unsere Beispiele in diesem Kurs sind deshalb überwiegend **Bash-artig**.

## CLI

**CLI** steht für *Command Line Interface*. Gemeint ist die textbasierte Bedienoberfläche eines Programms.

Beispiele:

```bash
git status
python --version
uv run pytest
```

Git, Python und `uv` sind dabei jeweils eigene Programme. Die Shell startet diese Programme und übergibt ihnen die nachfolgenden Argumente.

---

# Welche Shell verwenden wir?

## Linux

Unter Linux ist eine Unix-Shell immer vorhanden; Bash ist sehr verbreitet. Ein Terminal kann direkt geöffnet und verwendet werden.

## macOS

macOS besitzt ebenfalls eine Unix-artige Kommandozeilenumgebung. Auf aktuellen macOS-Systemen ist standardmäßig häufig **zsh** statt Bash konfiguriert. Für die grundlegenden Befehle dieses Kapitels macht das praktisch keinen Unterschied.

## Windows

Unter Windows gibt es mehrere sinnvolle Möglichkeiten:

- **PowerShell / Windows Terminal** für native Windows-Arbeit,
- **Git Bash** für einen schnellen Bash-artigen Einstieg,
- **WSL (Windows Subsystem for Linux)** für eine vollständige Linux-Umgebung unter Windows.

Für diesen Kurs ist **Git Bash** oft der unkomplizierteste gemeinsame Einstieg, wenn ohnehin Git installiert wird. WSL ist besonders interessant, wenn später stärker mit Linux-Werkzeugen oder Serverumgebungen gearbeitet wird.

> **Wichtig:** PowerShell ist eine andere Shell und besitzt teilweise andere Befehle oder Optionen. Viele einfache Kommandos sehen ähnlich aus, aber Bash-Beispiele sollten nicht blind als PowerShell-Syntax interpretiert werden.

---

# Die Anatomie eines Befehls

Ein typischer Kommandozeilenbefehl besteht aus drei Teilen:

```text
programm   option(en)   argument(e)
```

Zum Beispiel:

```bash
ls -l data
```

- `ls` ist das Programm bzw. der Befehl,
- `-l` ist eine Option,
- `data` ist ein Argument, hier ein Verzeichnisname.

Ein anderes Beispiel:

```bash
cp report.txt archive/report.txt
```

Hier erhält `cp` zwei Argumente:

1. die Quelldatei,
2. das Ziel.

Viele Programme erklären ihre Optionen selbst:

```bash
ls --help
git --help
uv --help
```

Auf Linux/macOS steht zusätzlich häufig das Manual-System zur Verfügung:

```bash
man ls
```

Niemand muss alle Optionen auswendig kennen. Wichtig ist, die **häufigen Grundbefehle** zu kennen und bei Bedarf gezielt nachschlagen zu können.

---

# Das Dateisystem und das aktuelle Arbeitsverzeichnis

Die Shell arbeitet immer in einem bestimmten **aktuellen Arbeitsverzeichnis** (*current working directory*).

Genau wie ein Dateimanager zeigt sie also nicht „den ganzen Computer gleichzeitig“, sondern wir befinden uns an einer bestimmten Position im Dateisystem.

## `pwd`: Wo bin ich?

```bash
pwd
```

`pwd` steht für **print working directory**.

Eine mögliche Ausgabe unter Linux/macOS wäre:

```text
/home/alice/projects
```

oder beispielsweise in Git Bash unter Windows:

```text
/c/Users/Alice/projects
```

> Wenn ihr unsicher seid, **wo** ein Befehl gerade wirkt, ist `pwd` fast immer ein guter erster Schritt.

---

# `ls`: Was ist hier?

```bash
ls
```

`ls` zeigt den Inhalt eines Verzeichnisses an.

Besonders nützliche Varianten sind:

```bash
ls -l
ls -a
ls -la
ls -lh
```

- `-l`: ausführlichere Darstellung (*long listing*),
- `-a`: auch versteckte Einträge anzeigen,
- `-h`: Dateigrößen besser lesbar darstellen; sinnvoll zusammen mit `-l`.

Unter Unix-artigen Systemen beginnen versteckte Dateien und Ordner typischerweise mit einem Punkt, beispielsweise:

```text
.git
.gitignore
.venv
```

Darum wird uns `ls -a` später bei Git besonders nützlich sein.

Ein anderes Verzeichnis kann auch direkt angegeben werden:

```bash
ls data
ls data/raw
```

---

# `cd`: Verzeichnisse wechseln

Mit `cd` (*change directory*) wechseln wir das aktuelle Arbeitsverzeichnis.

```bash
cd projects
```

Eine Ebene nach oben:

```bash
cd ..
```

Ins Home-Verzeichnis:

```bash
cd ~
```

Zur Kontrolle:

```bash
pwd
ls
```

## Relative und absolute Pfade

Ein **relativer Pfad** wird ausgehend vom aktuellen Verzeichnis interpretiert:

```bash
cd data/raw
```

Ein **absoluter Pfad** beschreibt eine vollständige Position im Dateisystem:

```bash
cd /home/alice/projects/demo
```

Unter Windows sehen absolute Pfade außerhalb einer Unix-artigen Shell anders aus, zum Beispiel:

```text
C:\Users\Alice\projects\demo
```

Für unsere Arbeit ist vor allem wichtig zu verstehen:

> Ein relativer Pfad hängt davon ab, **wo ihr gerade seid**.

## `.` und `..`

Zwei besondere Pfadangaben werden ständig verwendet:

- `.` bedeutet: **aktuelles Verzeichnis**,
- `..` bedeutet: **übergeordnetes Verzeichnis**.

Darum bedeutet etwa

```bash
cd ..
```

„gehe eine Ebene nach oben“.

---

# Namen, Leerzeichen und Quotes

Shells trennen Argumente normalerweise an Leerzeichen.

Der Befehl

```bash
mkdir my project
```

legt deshalb **zwei** Verzeichnisse an:

```text
my/
project/
```

Soll wirklich ein Verzeichnis mit Leerzeichen im Namen erstellt werden, muss der Name geschützt werden:

```bash
mkdir "my project"
cd "my project"
```

Für Softwareprojekte sind einfache Namen ohne Leerzeichen meist angenehmer, beispielsweise:

```text
my-project
shell-demo
first_git_project
```

---

# Verzeichnisse anlegen: `mkdir`

Ein neues Verzeichnis wird mit `mkdir` erstellt:

```bash
mkdir course-demo
```

Danach:

```bash
ls
cd course-demo
pwd
```

Mehrere verschachtelte Verzeichnisse lassen sich mit `-p` bequem anlegen:

```bash
mkdir -p data/raw
mkdir -p data/processed
```

Oder gleichzeitig:

```bash
mkdir -p data/raw data/processed
```

---

# Dateien anlegen: `touch`

Eine leere Datei kann mit `touch` angelegt werden:

```bash
touch notes.txt
```

Mehrere Dateien:

```bash
touch measurement_1.csv measurement_2.csv measurement_3.csv
```

`touch` hat technisch noch eine zweite Aufgabe: Existiert die Datei bereits, wird ihr Änderungszeitpunkt aktualisiert. Für unseren Einstieg ist aber vor allem das schnelle Erzeugen leerer Dateien nützlich.

---

# Text ausgeben: `echo`

Mit `echo` können wir Text im Terminal ausgeben:

```bash
echo "Hello world"
```

Das wirkt zunächst unspektakulär, wird in Skripten aber sehr häufig verwendet.

Beispiel:

```bash
echo "Starting analysis..."
python analysis.py
echo "Finished."
```

## Ausgabe in eine Datei schreiben

Für kleine Beispiele ist eine einfache Ausgabeumleitung praktisch:

```bash
echo "42" > result.txt
```

`>` schreibt die Ausgabe in die Datei. Existiert sie bereits, wird ihr bisheriger Inhalt ersetzt.

Mit `>>` wird stattdessen angehängt:

```bash
echo "17" >> result.txt
```

Danach enthält die Datei zwei Zeilen.

> Umleitungen sind nützlich, aber kein Schwerpunkt der ersten Session. Das wichtigere Konzept ist zunächst: **Programme können über die Shell gestartet werden und Text ein- bzw. ausgeben.**

---

# Dateien anzeigen: `cat`

Mit `cat` können wir kleine Textdateien direkt im Terminal anzeigen:

```bash
cat result.txt
```

Beispiel:

```text
42
17
```

Der Name kommt historisch von *concatenate*: `cat` kann mehrere Dateien hintereinander ausgeben. Für uns ist zunächst das einfache Anzeigen entscheidend.

Für sehr große Dateien ist `cat` oft unpraktisch. Später können dafür beispielsweise `head`, `tail` oder spezialisierte Werkzeuge sinnvoll sein.

---

# Dateien kopieren: `cp`

Eine Datei kopieren:

```bash
cp original.txt copy.txt
```

In ein anderes Verzeichnis kopieren:

```bash
cp report.txt archive/
```

Mit neuem Namen in ein anderes Verzeichnis:

```bash
cp report.txt archive/report_backup.txt
```

Für ganze Verzeichnisse wird üblicherweise die rekursive Option benötigt:

```bash
cp -r source_directory backup_directory
```

Für die erste Session konzentrieren wir uns hauptsächlich auf Dateien.

---

# Verschieben und Umbenennen: `mv`

`mv` steht für **move**. Derselbe Befehl wird sowohl zum Verschieben als auch zum Umbenennen verwendet.

## Umbenennen

```bash
mv statiscs.txt statistics.txt
```

## Verschieben

```bash
mv statistics.txt data/
```

Oder gleichzeitig verschieben und umbenennen:

```bash
mv statistics.txt data/statistics_2026.txt
```

Dieses Verhalten ist wichtig zu verstehen: In einem Dateisystem ist „Umbenennen“ im Wesentlichen eine Form des Verschiebens.

---

# Löschen: `rm`

Eine Datei löschen:

```bash
rm old_notes.txt
```

> **Achtung:** `rm` verschiebt eine Datei in der Regel **nicht in den Papierkorb**. Das Löschen kann unmittelbar und endgültig sein.

Vor einem Löschbefehl lohnt sich daher besonders bei längeren Pfaden:

```bash
pwd
ls
```

Erst danach:

```bash
rm old_notes.txt
```

## Verzeichnisse löschen

Ein nicht-leeres Verzeichnis muss rekursiv gelöscht werden:

```bash
rm -r old_directory
```

Die häufig im Internet sichtbare Kombination

```bash
rm -rf ...
```

ist besonders gefährlich:

- `-r` löscht rekursiv ganze Verzeichnisbäume,
- `-f` unterdrückt viele Rückfragen bzw. Fehlerhinweise.

> **Sicherheitsregel:** `rm -rf` niemals blind aus einer Anleitung, einem Forum oder einer KI-Antwort übernehmen. Vorher Pfad und aktuelles Arbeitsverzeichnis prüfen und verstehen, was gelöscht wird.

Eine vorsichtigere Variante für einzelne Dateien ist beispielsweise:

```bash
rm -i old_notes.txt
```

Dabei fragt `rm` vor dem Löschen nach.

---

# Platzhalter: `*`

Ein kleines Shell-Konzept ist in der Praxis so häufig, dass wir es zumindest kennen sollten: **Wildcards**.

```bash
ls *.csv
```

`*` steht hier für eine beliebige Zeichenfolge. Angezeigt werden also alle passenden `.csv`-Dateien im aktuellen Verzeichnis.

Beispiel:

```bash
cp data/*.csv archive/
```

Die Shell erweitert `data/*.csv` zunächst zu den passenden Dateinamen und übergibt diese anschließend an `cp`.

> Wildcards sind nützlich, aber vor Befehlen wie `rm` sollte man besonders sorgfältig prüfen, welche Dateien tatsächlich getroffen werden.

---

# Die wichtigste Verbindung zum weiteren Kurs: Programme starten

Bis hierhin haben wir vor allem Dateien und Verzeichnisse verwaltet. Der eigentliche Mehrwert der Shell entsteht aber dadurch, dass wir **andere Programme** starten können.

## Python starten

Version anzeigen:

```bash
python --version
```

Je nach System kann der Befehl auch `python3` heißen:

```bash
python3 --version
```

Ein Python-Skript ausführen:

```bash
python analysis.py
```

Ein Python-Modul ausführen:

```bash
python -m my_package
```

## Python mit `uv`

In unseren Python-Projekten wird häufig `uv` verwendet. Dadurch können Befehle in der zum Projekt gehörenden Python-Umgebung ausgeführt werden.

```bash
uv --version
uv run python --version
uv run python analysis.py
```

Für ein Skript ist auch die kürzere Form möglich:

```bash
uv run analysis.py
```

In einem `uv`-Projekt stellt `uv run` sicher, dass der Befehl in der passenden Projektumgebung läuft.

## Entwicklungswerkzeuge starten

Später werden beispielsweise folgende Befehle wichtig:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

Und natürlich Git:

```bash
git status
```

Damit wird die Shell zur gemeinsamen Schnittstelle zwischen unseren Werkzeugen.

---

# Shell-Skripte

Wenn wir dieselben Befehle wiederholt ausführen, können wir sie in einer Textdatei speichern.

Eine einfache Datei `hello.sh` könnte so aussehen:

```bash
#!/usr/bin/env bash

echo "Hello from the shell!"
echo "Current directory:"
pwd
```

Ausführen:

```bash
bash hello.sh
```

Die erste Zeile

```bash
#!/usr/bin/env bash
```

wird **Shebang** genannt. Sie beschreibt, welcher Interpreter für das Skript vorgesehen ist.

Wenn ein Skript explizit mit

```bash
bash hello.sh
```

gestartet wird, ist die Shebang technisch nicht notwendig. Sie ist trotzdem eine hilfreiche und übliche Dokumentation.

## Andere Programme aus einem Skript starten

Ein Shell-Skript kann alles aufrufen, was wir auch direkt im Terminal aufrufen könnten.

Beispiel `run_analysis.sh`:

```bash
#!/usr/bin/env bash

echo "Running analysis..."
uv run python analysis.py
echo "Done."
```

Ausführen:

```bash
bash run_analysis.sh
```

Genau dieses Prinzip wird später auch bei Build-, Test- oder CI-Abläufen wichtig.

---

# Argumente an Shell-Skripte übergeben

Shell-Skripte können Werte beim Aufruf entgegennehmen.

`show_argument.sh`:

```bash
#!/usr/bin/env bash

echo "First argument: $1"
```

Aufruf:

```bash
bash show_argument.sh hello
```

Ausgabe:

```text
First argument: hello
```

- `$1` ist das erste Argument,
- `$2` das zweite,
- `$3` das dritte usw.

Ein zweites kleines Beispiel:

```bash
#!/usr/bin/env bash

echo "$1 $2"
```

Aufruf:

```bash
bash two_words.sh hello world
```

---

# Bash ist eine Programmiersprache – aber wie viel brauchen wir davon?

Bash unterstützt Variablen, Schleifen, Bedingungen, Funktionen und vieles mehr.

Zum Beispiel:

```bash
for item in one two three; do
    echo "$item"
done
```

Oder:

```bash
if [ -f pyproject.toml ]; then
    echo "Python project found"
else
    echo "No pyproject.toml found"
fi
```

Das ist nützlich zu wissen. Für diesen Kurs ist aber wichtiger, **Bash als Steuerzentrale für Dateien und Entwicklungswerkzeuge** zu verstehen als umfangreiche Programme in Bash zu schreiben.

Für komplexe Logik ist Python häufig die angenehmere Wahl.

## Faustregel: Shell oder Python?

**Shell eignet sich besonders gut für:**

- Programme starten,
- Dateien und Ordner organisieren,
- wenige Befehle zu einem Ablauf kombinieren,
- einfache Automatisierung,
- CI- und Server-Kommandos.

**Python eignet sich meistens besser für:**

- komplexe Datenstrukturen,
- umfangreiche Berechnungslogik,
- größere Programme,
- detaillierte Fehlerbehandlung,
- gut testbare Anwendungslogik.

In realen Projekten werden beide häufig kombiniert.

---

# Kleine Übung

Erstellt nur mit der Shell folgende Struktur:

```text
shell-practice/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
└── README.txt
```

Möglicher Start:

```bash
mkdir shell-practice
cd shell-practice
mkdir -p data/raw data/processed scripts
touch README.txt
```

Danach:

1. Legt in `data/raw/` drei leere Dateien mit der Endung `.csv` an.
2. Schreibt mit `echo` eine kurze Zeile in `README.txt`.
3. Zeigt den Inhalt mit `cat` an.
4. Kopiert eine der CSV-Dateien nach `data/processed/`.
5. Benennt die Kopie dort um.
6. Prüft mit `pwd` und `ls`, wo ihr seid und welche Dateien vorhanden sind.
7. Löscht nur die umbenannte Kopie wieder.
8. Erstellt ein kleines Python-Skript und führt es aus dem Terminal aus.

---

# Häufige Fehler und wie man sie diagnostiziert

## „No such file or directory“

Meistens stimmt der Pfad nicht oder ihr befindet euch im falschen Verzeichnis.

Prüfen:

```bash
pwd
ls
```

## Ein Befehl wird nicht gefunden

Beispiel:

```text
command not found: uv
```

Dann ist das Programm entweder nicht installiert oder nicht über den `PATH` auffindbar.

Prüfen könnt ihr beispielsweise:

```bash
python --version
git --version
uv --version
```

## Dateiname enthält Leerzeichen

Dann Quotes verwenden:

```bash
cat "my notes.txt"
```

## Falsche Datei gelöscht

Bei `rm` gibt es oft keinen einfachen Undo-Schritt. Deshalb:

1. erst `pwd`,
2. dann `ls`,
3. Pfad lesen,
4. erst dann löschen.

## Ein Shell-Beispiel aus dem Internet funktioniert unter PowerShell nicht

Bash und PowerShell sind unterschiedliche Shells. Prüft zuerst, **welche Shell** ihr gerade verwendet.

---

# Cheat Sheet: Shell-Kommandos für den Kurs

Dieses Cheat Sheet ist bewusst etwas umfangreicher als das Minimum der ersten Session. Es soll später bei Übungen und Praktika als schnelle Referenz dienen.

## Orientierung und Navigation

| Aufgabe | Befehl | Beispiel / Hinweis |
|---|---|---|
| Aktuelles Verzeichnis anzeigen | `pwd` | `pwd` |
| Inhalt anzeigen | `ls` | `ls` |
| Ausführliche Liste | `ls -l` | Rechte, Größe, Datum etc. |
| Versteckte Dateien anzeigen | `ls -a` | zeigt z. B. `.git` |
| Ausführlich + versteckt | `ls -la` | sehr häufig nützlich |
| Lesbare Größen | `ls -lh` | z. B. KiB/MiB statt nur Bytes |
| In Verzeichnis wechseln | `cd <pfad>` | `cd data` |
| Eine Ebene hoch | `cd ..` | zum Elternverzeichnis |
| Ins Home-Verzeichnis | `cd ~` | Unix-artige Shells |
| Aktuelles Verzeichnis als Pfad | `.` | z. B. `ruff check .` |
| Elternverzeichnis als Pfad | `..` | z. B. `ls ..` |

## Dateien und Verzeichnisse

| Aufgabe | Befehl | Beispiel / Hinweis |
|---|---|---|
| Verzeichnis erstellen | `mkdir <name>` | `mkdir results` |
| Verschachtelte Verzeichnisse erstellen | `mkdir -p <pfad>` | `mkdir -p data/raw` |
| Leere Datei anlegen | `touch <datei>` | `touch notes.txt` |
| Text ausgeben | `echo <text>` | `echo "hello"` |
| Datei anzeigen | `cat <datei>` | `cat README.md` |
| Datei kopieren | `cp <quelle> <ziel>` | `cp a.txt b.txt` |
| Datei in Ordner kopieren | `cp <datei> <ordner>/` | `cp a.csv data/` |
| Verzeichnis rekursiv kopieren | `cp -r <quelle> <ziel>` | bei ganzen Ordnern |
| Verschieben | `mv <quelle> <ziel>` | `mv a.txt archive/` |
| Umbenennen | `mv <alt> <neu>` | `mv old.txt new.txt` |
| Datei löschen | `rm <datei>` | **kein Papierkorb** |
| Interaktiv löschen | `rm -i <datei>` | fragt vor dem Löschen |
| Verzeichnis rekursiv löschen | `rm -r <ordner>` | mit großer Vorsicht |

## Pfade und Namen

| Ausdruck | Bedeutung |
|---|---|
| `.` | aktuelles Verzeichnis |
| `..` | übergeordnetes Verzeichnis |
| `~` | Home-Verzeichnis in Unix-artigen Shells |
| `data/raw/file.csv` | relativer Pfad |
| `/home/alice/project` | absoluter Unix-Pfad |
| `"my file.txt"` | Quotes schützen Leerzeichen |
| `*.csv` | alle passenden `.csv`-Dateien im aktuellen Kontext |

## Einfache Ein-/Ausgabe

| Aufgabe | Befehl | Hinweis |
|---|---|---|
| Text anzeigen | `echo "text"` | Ausgabe ins Terminal |
| Datei anzeigen | `cat file.txt` | für kleinere Textdateien |
| Ausgabe in Datei schreiben | `command > file.txt` | überschreibt Datei |
| Ausgabe an Datei anhängen | `command >> file.txt` | hängt an |

## Hilfe

| Aufgabe | Befehl |
|---|---|
| Kurzhilfe eines Programms | `<command> --help` |
| Unix-Manual öffnen | `man <command>` |
| Git-Hilfe | `git help <command>` |
| uv-Hilfe | `uv <command> --help` |

## Python und Entwicklungswerkzeuge

| Aufgabe | Befehl | Hinweis |
|---|---|---|
| Python-Version | `python --version` | manchmal `python3` |
| Python-Skript starten | `python script.py` | System-/aktive Umgebung |
| Python-Modul starten | `python -m package` | Modul als Programm |
| uv-Version | `uv --version` | prüft Installation |
| Python über uv | `uv run python --version` | Projektumgebung |
| Skript über uv | `uv run script.py` | kurze Form |
| Skript explizit über Python/uv | `uv run python script.py` | ebenfalls gut lesbar |
| Tests starten | `uv run pytest` | später im Kurs |
| Ruff-Linter starten | `uv run ruff check .` | später im Kurs |
| Ruff-Format prüfen | `uv run ruff format --check .` | später im Kurs |
| Git-Status | `git status` | nächstes Kapitel |

## Shell-Skripte

| Aufgabe | Befehl / Syntax |
|---|---|
| Bash-Skript starten | `bash script.sh` |
| Erstes Argument im Skript | `$1` |
| Zweites Argument | `$2` |
| Alle Argumente | `$@` |
| Shebang | `#!/usr/bin/env bash` |
| Text ausgeben | `echo "..."` |

## Sicherheits-Check vor Dateioperationen

Vor allem vor einem Löschbefehl:

```bash
pwd
ls
```

Dann den Pfad noch einmal lesen und erst anschließend beispielsweise:

```bash
rm unwanted_file.txt
```

> **Merksatz:** Geschwindigkeit im Terminal entsteht nicht dadurch, Befehle blind schnell einzutippen, sondern dadurch, dass ihr genau wisst, **wo** ihr seid und **was** ein Befehl verändern wird.

---

# Weiterführende Quellen

- GNU Coreutils Manual: <https://www.gnu.org/software/coreutils/manual/>
- GNU Bash Manual: <https://www.gnu.org/software/bash/manual/>
- Python-Dokumentation: <https://docs.python.org/>
- uv-Dokumentation: <https://docs.astral.sh/uv/>
- Git-Dokumentation: <https://git-scm.com/docs>
- Microsoft WSL-Dokumentation: <https://learn.microsoft.com/windows/wsl/>

Für einen schnellen, einsteigerfreundlichen Überblick zu einzelnen Bash-Befehlen kann zusätzlich die von euch bereits verwendete W3Schools-Übersicht hilfreich sein: <https://www.w3schools.com/bash/bash_commands.php>
