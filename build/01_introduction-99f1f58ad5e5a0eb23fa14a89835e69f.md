# Einführung
Dieses Skript begleitet den Kurs "Data Science und AI Infrastrukturen" im Studiengang DAISY an der [Hochschule Düsseldorf](https://www.hs-duesseldorf.de/).

Bisher (1. und 2. Semester) haben wir, z.B. in der [Einführung Programmieren](https://florian-huber.github.io/python-introduction/) und in der [Einführung Data Science](https://florian-huber.github.io/data_science_course/) mit Hilfe von Python, zahlreichen Python Bibliotheken und Jupyter Notebooks komplette Data Science Workflows umgesetzt. Die Vorteile von dieser Art zu arbeiten liegen auf der Hand:

- schnelle Umsetzbarkeit
- Kompletter Ablauf von Datenimport bis hin zu den Visualisierungen in einer Umgebung
- Kann gleichzeitig zur Dokumentation des Prozesses und der Ergebnisse dienen
- Wiederausführbar mit Möglichkeit einzelne Code-Zellen jederzeit anzupassen und zu ergänzen
- Damit: sehr zügiges, dynamisches Arbeiten möglich. 

Ideal für den Data Science Prozess!

Oder doch nicht?

## Grenzen des Notebooks

Jupyter Notebooks sind für viele Anwendungen im Data Science Bereich sehr nützlich und werden darum aus gutem Grund in der Praxis sehr häufig verwendet. Besonders geeignet sind Jupyter Notebooks für das schnelle Testen und Erkunden ("Prototyping"). Wenn sie sehr ordentlich erstellt werden, eignen sie auch sehr gut um Prozesse zu dokumentieren (Stichwort: "Literate Programming").

Allerdings hat diese Form zu arbeiten einige sehr wichtige Begrenzungen!
Wer schon häufig mit anderen im Team gearbeitet hat, wird möglicherweise schon festgestellt haben, das es nicht besonders einfach ist mit mehreren Leuten gemeinsam an Jupyter Notebooks zu arbeiten. Und auch wenn sauber erstelltes und dokumentiertes Notebook gut lesbar sein kann, bedeutete das noch lange nicht, dass es auch bei anderen im Team direkt ausführbar ist.
Wir kommen also recht schnell an Grenzen, ab denen Jupyter Notebooks nicht mehr nutzbar, oder zumindest nicht sehr praktisch sind. Genau in diesen Bereich möchten wir uns in diesem Kurs vortasten. Es geht um das Erlernen und Anwenden von Schlüsseltechniken die euch erlauben werden, professionelle Data Science Workflows zu entwickeln und zu implementieren die deutlich den Rahmen von Jupyter Notebooks sprengen, sei es durch höhere Komplexität, erhöhte Verlässlichkeit und Reproduzierbarkeit, oder stark verbesserte Performance.

### Getting serious

Falls es unser Ziel war, nur einmalig bestimmte Analysen durchzuführen, Korrelationen zu finden, eine erste Aussage zu treffen etc., dann kann es gut sein, dass ein komplettes Data Science Projekt vollständig in Jupyter Notebook(s) umsetzbar ist. Das fertige Notebook und die damit generierten Grafiken sind quasi unser Endprodukt und wir können unser Projekt danach abschließen.

Häufig geht ein Projekt aber deutlich weiter, etwa wenn:

- eine Analyse auf verschiedenen Datensätzen, durch verschiedene Personen, oder zu verschiedenen Zeitpunkten erneut durchgeführt werden soll (Stichwort: "Reproduzierbarkeit")
- ein Produkt das Ziel des Projektes ist. Zum Beispiel ein Machine Learning Modell das später in einer bestimmten Software verwendet werden soll. Oder eine Web-App, ein Dashboard, eine Erkennungsmethode usw.
- die Abläufe/Analysen in eine umfangreicher Software (oder auch ein umfangreicheren Workflow) eingefügt werden sollen.
- weitere Optimierungsschritte nötig sind

Um auf diese Stufe zu kommen müssen wir uns mit einigen Aspekten aus dem Bereich Softwareentwicklung vertraut machen. Wichtige Ziele sind dabei:

- Code schreiben der verlässlich ist (ausgibt was er soll).
- Code schreiben der nachhaltig funktioniert (also nicht mehr: "auf meinem Rechner lief aber alles...").
- Code mit mehreren Leuten entwickeln.
- Code optimieren.

Für alle diese Punkte sind Jupyter Notebooks nicht gut geeignet.


Eine weiter Grenze der Notebooks sind

### Performance-Limits

Notebooks funktionieren gut solange sie nicht mehr als die frei verfügbaren Ressourcen unseres Computers  in Anspruch nehmen. D.h. nur soviel Arbeitsspeicher wie vorhanden und nur soviel CPU/GPU das wir nicht tagelang auf Berechnungen warten müssen. Je nach Bereich und Aufgabe werden diese Grenzen aber oft sehr schnell gesprengt! 
