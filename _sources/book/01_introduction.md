# Data Science und AI Infrastrukturen

Bisher (1. und 2. Semester) haben wir mit Hilfe von Python, zahlreichen Python Bibliotheken und Jupyter Notebooks komplette Data Science Workflows umgesetzt. Die Vorteile von dieser Art zu arbeiten liegen auf der Hand:

- schnelle Umsetzbarkeit
- Kompletter Ablauf von Datenimport bis hin zu den Visualisierungen in einer Umgebung
- Kann gleichzeitig zur Dokumentation des Prozesses und der Ergebnisse dienen
- Wiederausführbar mit Möglichkeit einzelne Code-Zellen jederzeit anzupassen und zu ergänzen
- Damit: sehr zügiges, dynamisches Arbeiten möglich. 

Ideal für den Data Science Prozess!

Oder doch nicht?

### Grenzen des Notebooks

Jupyter Notebooks sind für viele Anwendungen im Data Science Bereich sehr nützlich und werden (aus gutem Grund) in der Praxis auch sehr häufig verwendet. Allerdings hat diese Form zu arbeiten einige sehr wichtige Begrenzungen!

- Jupyter Notebooks sind sehr gut für das schnelle Testen und Erkunden ("Prototyping").
- Wenn sie sehr ordentlich erstellt werden, eignen sie sich auch Prozesse zu dokumentieren ("Literate Programming")

Über diese Schritte hinaus, sind Jupyter Notebooks allerdings nicht mehr nutzbar, oder zumindest nicht sehr praktisch. Aber was sollen diese Schritte darüber hinaus eigentlich sein?

#### Getting serious

Falls es unser Ziel war, nur einmalig bestimmte Analysen durchzuführen, Korrelationen zu finden, eine erste Aussage zu treffen etc., dann kann es gut sein, dass ein komplettes Data Science Projekt vollständig in Jupyter Notebook(s) umsetzbar ist. Das fertige Notebook und die damit generierten Grafiken sind quasi unser Endprodukt und wir können unser Projekt danach abschließen.

Häufig geht ein Projekt aber deutlich weiter, etwa wenn:

- eine Analyse auf verschiedenen Datensätzen, durch verschiedene Personen, oder zu verschiedenen Zeitpunkten erneut durchgeführt werden soll (--> "Reproduzierbarkeit")
- ein Produkt das Ziel des Projektes ist. Zum Beispiel ein Machine Learning Modell das später in einer bestimmten Software verwendet werden soll. Oder eine Web-App, ein Dashboard, eine Erkennungsmethode usw.
- die Abläufe/Analysen in eine umfangreicher Software (oder auch ein umfangreicheren Workflow) eingefügt werden sollen.
- weitere Optimierungsschritte nötig sind

Um auf diese Stufe zu kommen müssen wir uns mit einigen Aspekten aus dem Bereich Softwareentwicklung vertraut machen. Wichtige Ziele sind dabei:

- Code schreiben der verlässlich ist (ausgibt was er soll).
- Code schreiben der nachhaltig funktioniert ("auf meinem Rechner lief alles...").
- Code mit mehreren Leuten entwickeln.
- Code optimieren.

Für alle diese Punkte sind Jupyter Notebooks nicht gut geeignet.



Eine weiter Grenze der Notebooks sind

#### Performance-Limits

Notebooks funktionieren gut solange sie nicht mehr als die frei verfügbaren Ressourcen unseres Computers  in Anspruch nehmen. D.h. nur soviel Arbeitsspeicher wie vorhanden und nur soviel CPU/GPU das wir nicht tagelang auf Berechnungen warten müssen. Je nach Bereich und Aufgabe werden diese Grenzen aber oft sehr schnell gesprengt! 

Frage: Gab es schon Probleme, bei denen die Hardware die zu Verfügung stand nicht mehr ausgereicht hat?

