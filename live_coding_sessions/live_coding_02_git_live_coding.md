# Live Coding: git & GitHub

(Erstellt auf Grundlage des Carpentry Git Kurses: https://carpentries-incubator.github.io/git-novice-branch-pr/)

## Git installieren
#### Windows:
[Hier](https://git-scm.com/downloads/win) herunterladen & installieren

#### macOS:
Um git zu installieren gibt es zwei Möglichkeiten:
1. Mit dem Paketmanager [homebrew](https://brew.sh/). Dazu im launchpad/spotlight die app *terminal* öffnen und folgende Befehle ausführen:
    1. wenn homebrew noch nicht installiert ist:
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    2. Terminal schließen und wieder öffnen
    3. git installieren: `brew install git`
2. oder mit den xcode command line tools. Dazu im launchpad/spotlight die app *terminal* öffnen und folgendes eingeben:
`xcode-select --install`


## Erste Schritte
- Läuft git? --> `git version`
- Einrichten:
  `git config --global user.name "Alice B"`
  `git config --global user.email "abc@def.com"`
- Die bisherigen Einstellungen lassen sich einsehen mit `git config --list`.
- Je nachdem wie git installiert wurde ist der Standardname für den Haupt-Branch "master" oder "main". Wenn es immer "main" sein soll, lässt sich dies auch nachträglich noch ändern mit:
  ```bash
  git config --global init.defaultBranch main
  ```

  



## Live Coding

(Teil des Materials wurde adaptiert von: https://carpentries-incubator.github.io/git-novice-branch-pr/03-create/)


#### Neues Projekt starten

- Zum Desktop gehen (oder anderem Ort)

- Neues Verzeichnis "planets" erstellen

  ```
  $ cd ~/Desktop
  $ mkdir planets
  $ cd planets
  ```

- Wir sind jetzt im neuen Verzeichnis "planets". Wir möchten dies zu einem git-Repository machen:

  ```
  $ git init
  ```

- Hat sich im Ordner etwas verändert?
  Vielleicht nicht auf den ersten Blick (`ls`, bzw. `dir`), aber bei genauerem Hinsehen schon:  `ls -a` (`dir /a` oder `dir -Force`) --> .git

- --> Neuer Ordner `.git` wurde erstellt. Darin wird die Projektgeschichte gespeichert. 

#### Erste Datei erzeugen und mit git tracken

```
$ nano mars.txt
```

Gib den folgenden Text in die `mars.txt` Datei ein:

```
Cold and dry, but everything is my favorite color
```

`mars.txt` enthält nun eine Zeile, die wir anzeigen können, indem wir ausführen:

```
$ cat mars.txt
```

Wenn wir den Status unseres Projekts erneut überprüfen, zeigt uns Git, dass es die neue Datei erkannt hat:

```
$ git status
On branch main

Initial commit

Untracked files:
   (use "git add <file>..." to include in what will be committed)

	mars.txt
nothing added to commit but untracked files present (use "git add" to track)
```

Die Nachricht "Untracked files" bedeutet, dass es eine Datei im Verzeichnis gibt, die Git nicht verfolgt. Wir können Git mit `git add` mitteilen, eine Datei zu verfolgen:

```
$ git add mars.txt
```

Danach können wir überprüfen, ob alles korrekt durchgeführt wurde:

```
$ git status
On branch main

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   mars.txt
```

Git weiß nun, dass es `mars.txt` verfolgen soll, hat diese  Änderungen jedoch noch nicht als Commit festgehalten. Um das zu tun, müssen wir noch einen Befehl ausführen:

##### Git commit

```
$ git commit -m "Start notes on Mars as a base"
[main (root-commit) f22b25e] Start notes on Mars as a base
 1 file changed, 1 insertion(+)
 create mode 100644 mars.txt
```

Wenn wir `git commit` ausführen, nimmt Git alles, was wir ihm mit `git add` zum Speichern mitgeteilt haben, und speichert eine Kopie dauerhaft im speziellen `.git` Verzeichnis. Diese dauerhafte Kopie wird als [commit](https://carpentries-incubator.github.io/git-novice-branch-pr/reference/#commit) (oder [revision](https://carpentries-incubator.github.io/git-novice-branch-pr/reference/#revision)) bezeichnet und ihr Kurzidentifikator ist `f22b25e` (Dein Commit könnte einen anderen Identifikator haben.)

Mit der `-m`-Option (für "message") können wir einen kurzen, beschreibenden und spezifischen Kommentar aufzeichnen, der uns später helfen wird, uns daran zu erinnern, was wir getan haben und warum. Wenn wir nur `git commit` ohne die `-m`-Option ausführen, startet Git `nano` (oder welchen anderen Editor wir als `core.editor` konfiguriert haben), damit wir eine längere Nachricht schreiben können.

[Gute Commit-Nachrichten](https://chris.beams.io/posts/git-commit/) beginnen mit einer kurzen (weniger als 50 Zeichen) Zusammenfassung der im Commit vorgenommenen Änderungen. Wenn du ins Detail gehen möchtest, füge eine leere Zeile zwischen der Zusammenfassung und deinen zusätzlichen Anmerkungen hinzu.

Danach --> `git status`



##### Git log

Wenn wir wissen wollen, was wir kürzlich gemacht haben, können wir Git bitten, uns die Historie des Projekts mit `git log` zu zeigen:

```
$ git log
commit f22b25e3233b4645dabd0d81e651fe074bd8e73b
Author: Alice B. Changing <alice@futurum.galaxy>
Date:   Thu Aug 22 09:51:46 2023 -0400

    Start notes on Mars as a base
```

`git log` listet alle Commits eines Repositoriums in  umgekehrter chronologischer Reihenfolge auf. Die Auflistung für jeden  Commit enthält den vollen Identifier des Commits (der mit den gleichen  Zeichen beginnt wie der Kurzidentifier, der vom `git commit`-Befehl zuvor gedruckt wurde), den Autor des Commits, wann er erstellt wurde,  und die Log-Nachricht, die Git beim Erstellen des Commits gegeben wurde.

Das ist alles etwas unübersichtlich, darum nutzen wir hier oft eine Kurzversion der Ansicht mit
```bash
git log --oneline
```



#### Datei verändern und aktualisieren

Jetzt fügen wir der Datei `mars.txt` eine weitere Zeile hinzu.

```bash
$ nano mars.txt
$ cat mars.txt
```

Output:

```
Cold and dry, but everything is my favorite color.
Having two moons sounds awesome!
```

Unsere Änderungen werden von Git erkannt (--> `git status`), aber es steht dort auch "no changes added to commit", d.h. die Änderungen werden nicht automatisch hinzugefügt. Dies muss aktiv durch uns selbst vorgenommen werden.
Zuerst können wir uns aber nochmal die Änderungen genau anschauen:

```bash
git diff
```

Das gibt in etwas sowas aus:

```
diff --git a/mars.txt b/mars.txt
index d6a9cf8..b2ccad4 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1 +1,3 @@
 Cold an dry, but everything is nicely red.
+Having two moons sounds awesome!
+
```

Falls wir mit den Änderungen einverstanden sind, können wir sie hinzufügen.

--> `git commit -m "add comment on moons"`

Das funktioniert aber nicht!

Denn wir haben den Stageing-Schritt vergessen. Korrekt muss der Ablauf so aussehen:

```bash
git add mars.txt
git commit -m "add comment on moons"
```

#### diff --> Optionen

Für `git diff` gibt es noch weitere Optionen, z.B. `--staged` wenn wir Änderungen anschauen wollen die schon mit `git add` in den Stageing-Bereich geschoben wurden. Oder `--color-words` wenn wir nicht Zeilen sondern Zeichen-weise vergleichen wollen.

#### Mini-Übung

Fügt jetzt eine weitere Zeile Text zu eurer `mars.txt` Datei und "committed" diese Änderungen mit Git.

#### Staging

Natürlich müssen wir diesen Prozess nicht immer für jede Zeile durchführen!
Zum Staging-Area können belieb viele Änderungen gleichzeitig oder nacheinander hinzugefügt werden. In der Praxis empfiehlt es sich, die einzelnen Commits nicht zu groß werden zu lassen, da nur die Commits wirkliche Speicherpunkte in der Geschichte darstellen (dazu später noch mehr).

Jetzt versuchen wir aber mehrere Arten von Änderungen einmal zu kombinieren.

#### Mini-Übung

- Einen weiteren Satz zu `mars.txt` hinzufügen
- Eine neue Datei `venus.txt` erstellen mit einem ersten Satz darin (z.B. "If mars is too cold for you, this might be a good place to consider.")
- Was steht nun bei `git status`? (Vor und nach `git add`)

Hier sehen wir zwei Arten von Änderungen:

```
...
	new file:   venus.txt
    modified:   mars.txt
```

Es fällt uns nun auf, dass wir doch lieber noch eine 2te Zeile zu `venus.txt` hinzufügen würden bevor wir das comitten.
Was geschieht jetzt bei `git status`?

[Randnotitz: es geht auch `git status -s` für einen Kurzreport]

#### Exploring history

Nicht immer sind wir zufrieden mit unseren Änderungen.
Bitte darum einmal eine weitere Zeile zu `mars.txt` hinzufügen.

Wir können die Änderungen zu bestimmten zeitlichen Punkten (commits) anschauen mit:

```bash
git diff HEAD~1 mars.text
```

Das bezieht sich immer auf den aktuellen Zustand (HEAD) und zählt Commits zurück.
Es ist auch möglich direkt auf einen bestimmten Commit zu verweisen und zwar über den mit `git log` angegebenen Hash.

```bash
git diff 6bdfa53a094b11e7f124ca894955b57dd2210f27
```

Die Hashes sind natürlich etwas sperrig. Am besten einfach Copy+Paste Nutzen (**übrigens**: in Bash geht das mit CTRL+INS/EINFG bzw. SHIFT+INS/EINFG).
Oder, wir können auch nur die ersten Zeichen eines Hashes nutzen. Solange das für Git eindeutig ist wird auch das funktionieren:

```bash
git diff 6bdfa5
```

### Changing history

Es gibt bei Git mehrere Wege um Änderungen wieder zurückzunehmen, z.B. bei versehentlichen oder fehlerhaften Änderungen. Hierbei gibt es aber eine Reihe von Dingen zu beachten. Die wichtigste Frage dabei ist: Wollen wir bestimmte Teil zu einem früheren Stand zurücksetzen (die zwischenzeitlichen Änderungen bleiben Teil der git-history), oder wollen wir komplett zu einem früheren Stand zurückkehren?
Außerdem ist wichtig zu wissen: Wurden die Änderungen bereits "committed", oder befinden sie sich nur in der Staging Area?

#### Staging Area: Un-committed mistakes

Dann einfach `git checkout HEAD mars.txt` um z.B. die noch Änderungen im Staging Bereich zu verwerfen.

#### Commits zurücknehmen mit `revert`

`git revert` ist die sicherste Methode um Änderungen zurückzunehmen. Die Historie wird nämlich nicht geändert, sondern nur ein vorheriger Zustand erneut als neuer Commit hinzugefügt.

**Szenario:** Sie möchten die Änderungen eines bestimmten Commits rückgängig machen, ohne den Verlauf zu verändern.

Um die Änderungen eines bestimmten Commits rückgängig zu machen, verwenden Sie:

```
$ git revert [COMMIT-HASH]
```

Wenn Sie zum Beispiel den letzten Commit rückgängig machen möchten, verwenden Sie:



```
$ git revert HEAD
```

`git revert` wird Sie dann zu einem Texteditor führen, um eine Commit-Nachricht für den neuen Revert-Commit einzugeben. Sie können die vorgeschlagene Nachricht übernehmen oder eine eigene hinzufügen.

Nachdem Sie die Nachricht gespeichert und den Editor geschlossen haben, wird ein neuer Commit erstellt, der die Änderungen des angegebenen Commits rückgängig macht.
Soll keine spezielle Nachricht erscheinen, sondern nur so etwas wie "Revert XYZ commit", dann geht dies mit der zusätzlichen option `--no-edit`, also `git revert HEAD --no-edit`.



#### Datei(en) mit `checkout`in einen Zustand vor einem bestimmten Commit versetzen

```bash
git checkout 6bdfa5 mars.txt
```

Oder

```bash
git checkout HEAD~1 mars.txt
```

Mit `git checkout` setzen Sie die Datei auf den Zustand eines früheren Commits zurück. Dies ist hilfreich, wenn Sie nur eine bestimmte Datei und nicht Ihr gesamtes Projekt rückgängig machen möchten.

Wir probieren das mal aus und fügen eine fehlerhafte Zeile zur `mars.txt` Datei hinzu.
`For germans, Mars is a candy bar.`

Danach fügen wir diese wie gewohnt hinzu mit `git add` und `git commit`.

Nun machen wir das Ganze wieder rückgängig mit `checkout`!

Überprüfen Sie den Inhalt von `mars.txt`:

```shell
$ cat mars.txt
```

Achtung!
Wenn wir hier nicht `mars.txt` dazu nehmen, dann erscheint eine Meldung `You are in 'detached HEAD' state.`.

Das kann mit `git checkout main` wieder geändert werden.

#### Mit `reset`: Nicht-committete Änderungen rückgängig machen

Wenn Sie Änderungen an einer Datei vorgenommen haben und diese Änderungen noch nicht committed wurden, können Sie diese Änderungen mit `git reset` verwerfen:

```bash
$ git reset --hard
```

Achtung: Der Befehl löscht alle nicht-committeten Änderungen in Ihrem Arbeitsverzeichnis.

**Mit `git reset`: Letzten Commit rückgängig machen**

Wenn Sie den letzten Commit rückgängig machen möchten, können Sie:

```bash
$ git reset HEAD~1
```

Hierbei werden die Änderungen aem letzten Commit in Ihrem Arbeitsverzeichnis beibehalten, aber der Commit selbst wird aus Ihrer Commit-Historie entfernt.

Wir probieren auch das einmal aus. Dazu fügen wir eine Zeile zu `mars.txt` hinzu, z.B. unsere Telefonnummer oder Kreditkartendaten. Und schließen das mit einem Commit ab.

Komischerweise merken wir erst dann, dass das vielleicht nicht so schlau war. Was jetzt?

Noch ist ja alles lokal, also nur bei uns auf dem eigenen Rechner. Daher lässt sich das noch einfach lösen und zwar über `git reset HEAD~1`. Nun einmal mit `git log` und `git diff` bzw. `cat mars.txt` anschauen was passiert ist...
Wir benötigen also noch einen Schritt, z.B. eine manuelle Anpassung der Datei, oder einfach ein erneutes `git checkout -- mars.txt`. Danach ist alles so, als wäre nichts geschehen.

#### Zusammenfassung von `revert` im Vergleich zu `checkout` und `reset`

- `git revert` erstellt einen neuen Commit und verändert nicht den Verlauf. Das macht es sicherer für Änderungen, die bereits öffentlich gemacht wurden.
- `git checkout` ändert den Zustand von Dateien zu einem bestimmten Commit, ändert aber nicht den Verlauf.
- `git reset` kann den Verlauf ändern, indem Commits entfernt werden. Es gibt verschiedene Modi (`--soft`, `--mixed`, `--hard`), die bestimmen, wie der Arbeitsbereich und der Index beeinflusst werden.

**Empfehlung:** In den meisten Fällen, insbesondere wenn Änderungen bereits in ein Remote-Repository gepusht wurden, ist `git revert` oder `git checkout` die sicherste Wahl, um Fehler rückgängig zu machen, da es keinen Verlauf umschreibt.

**Ausnahmen** sind zum Beispiel das versehentliche Hinzufügen von kritischen Inhalten, z.B. Passwörtern, Adressen etc. 



## Branches

Bisher haben wir immer auf einem geraden Zeitstrahl gearbeitet. Manchmal möchten wir jedoch unseren Hauptzweig vor experimentellen Änderungen schützen. Hierfür können wir Zweige (Branches) nutzen, um gleichzeitig an separaten Aufgaben zu arbeiten.

Betrachten wir die existierenden Branches mit:

```bash
$ git branch
* main
```

`*` zeigt den aktuellen Zweig an.

In dieser Lektion will Dracula eine Analyse durchführen und weiß nicht, ob sie schneller in Bash oder Python sein wird. Er wird separate Branches für beide Analysen verwenden und dann den schnelleren in seinen Hauptzweig zusammenführen.

Erstellen wir den Python-Branch:

```bash
$ git branch pythondev
$ git branch
* main
  pythondev
```

Wir sehen, dass wir den `pythondev` Branch erstellt haben, aber immer noch im `main` Branch sind.

Wechseln wir zum neuen Branch:

```bash
$ git checkout pythondev
$ git branch
  main
* pythondev
```

Nun erstellen wir unser Python-Skript:

```bash
$ touch analysis.py
$ git add analysis.py
$ git commit -m "Wrote and tested python analysis script"
```

Wechseln wir zurück zum `main` Branch:

```bash
$ git checkout main
```

Die Datei `analysis.py` ist nicht im `main` Branch. Wir können dies überprüfen mit `ls` und `git log`.

Wiederholen wir den Prozess für unser Bash-Skript in einem Branch namens `bashdev`:

```bash
$ git checkout -b bashdev
$ touch analysis.sh
$ git add analysis.sh
$ git commit -m “Wrote and tested bash analysis script”
```

Die Python-Analyse (`analysis.py`) ist viel schneller als `analysis.sh`. Fügen wir diese Version in unseren `main` Branch ein:

```bash
$ git checkout main
$ git merge pythondev
```

Nun löschen wir unsere alten Branches, um Verwirrung zu vermeiden:

```bash
$ git branch -d pythondev
```

Da wir die Änderungen im `bashdev` Branch nicht beibehalten wollen, löschen wir auch diesen Branch:

```bash
$ git branch -D bashdev
```

So haben wir erfolgreich Branches erstellt, verwendet und gelöscht, sowie Änderungen aus einem Branch in einen anderen zusammengeführt.



## Bonusmaterial: Wie speichert Git die Daten?

Nahezu alles was Git benötigt wird im `.git/` Ordner gespeichert.

```bash
git log --online
```

zeigt uns die bisherige Commit-Historie. Wir können uns die jeweiligen Git-Bäume anschauen mit

```bash
git ls-tree add-hash-here
```

Wobei der hash code des jeweiligen Commits der uns interessiert genutzt wird.

Einzelne Elemente des Baumes können angezeigt werden, z.B. mit:

```bash
git cat-file blob add-hash-here
```

Alle Bäume (trees), Commits, und Dateien (blobs) werden als Objekte im Ordner `objects/` gespeichert. Der jeweilige Inhalt wird über die SHA1 hash-Funktion in einen 160bit hash umgewandelt. Die ersten zwei Zeichen werden als Ordnername genutzt. Die jeweiligen Dateien, deren Name sich aus den restlichen Hash-Zeichen zusammensetzt, werden von git über Zip komprimiert um Speicherplatz zu sparen, darum sind sie nicht direkt sinnvoll lesbar (aber z.B. über `git cat-file`).

