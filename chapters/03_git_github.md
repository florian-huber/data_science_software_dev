# Git & GitHub

## Motivation

Jeder kennt das --> wir arbeiten an einem großeren Programm oder Textdokument und speichern verschiedene Versionen unter verschiedenen Namen.

Keine Sorge. Jede/r macht das (oder hat das gemacht).

Aber, es funktioniert nicht sonderlich gut, zumindest nicht für größere Projekte und erst recht nicht für Projekte an denen mehrere Leute mitarbeiten.

Probleme --> Viele Dateien! , Undeutlich wo/wann welche Änderung kam ...



![fig_versioning_unprofessional_way_01](..\images\fig_versioning_unprofessional_way_01.png)

Wenn wir mit mehreren Leuten asynchron arbeiten kommt noch hinzu, dass es oft sehr aufwendig bos unmöglich ist verschiedene Versionen zu kombinieren ("mergen").





![fig_versioning_unprofessional_way_02](..\images\fig_versioning_unprofessional_way_02.png)

## Warum Versionskontrolle (version control)?

--> expand this!

•Aufzeichnen Was, Wann durch Wen verändert wurde

•Unterschiedliche Versionen / Dateien vergleichen

•Einfaches Teilen mit Anderen

•Änderungen Anderer einbauen (merging)

•Fertige Produktversionen markieren (tags)

•Gefahrlos Ideen ausprobieren (branches)

•Standard in der IT/Software-Welt

**Achtung: Versionskontrolle** **≠** **Backup**



## Wie funktioniert Git (ungefähr)

--> expand this!

Nicht alle Dateien werden jeweils gespeichert ... sondern veränderungen/deltas...



![fig_versioning_deltas](..\images\fig_versioning_deltas.png)

## Grundlegender Prozess

--> expand: (stageing, commit...)



![fig_git_basic_process](..\images\fig_git_basic_process.png)

### Branches

--> expand: basic idea of branches, how to do with git



![fig_git_basic_process_branches](..\images\fig_git_basic_process_branches.png)

## Es geht nicht nur um eine Datei!

--> expand this:

**Bisher oft: 
** Projekte bestanden aus einer .py-Datei oder einem Jupyter Notebook

**
 Softwareprojekte, größere Data Science und** **KI Projekte****:** 
 Bestehen in der Regel aus mehreren Dateien und Ordnern.



Der Ordner der den Quellcode eines Projektes enthält (egal wie viele Dateien und Unterordner) wird insgesamt als **Repository** bezeichnet.



**Wichtig: 
** Versionskontrolle ist kein allgemeines Backup-Tool und sollte nicht ohne besonderen Grund auf (größere) Daten angewendet werden!



## Rad nicht neu erfinden

Git ist eine extrem verbreitetes Standardtool im Softwarebereich. Darum gibt es auch sehr viel (gutes) Material um das Thema zu erlernen und zu vertiefen. Zum Beispiel

- https://www.w3schools.com/git/
- https://www.atlassian.com/git