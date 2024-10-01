# Shell Scripting

## Zurück in die Zukunft... Shell scripting!

Viele von uns sind es gewohnt, Computer vor allem über grafische Benutzeroberflächen zu bedienen. Das Öffnen eines Terminals kann wie eine Reise in die Vergangenheit erscheinen. Doch im Bereich Data Science und KI gibt es triftige Gründe, sich mit der Kommandozeile vertraut zu machen. 

Aber starten wir einfach mit einer Frage:  
**Welche Programmiersprachen nutzen Hacker?** 

Hier geht's zu Auflösung:
```{toggle}
  Das ist eine häufig gestellte Frage, wenn es um das Image der "Hacker" geht. Eine Untersuchung aus dem Jahr 2022 {cite}`koch2022programming` fand, dass 72,5% der Hacker hier zuerst "Bash, Shell, PowerShell" angaben, gefolgt von Python mit 70%. Danach kommt lange nichts – alle anderen Sprachen liegen um die 30% und darunter.
```

Ok, jetzt geht es aber hier im Kurs nicht darum Hacker auszubilden (sorry!), sondern wir bewegen uns im Bereich Data Science. Unter Data Scientists wäre Python sicher auf dem ersten Platz gelandet, aber zumindest grundlegende Skills im Bereich Bash/Shell sind trotzdem unerlässlich. Leicht gesagt, aber warum eigentlich?

Um Verwirrungen zu vermeiden starten wir aber mit ein paar Begriffen:

## Einführung der Begriffe: Bash, CLI, Shell
Die gängigen Betriebssysteme setzten heute alle auf grafische Benutzeroberflächen, egal ob am Rechner, Tablet, oder Smartphone.
In den 1970er Jahren war daran noch gar nicht zu denken, schon angesichts der im Rückblick bescheidenen Rechenkapazitäten. Bei Betriebssystemen war es daher lange völlig normal das Nutzer*innen ausschließlich über Eingaben in Textform mit dem Rechner interagierten, über ein sogenanntes  **CLI (Command Line Interface)**, eine textbasierte Benutzeroberfläche zur Interaktion mit dem Betriebssystem.

Mit **Shell** (engl. für Schale oder Hülle) meint man im allgemeinen genau solch ein Programm das Befehle (in Textform) interpretiert und ausführt. Damit macht die Shell die Fähigkeiten eines Betriebssystems den Nutzer*innen, aber auch anderen Programmen zugänglich. Dabei ist **Bash**, die "Bourne Again Shell" (bezieht sich auf eine frühere Shell von Stephen Bourne) die am weitesten verbreitete Shell in Linux-Umgebungen.

Die Begriffe **Console** und **Terminal** bezogen sich ursprünglich auf physische Hardware also Monitor und Keyboard über die die Texteingaben erfolgten (also über ein Shell-Programm). Diese beiden Begriffe Console und Terminal wurden aber schon lange übertragen auf Software-Umsetzungen und werden heute im Alltag oft synonym verwendet.

OK, das macht geschichtlich alles Sinn, aber warum sollten wir heute noch über eine textbasierte Shell arbeiten?
Schließlich verfügen auch Linux-Systeme, wie z.B. Ubuntu, heute über sehr zugängliche grafische Oberflächen.
Diese grafischen Oberflächen sind aber für "End-Nutzer*innen" konzipiert. Und wir werden sehen, dass sehr viele Prozesse besser oder sogar ausschließlich über ein Shell möglich sind!

Wir starten mit der Frage: **Nutzt ihr selber Linux? Und wenn ja, wofür nutzt ihr es?
```{toggle}
Was auch immer hier die Antwort war. Sollte sie "Nein" gewesen sein, war sie ziemlich sicher nicht korrekt :)

Linux ist nämlich überall in der digitalen Welt zu finden!

**Linux**
  - 1991 wurde das Betriebssystem Linux von Linus Torvalds entwickelt (davor hab es seit den 1970er das Betriebssysten UNIX).
  - Das Projekt war schnell (für Linus Torvalds wiedererwartend) erfolgreich
  - Heute ist Linux allgegenwärtig, besonders in Bereichen wie Servern, Cloud Computing und Supercomputern.
  - Linux bildet die Basis für Betriebssysteme wie Android und Chrome OS und wird von riesigen IT-Infrastrukturen verwendet, inklusive Google und Facebook.
  - Selbst Microsoft betreibt die meisten seiner Server mit Linux!
```

**Warum ist Linux so beliebt?**
  - **Open Source!**: Jeder kann den Quellcode einsehen und verändern.
  - **Kostenlos**: Linux kostet nichts, damit kann es auch auf belieb vielen Rechnern ohne Lizenzgebühren installiert werden
  - **Sicherheit**: Linux gilt als recht sicher, da dank der globalen Community Sicherheitslücken oft schnell entdeckt und behoben werden.
  - **Performance**: Im Vergleich zu Windows ist Linux oft ressourcenschonender, da es nicht auf eine umfassende Benutzererfahrung optimiert ist, sondern eher schlank und effizient läuft.


## Warum ist Shell Scripting unverzichtbar?

Das Erlernen der Grundlagen von Linux und Shell Scripting ist für Data Scientists unerlässlich, weil viele Aufgaben nur auf diesem Weg effizient gelöst werden können:

- **Automatisierung**: Viele wichtige Prozesse in der Software-Entwicklung, im Bereich Web-Apps und bei der Nutzung von Servern lassen sich mit der Kommandozeile besser automatisieren als mit grafischen Tools.
- **Nutzung größerer Hardware**: Server, Großrechner und Cloud-Infrastrukturen werden oft über Shell-Skripte gesteuert.
- **Macht der CLI**: Viele leistungsstarke Tools und Bibliotheken für Data Science sind direkt über die Kommandozeile zugänglich, z.B. Hadoop, Spark und Docker.


## Installation und Einrichtung

**Für den schnellen Einstieg: Git Bash**

Eine einfachere Möglichkeit, Bash unter Windows zu nutzen, ist **Git Bash**:

1. Lade [Git für Windows](https://gitforwindows.org/) herunter und installiere es.
2. Git Bash wird zusammen mit Git installiert und bietet eine Bash-ähnliche Umgebung.

**Für Fortgeschrittene: Bash unter Windows (via WSL)**

Um Bash unter Windows zu nutzen, kannst du das **Windows Subsystem for Linux (WSL)** installieren. Die entsprechenden Schritte findet man in zahlreichen online-Tutorials, z.B. [hier](https://www.howtogeek.com/744328/how-to-install-the-windows-subsystem-for-linux-on-windows-11/) oder [hier](https://learn.microsoft.com/en-us/windows/wsl/install).

**MacOS: Bash ist vorinstalliert**

Wenn du MacOS nutzt, hast du Glück – Bash ist bereits vorinstalliert. Du kannst einfach das Terminal öffnen und loslegen.



### Navigieren im Dateisystem:

Wir starten langsam und schauen uns erst einmal die Standard-Befehle an um Ordner zu wechseln und deren Inhalt zu sehen:

- `pwd` gibt den aktuellen Ordner an in dem wir uns befinden. Unter Linux sieht das typischerweise aus wie `/homer/itsme`, bei Windows eher wie `C:\Users\itsme`.
- `ls`(für list/listing) zeigt den Inhalt des aktuellen Verzeichnisses auf.
- mit `cd foldername` gehe ich in einen Ordner namens "foldername", mit `cd ..` gehe ich wieder einen Ordner tiefer zurück
- mit `--help` können Hinweise zu den möglichen Parametern abgefragt werden, z.B. `ls --help`.


Befehle sind immer wie folgt aufgebaut:

![Shell command structure](../images/shell_command_syntax.svg)

(Illustration taken from Data Carpentry course)

Anders als andere Programmiersprachen ist **bash** ein CLI (Command-Line Interface) und funktioniert immer im Kontext des aktuellen Verzeichnisses.

| Befehl                        | Funktion                                                     |
| ----------------------------- | ------------------------------------------------------------ |
| `ls`                          | Lists the files and subdirectories contained in the current directory |
| `ls -l`                       | Lists every file and directory on a separate line            |
| `ls -t`                       | Sorts the directory contents by last-modified date (descending) |
| `ls -R`                       | Recursively `ls` this directory and all of its subdirectories |
| `pwd`                         | `pwd` stands for "print working directory"                   |
| `echo`                        | prints something out                                         |
| `echo "I'm in $(pwd)"`        |                                                              |
| `echo "I'm in $PWD"`          |                                                              |
| `clear`                       | clears your screen                                           |
| `cd`                          | stands for "change directory"                                |
| `cd ~`                        | change to home directory                                     |
| `cd ..`                       | go up one directory                                          |
| `cd /home/username/Documents` | change to specific directory                                 |
| `cd -`                        | change to last directory                                     |
|                               |                                                              |


Das gute an Bash-Befehlen: Man muss sie nicht auswendig lernen! Bei Unsicherheiten können Befehle einfach nachgeschlagen werden. Für einen schnellen Überblick gibt es z.B. [hier](https://www.educative.io/blog/bash-shell-command-cheat-sheet) eine Übersicht.

```{warning}
**Achtung!** Shell/Bash ist nicht umsonst ein beliebtes Hacker Tool.

- Mit Bash können Datei-Rechte eingesehen und geändert werden.
- Mit Bash können Dateien, Verzeichnisse, Festplatten gelöscht werden.
- Und: es gibt keinen Papierkorb!
```

### Nächster Schritt: Dateien & Verzeichnisse erstellen und löschen

Mit **bash** können wir Dateien und Verzeichnisse einfach erstellen, anzeigen, umbenennen, kopieren, verschieben oder löschen. Diese Operationen sind nützlich für das Arbeiten mit Dateien auf der Kommandozeile.

| Befehl           | Funktion                                                     |
| ---------------- | ------------------------------------------------------------ |
| `mkdir new_dir`  | Erstellt ein neues Verzeichnis namens "new_dir"              |
| `rm -r new_dir/` | Löscht das Verzeichnis "new_dir" und seinen Inhalt rekursiv (Achtung: unwiderruflich!) |
| `ls -t`          | Sortiert die Verzeichnisinhalte nach Änderungsdatum (absteigend) |
| `ls -R`          | Listet die Inhalte eines Verzeichnisses rekursiv auf         |



```{warning}
**Achtung!**
`rm new_dir/` Vorsicht! Dieser Befehl löscht Dateien/Verzeichnisse unwiderruflich! 
```

#### Dateien und Verzeichnisse erstellen
**Verzeichnisse erstellen:**

Mit dem Befehl mkdir lassen sich Verzeichnisse schnell erstellen. Beispiel:
```bash
# Erstelle ein neues Verzeichnis
mkdir new_dir

# Überprüfen, ob das Verzeichnis erstellt wurde:
ls
```
Mehrere Verzeichnisse auf einmal erstellen:
```bash
mkdir -p secrets/data

# Mit Unterverzeichnissen anzeigen
ls -R
```
Hinweis: Das ist das Gleiche, als ob du im Dateiexplorer ein Verzeichnis erstellst!

**Dateien erstellen:**

Um eine Datei zu erstellen, kann ein Texteditor wie nano verwenden werden:
```bash
cd secrets
nano my_diary.txt
```
Oder, alternativ kannst auch direkt eine leere Dateien ohne Editor erstellt werden mit `touch`:
```bash
touch data/facts1.csv
touch data/facts2.csv
touch data/facts3.csv
```

#### Dateien und Verzeichnisse umbenennen, verschieben und kopieren
Dateien oder Verzeichnisse können mit `mv`verschoben oder umbenannt werden.
```bash
cd data
# Umbenennen der Datei facts3.csv in facts0.csv
mv facts3.csv facts0.csv
```

Dateien können mit dem Befehl `cp` kopiert werden:
```bash
# Kopieren der Datei facts2.csv und Umbenennen der Kopie in facts3.csv
cp facts2.csv facts3.csv
```

**Versteckte Verzeichnisse:**

Verzeichnisse können durch Voranstellen eines Punktes „versteckt“ werden.
```bash
mv secrets/ .secrets/
ls
ls -a  # Zeigt auch versteckte Dateien und Verzeichnisse an
```

#### Übung:

Es wurde eine Datei statiscs.txt erstellt (z.B. mit `touch statiscs.txt`), sie sollte jedoch statistics.txt heißen. Mit welchem der folgenden Befehle kann sie umbenannt werden?
```bash
cp statiscs.txt statistics.txt
mv statiscs.txt statistics.txt
mv statiscs.txt .
cp statiscs.txt .
```

**Gute Namenskonventionen:**

Es wird empfohlen, keine Punkte oder Leerzeichen in Dateinamen zu verwenden, um Komplikationen zu vermeiden.

Beispiel:
```bash
mkdir one long name
ls
```
Was passiert hier (und warum)?

Leerzeichen in Dateinamen sollten vermieden werden. Um sie wieder zu löschen kann `rm -r one\ long\ name` genutzt werden.

#### Dateien und Verzeichnisse löschen:

Das Löschen eines Verzeichnisses mit `rm new_dir/ ist nicht ausreichend. Es muss rekursiv gelöscht werden:`
```bash
rm -r new_dir/
```

Dateien können mit dem Befehl `rm` direkt gelöscht werden:
```bash
rm facts0.csv
```

```{warning}
**Hinweis:** Gelöschte Dateien werden nicht in den Papierkorb verschoben, sondern dauerhaft entfernt.
```
Zum sichereren Löschen kann `rm` mit der Option `-i` (interaktiv) verwendet werden:
```bash
rm -i facts3.csv
```


### Bash-Skripte

Für komplexere Aufgaben wird die Kommandozeile alleine sehr schnell zu umständlich, daher wechseln wir hier zu Shell oder Bash Skripten. Das sind einfach Textdateien (typischerweise mit `.sh` Endung) in denen wir beliebig umfangreiche Bash-Programme entwerden können. Die Skripte lassen sich aus der Kommanozeile aufrufen mit:

```bash my_script.sh```

In Form dieser Skripte lassen sich auch die Vielzahl der Möglichkeiten die Bash bietet besser nutzen. Zum Beispiel **Loops**, diese sehen in Bash folgendermaßen aus:

```
for variable in 1 2 3
do
    echo $variable
done
```

Eine klassische for-Schleife lässt sich erstellen über:

```
for ((a=1; a <= $2; a++))
do
    echo $a
done
```

Eine weitere wichtige Struktur sind Verzweigungen. Auch in Bash gibt es if-else:

```
if [ Bedingung ]; then
   Befehle, die ausgeführt werden, wenn die Bedingung wahr ist
else
   Befehle, die ausgeführt werden, wenn die Bedingung falsch ist
fi
```


#### Argumente in der Kommandozeilen übergeben

Innerhalb eines Bash-Skripts können wir auch Argumente nutzen. Hier bezeichnet `$1`, `$2` etc. das erste, zweite usw. Argument nach dem Skriptnamen. Z.B. folgendes Skript, `print_first.sh`:

```
echo $1
```

Kann jetzt über `bash print_first.sh "dies hier bitte ausgeben"` aufgerufen werden und gibt dann über `echo` das Argument (also "dies hier bitte ausgeben") aus.

`$@` kann genutzt werden um alle Argumente zu addressieren.



### Zum Schluss: Bash + Python!

Nicht umsonst ist im Hacking-Bereich Bash UND Python recht beliebt. Beides lässt sich nämlich auch sehr einfach kombinieren!

Über `python my_python_code.py` lassen sich von einem Bash-Skript aus Python-Skripte ausführen.

```
print("Das ist Python-Code!")
```

Speichern Sie den obigen Code in einer Datei namens `example_script.py`, machen Sie ihn ausführbar mit `chmod +x example_script.py` und führen Sie ihn aus mit `./example_script.py`.


## Unix shell/bash vs. Windows

Wir haben uns in der ersten Session mit der Unix Shell auseinandergesetzt. Mit "git bash" konnten wir dies sowohl unter Linux, wie auch MacOS oder Windows nutzen. Der Windows eigene Terminal (cmd.exe) hat aber andere historische Wurzeln (DOS) und hat darum auch andere Befehle. 

Hier eine kleine Auswahl der häufigstens Befehle die sich unterscheiden:

| Bash | Windows | Funktion                                                |
| ---- | ------- | ------------------------------------------------------- |
| `ls` | `dir`   | Dateien und Verzeichnisse im aktuellen Ordner anzeigen. |
| `rm` | `del`   | Datei(en) löschen                                       |
| `mv` | `move`  | Dateien verschieben                                     |
| `cp` | `copy`  | Dateien kopieren                                        |




### Und noch vieles mehr.

Bash kann noch viel mehr, aber das werden wir (vorläufig) noch nicht benötigen. So können beispielsweise auch Funktionen definiert werden und vieles mehr.

Für weitere Übungen, Tipps und Beispiele zu Bash hier einige Links:

- https://www.learnshell.org/
- https://explainshell.com/
- https://wiki.ubuntuusers.de/Shell/Bash-Skripting-Guide_f%C3%BCr_Anf%C3%A4nger/
