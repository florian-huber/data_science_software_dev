# Shell Live Coding Session

## Erste Schritte - Wo bin ich?

```bash
pwd
ls
ls --help
```

## Sortierung nach letzter Änderung

```bash
ls -t
```

## Umkehrsortierung

```bash
ls -r 
```

### Übung:

Was machen die Einstellungen `-l` ("L" nicht "1") oder die Kombination aus `-l` und `-h` zusammen?

### Lösung:

- `-l` --> long listing format
- `-h` --> "human readable", z.B. 5.3k statt 5369

### Übung:

Findet über die Hilfe (`--help`) heraus wie alle Dateien alphabetisch mit ?

## Verzeichnisse erstellen

```bash
mkdir new_dir
ls
```

### Mehrere Verzeichnisse gleichzeitig erstellen

```bash
mkdir -p secrets/data
ls -R
```

**Hinweis**: Das ist das GLEICHE wie mit dem Explorer ein Verzeichnis zu erstellen!

### Dateien erstellen

Mit dem Nano-Editor:

```bash
cd secrets
nano my_diary.txt
```

Ohne Editor (erstellt leere Dateien):

```bash
touch data/facts1.csv data/facts2.csv data/facts3.csv
```

## Dateien verschieben und kopieren

```bash
cd data
mv facts3.csv facts0.csv
cp facts2.csv facts3.csv
```

### Verstecken von Dateien

```bash
mv secrets/ .secrets/
ls
ls -a
```

### Übung:

Wir haben eine Datei `statiscs.txt` erstellt, sie sollte aber `statistics.txt` heißen. Welchen Befehl würdest du verwenden, um sie umzubenennen?

 `cp statiscs.txt statistics.txt`

 `mv statiscs.txt statistics.txt`

 `mv statiscs.txt .`

`cp statiscs.txt .`

--> Antwort (2)

### Achtung beim Erstellen von Ordnern

Vermeide Namen mit Leerzeichen (oder anderen Sonderzeichen).

```bash
mkdir one long name
ls
```

Dies erstelle drei Ordner (one/, long/, und name/).

### Verzeichnisse löschen

Der folgende Befehl funktioniert NICHT:

```bash
rm new_dir/
```

Aber dieser funktioniert:

```bash
rm -r new_dir/
```

**Achtung**: Löschen mit `rm` ist endgültig!

### Übung:

Was macht der folgende Befehl?

```bash
rm -i facts3.csv
```

### Platzhalterzeichen: `*`

```bash
cd ..
mkdir submission/
```

Was macht der folgende Befehl? Und warum?

```bash
cp data/*1.* submission/
```

## Wortanzahlen

```bash
wc *.txt
```

## Ist Bash wirklich eine Programmiersprache?

### Ja! Hier ein paar Beispiele:

#### Variablen

```bash
greeting='Hello world!'
echo greeting
echo $greeting
```

#### Loops

For-Loop:

```bash
for Variable in {1..5}
do
    echo $Variable$
done
```

Traditionelle For-Schleife:

```bash
for ((a=1; a <= 5; a++))
do
    echo $a
done
```

### Shell-Skripte

Längere Code-Teile im Shell einzugeben ist nervig und macht darum auch niemand. Dazu verwenden wir **Shell-Skripte**, also Textdateien (mit `.sh` Endung) die den Bash Code enthalten.

Ausgeführt werden solche Shell-Skripte z.B. mit
```bash
bash my_script.sh
```

### Command-Line Interface

Wir können einem Shell-Skript Inputwerte mitgeben die intern über `$1`, `$2` , etc. nutzbar sind.

### Übung `repeater`

Hier geht es darum ein Shell-Skript (`repeater.sh`) zu schreiben und mit `bash repeater.sh 5 yes` ausführen. Das Skript soll dann 5 mal "yes" ausgeben. Dazu sollen intern die übergebenen Variablen `$1`und `$2` genutzt werden.

```bash
# Repeat $1 times
for ((a=1; a <= $1; a++))
do
# Print the second CLI input
    echo $2
done
```



### If-else Anweisungen & "Input"

Beispielcode:

```bash
echo -n "Enter a number:"
read variable

if [[ $variable -gt 10 ]]
then
echo "It is greater than 10!"
else
echo "It is smaller than 10!"
fi
```



### Bash + Python

Python-Code lässt sich einfach aus einem Shell-Skript ausführen mit:

```
python test_file.py
```

### Bash in Bash

Wir können Shell-Skripte einfach aus anderen Shell-Skripten heraus ausführen. Dazu müssten diese einfach nur aufgerufen werden!

```bash
./my_other_script.sh
```

Dies würde das im selben Ordner liegende Shell-Skript `my_other_script.sh` ausführen.
