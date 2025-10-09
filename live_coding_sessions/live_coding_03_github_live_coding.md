# Live Coding: git & GitHub

[TOC]



## Mini-Wiederholung

Im ersten Teil der git & GitHub Session hatten wir uns die Basics von Git angeschaut. Die zentralen Befehle und Schritte waren `git add`(--> Staging Area), `git commit` (--> .git Ordner), `git checkout` (zurück in den Arbeitsordner, bzw. Branch-Wechsel).

Für die Basics gibt es auch viele gute Cheat Sheets, z.B. hier: https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet oder hier: https://education.github.com/git-cheat-sheet-education.pdf



## GitHub Intro

### Erster Überblick

- Overview & Repositories

- (Projects kommt die nächsten Wochen)

- `Public profile` (unter Settings)

  

## How to create a Remote + (linked) Local Repository

Es gibt verschiedene Wege ein Remote Repository und ein dazugehöriges lokales Repository anzulegen. In den meisten Fällen gehen wir aber einen der folgenden zwei Wege:

### 1. GitHub first --> clone

Dieser Weg wird genommen wenn das Repository bereits bei GitHub existiert. Oder falls wir ein komplett neues Projekt beginnen und dazu in unserer eigenen GitHub Umgebung ein neues Repository erstellen.

Dann können wir einfach bei GitHub den HTTPS Link kopieren (Code --> Clone - HTTPS) und lokal auf unserem Rechner an unserem Wunschort den folgenden Befehl ausführen:
```bash
git clone https://github.com/<MY_GITHUB_USERNAME>/<MY_REPOSITORY_NAME>.git
```

- das Repository wird in den entsprechenden Ordner kopiert
- Local und Remote sind dann bereits über Git gekoppelt

### 2. Local Git first

Es kann natürlich auch sein, dass wir das Projekt bisher nur lokal auf unserem Rechner begonnen haben und es nun auf unseren GitHub-Account stellen möchten.

In dem Fall können wir ein Remote Repository erstellen und verlinken:

```bash
git init
git add --all
git commit -m 'Added my project'
git remote add origin https://github.com/<MY_GITHUB_USERNAME>/<MY_REPOSITORY_NAME>.git
git push -u -f origin main
```



### Mögliche Schwierigkeit: Verbinden mit GitHub

Nicht immer funktioniert der Zugang über HTTPS. Eine weitere Möglichkeit ist dann der Weg via SSH, siehe z.B.:

https://docs.github.com/en/get-started/quickstart/set-up-git

https://git-scm.com/book/en/v2/GitHub-Account-Setup-and-Configuration

https://carpentries-incubator.github.io/git-novice-branch-pr/02-setup/

## Arbeiten mit Remote Repository

### 1. Eigenes Projekt erstellen!

- Erstellt ein eigenes Repository: "solar_system"
  (Description = "HSD GitHub Crashkurs", Visibility = Private, add README = True)git

#### Option 1: VSCode
- Erstellt eine lokale Copy: In VSCode `Clone Git Repository` und gebt ein: `https://github.com/<MY_GITHUB_USERNAME>/<MY_REPOSITORY_NAME>.git`
- Es öffnet sich ein Fenster zu Anmeldung und ihr meldet euch einmalig an
- Öffnet das VSCode Terminal (`Ctrl+Shift+ö`) und schaut euch die remote settings an: `git remote -v`
- Erstellt einen Ordner `planets/`
- Erstellt darin eine Datei `mars.py` und kopiert Code
- Staged eure Änderungen, committed die Änderungen und pushed die Änderungen


- Erstellt eine lokale Copy mit `git clone`
  `git clone https://github.com/<MY_GITHUB_USERNAME>/<MY_REPOSITORY_NAME>.git`
  (erstellt eine Kopie und setzt den `remote` auf euer GitHub Repository)
- Schaut euch die Remote-Settings an: `git remote -v`
- Erstellt bei euch auf dem Rechner den Ordner `planets/`
- Erstellt darin eine Datei `mars.py` und kopiert Code
- Staged eure Änderungen, committed die Änderungen und pushed die Änderungen mit `git add .`, `git commit -m "DEINE COMMIT MSG"`, `git push origin main`



### 2. Gemeinsam an einem Repository arbeiten

- Fügt Eure/n Nachbar*in als `Collaborator` hinzu (Settings --> Collaborators --> Add people).

- Der/Diejenige muss nun erneut (am besten in einem anderen Ordner) mit `git clone` das entsprechende Repository kopieren.

- Nun sollten beide die Möglichkeiten haben Code zu ändern und hinzuzufügen!

- Erster Test --> Beide einmal über GitHub eine kleine Änderung an der README erstellen.

- Beide Änderungen sollten in den Commits auftauchen

- Zweiter Test --> Beide eine Zeile zur Beschreibung in mars.py hinzufügen.
  (merge conflict?)

- Besser: Arbeiten über Branches!

  Jede/r einen eigenen Branch lokal erstellen. Zur Einfachheit kurz absprechen, dass die Namen der Branches nicht identisch sind.

  In beiden Branches eine kleine Änderung am README vornehmen. Dann committen und pushen.

  Wenn nötig Merge Conflicts lösen.
  Über Pull Requests in den Main Branch mergen.

- Zur besseren Abstimmung (und Planung): Issues!
  Issues erstellen (mindestens eins pro Person im Team), z.B. "add venus", "add jupiter", ...

- Dann: Issue Assignment --> Jede/r wählt sich ein freies Issue aus ("assign yourself")
  Einen weiteren lokalen Branch erstellen (issue01, ...) und darin das Issue bearbeiten.
  Commit + Push

- Pull Request erstellen

- Pull Request von Partner*in reviewen

- Mergen

- Jeweils Lokal --> `git pull`

  

### 3. Über Fork an einem Repository arbeiten

--> https://github.com/ZDDduesseldorf/ascii-dojo.github.io





