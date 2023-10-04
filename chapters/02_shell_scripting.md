# Shell Scripting

### Zurück in die Zukunft... Shell scripting!

iele von uns sind es gewohnt, Computer über grafische Benutzeroberflächen zu bedienen. Das Öffnen eines Terminals kann wie eine Reise in die Vergangenheit erscheinen. Doch im Bereich Data Science und KI gibt es triftige Gründe, sich mit der Kommandozeile vertraut zu machen. Lassen Sie uns einen Blick in die Geschichte werfen:

#### Unix

Unix ist ein Betriebssystem, das in den 1970er Jahren bei AT&T Bell Labs entwickelt wurde. Es war die Basis für viele moderne Betriebssysteme und führte Konzepte wie das hierarchische Dateisystem und die Verwendung von einfachen Textdateien für die Systemkonfiguration ein.

#### Linux

Linux ist ein Unix-ähnliches Betriebssystem, das in den frühen 1990ern von Linus Torvalds entwickelt wurde. Es verwendet den Linux-Kernel und bietet eine breite Palette von Tools und Anwendungen für Entwickler.

#### Shell

Die Shell ist eine Benutzeroberfläche, die dem Benutzer den Zugriff auf die Funktionen eines Betriebssystems ermöglicht. Dabei werden Befehle in Textform eingegeben.

#### Bash

Bash (Bourne Again SHell) ist eine der bekanntesten Shells und wurde als Ersatz für die Bourne Shell entwickelt. Sie bietet viele Erweiterungen und Verbesserungen, die in anderen Shells nicht zu finden sind.

------

### Bash

Das gute an Bash-Befehlen: Man muss sie nicht auswendig lernen! Bei Unsicherheiten können Befehle einfach nachgeschlagen werden. Für einen schnellen Überblick gibt es z.B. [hier](https://www.educative.io/blog/bash-shell-command-cheat-sheet) eine Übersicht.



#### Teil 1 - Dateien und Ordner

Wir starten langsam und schauen uns erst einmal die Standard-Befehle an um Ordner zu wechseln und deren Inhalt zu sehen:

- `pwd` gibt den aktuellen Ordner an in dem wir uns befinden
- `ls`(für list/listing) zeigt alle Dateien und Unterordner
- mit `cd foldername` gehe ich in einen Ordner namens "foldername", mit `cd ..` gehe ich wieder einen Ordner tiefer zurück
- mit `--help` können Hinweise zu den möglichen Parametern abgefragt werden, z.B. `ls --help`.


Befehle sind immer wie folgt aufgebaut:

![image-20220909135234762](C:\Users\flori\AppData\Roaming\Typora\typora-user-images\image-20220909135234762.png)

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



### Und noch vieles mehr.

Bash kann noch viel mehr, aber das werden wir (vorläufig) noch nicht benötigen. So können beispielsweise auch Funktionen definiert werden und vieles mehr.

Für weitere Übungen, Tipps und Beispiele zu Bash hier einige Links:

- https://www.learnshell.org/
- https://explainshell.com/
- https://wiki.ubuntuusers.de/Shell/Bash-Skripting-Guide_f%C3%BCr_Anf%C3%A4nger/

