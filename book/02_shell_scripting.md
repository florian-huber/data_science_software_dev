# Shell Scripting

## Zurück in die Zukunft... Shell scripting!

Viele von uns sind es gewohnt, Computer vor allem über grafische Benutzeroberflächen zu bedienen. Das Öffnen eines Terminals kann wie eine Reise in die Vergangenheit erscheinen. Doch im Bereich Data Science und KI gibt es triftige Gründe, sich mit der Kommandozeile vertraut zu machen. Hier lohnt sich ein (kleiner) Ausflug in die Geschichte:

**Unix**

Unix ist ein Betriebssystem, das in den 1970er Jahren bei AT&T Bell Labs entwickelt wurde. Es war die Basis für viele moderne Betriebssysteme und führte Konzepte wie das hierarchische Dateisystem und die Verwendung von einfachen Textdateien für die Systemkonfiguration ein.

**Linux**

Linux ist ein Unix-ähnliches Betriebssystem, das in den frühen 1990ern von Linus Torvalds entwickelt wurde. Es verwendet den Linux-Kernel und bietet eine breite Palette von Tools und Anwendungen für Entwickler.

**Shell**

Die Shell ist eine Benutzeroberfläche, die dem Benutzer den Zugriff auf die Funktionen eines Betriebssystems ermöglicht. Dabei werden Befehle in Textform eingegeben.

**Bash**

Bash (Bourne Again SHell) ist eine der bekanntesten Shells und wurde als Ersatz für die Bourne Shell entwickelt. Sie bietet viele Erweiterungen und Verbesserungen, die in anderen Shells nicht zu finden sind.


### Warum Shell Scripting lernen?

- **Welche Programmiersprachen nutzen Hacker?**
  - Eine häufig gestellte Frage, wenn es um das Image der "Hacker" geht. Eine Untersuchung von Koch et al. (2022) {cite}`koch2022programming` zeigt, dass 72,5% der Hacker Bash, Shell oder PowerShell nutzen, gefolgt von Python mit 70%. Danach kommt lange nichts – alle anderen Sprachen liegen um die 30% und darunter.
  
- **Linux und Data Science – Die unsichtbare Dominanz**
  - Kurze Geschichte von Linux:
    - 1991 wurde Linux von Linus Torvalds entwickelt.
    - Heute ist Linux allgegenwärtig, besonders in Bereichen wie Servern, Cloud Computing und Supercomputern.
    - Linux bildet die Basis für Betriebssysteme wie Android und Chrome OS und wird von riesigen IT-Infrastrukturen verwendet, inklusive Google und Facebook.
    - Selbst Microsoft betreibt die meisten seiner Server mit Linux!

- **Warum ist Linux so beliebt?**
  - **Open Source**: Jeder kann den Quellcode einsehen und verändern.
  - **Kostenlos**: Linux kostet nichts.
  - **Sicherheit**: Dank der globalen Community werden Sicherheitslücken schneller entdeckt und behoben.
  - **Performance**: Im Vergleich zu Windows ist Linux oft ressourcenschonender, da es nicht auf eine umfassende Benutzererfahrung optimiert ist, sondern schlank und effizient läuft.

---

## Warum ist Shell Scripting unverzichtbar?

Das Erlernen der Grundlagen von Linux und Shell Scripting ist für Data Scientists unerlässlich, weil viele Aufgaben nur auf diesem Weg effizient gelöst werden können:

- **Automatisierung**: Server, Großrechner und Cloud-Infrastrukturen werden oft über Shell-Skripte gesteuert.
- **Effizienz**: Viele wichtige Prozesse in der Software-Entwicklung, im Bereich Web-Apps und bei der Nutzung von Servern lassen sich mit der Kommandozeile besser automatisieren als mit grafischen Tools.
- **Macht der CLI**: Viele leistungsstarke Tools und Bibliotheken für Data Science sind direkt über die Kommandozeile zugänglich, z.B. Hadoop, Spark und Docker.

---

## Einführung der Begriffe: Bash, CLI, Shell

- **CLI (Command Line Interface)**: Eine textbasierte Benutzeroberfläche zur Interaktion mit dem Betriebssystem.
- **Shell**: Ein Kommandozeileninterpreter (CLI) bei Linux, der Befehle interpretiert und ausführt.
- **Bash**: Die "Bourne Again Shell" ist die am weitesten verbreitete Shell in Linux-Umgebungen.
  - Bash ist unter macOS vorinstalliert und kann auf Windows über das Windows Subsystem for Linux (WSL) oder Git Bash genutzt werden.

### Andere Shells:
- **Zsh**: Eine alternative Shell, die mehr Funktionen und Benutzerfreundlichkeit bietet.
- **Fish**: Eine moderne Shell mit einer intuitiven Syntax.
- **PowerShell**: Wird in Windows verwendet und hat tiefe Integration ins Windows-Betriebssystem.

---

## Installation und Einrichtung

### Bash unter Windows (via WSL)

Um Bash unter Windows zu nutzen, kannst du das **Windows Subsystem for Linux (WSL)** installieren. Die entsprechenden Schritte findet man in zahlreichen online-Tutorials, z.B. [hier](https://www.howtogeek.com/744328/how-to-install-the-windows-subsystem-for-linux-on-windows-11/).


### Alternativ: Git Bash

Eine einfachere Möglichkeit, Bash unter Windows zu nutzen, ist **Git Bash**:

1. Lade [Git für Windows](https://gitforwindows.org/) herunter und installiere es.
2. Git Bash wird zusammen mit Git installiert und bietet eine Bash-ähnliche Umgebung.

### MacOS: Bash ist vorinstalliert

Wenn du MacOS nutzt, hast du Glück – Bash ist bereits vorinstalliert. Du kannst einfach das Terminal öffnen und loslegen.



### Navigieren im Dateisystem:

Wir starten langsam und schauen uns erst einmal die Standard-Befehle an um Ordner zu wechseln und deren Inhalt zu sehen:

- `pwd` gibt den aktuellen Ordner an in dem wir uns befinden
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

### Nächster Schritt: Dateien & Verzeichnisse erstellen und löschen

Mit **bash** können wir einfach Dateien und Verzeichnisse erstellen oder eben auch löschen.



| Befehl          | Funktion                                                     |
| --------------- | ------------------------------------------------------------ |
| `mkdir new_dir` | "make directory" here: makes new directory "new_dir"         |
| `rm new_dir/`   | rm = "remove" --> Careful! Cannot be undone!                 |
| `ls -t`         | Sorts the directory contents by last-modified date (descending) |
| `ls -R`         | Recursively `ls` this direct                                 |

```

```

**Achtung!**
`rm new_dir/` Vorsicht! Dieser Befehl löscht Dateien/Verzeichnisse unwiderruflich! 

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

