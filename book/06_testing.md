# Warum brauchen wir Testing?

Das Testen ist ein integraler Bestandteil der Softwareentwicklung und stellt sicher, dass der Code korrekt funktioniert und die festgelegten Anforderungen erfüllt. Es ist wichtig zu verstehen, dass selbst gut geschriebener und korrekt formatierter Code nicht automatisch fehlerfrei ist. In dieser erweiterten Einführung werden wir die Notwendigkeit des Testens, verschiedene Fehlerarten, die Realität fehlerfreier Software und unterschiedliche Testmethoden genauer beleuchten.

## Die Notwendigkeit des Testens

### Verständnis der verschiedenen Fehlertypen

In der Programmierung lassen sich Fehler allgemein in drei Kategorien einteilen:

- **Syntaxfehler**: Dies sind grammatikalische Fehler im Code, die verhindern, dass das Programm ausgeführt wird. Sie sind normalerweise am einfachsten zu erkennen und zu beheben.
- **Ausnahmen**: Dies sind Laufzeitfehler, die aufgrund von Anomalien während der Programmausführung auftreten, wie etwa der Versuch, durch Null zu teilen.
- **Semantische Fehler**: Diese sind am schwerwiegendsten und betreffen logische Fehler. Das Programm stürzt nicht ab, liefert aber falsche Ergebnisse.

### Der Mythos der 100% fehlerfreien Software

Das Konzept völlig fehlerfreier Software ist eher ein theoretisches Ideal als eine praktische Realität. Studien legen nahe, dass typische Software zwischen 10 und 100 Fehler (oder Defekte) pro 1.000 Codezeilen aufweist {cite}`phipps1999comparing`{cite}`lipow1982number`. Dies hängt natürlich stark von der Art der Software, dem Codierungsstil und der verwendeten Programmiersprache ab. Bei Java zum Beispiel liegen die typischen Zahlen bei 50-80 Defekten pro 1.000 Codezeilen und 3 bis 10 Fehlern pro 1.000 Zeilen {cite}`phipps1999comparing` (für C++ waren diese Zahlen deutlich höher!). Selbst gut getestete Software könnte etwa einen Fehler pro 1.000 Zeilen aufweisen. Um dies in Perspektive zu setzen, betrachten wir die Größe einiger bekannter Software:

- MATLAB: Ungefähr 100.000 Codezeilen.
- Linux-Kernel oder Microsoft Office: Etwa 10 Millionen Codezeilen.

Angesichts dieser Zahlen ist klar, dass Fehler in der Softwareentwicklung unvermeidlich sind. Diese Fehler können schwerwiegende Folgen haben, wie das Beispiel des Ariane-5-Raketenversagens im Jahr 1996 aufgrund eines Softwarefehlers zeigt.

### Was ist Testen?

Das Testen in der Softwareentwicklung ist der Prozess der Bewertung eines Systems oder seiner Komponenten, um festzustellen, ob es die festgelegten Anforderungen erfüllt. Es umfasst die Ausführung einer Systemkomponente, um Lücken, Fehler oder fehlende Anforderungen im Vergleich zu den tatsächlichen Anforderungen zu identifizieren.

#### Manuelles vs. automatisiertes Testen

- **Manuelles Testen**: Dabei spielen menschliche Tester die Rolle der Endbenutzer und nutzen alle Funktionen der Anwendung, um korrektes Verhalten sicherzustellen.
- **Automatisiertes Testen**: Hier werden Softwaretools verwendet, um Tests automatisch auszuführen, Testdaten zu verwalten und Ergebnisse zur Verbesserung der Softwarequalität zu nutzen. Es ist schneller und zuverlässiger für sich wiederholende Aufgaben.

#### White-Box- vs. Black-Box-Testing

- **White-Box-Testen**: Auch als Clear-Box- oder Glass-Box-Testen bekannt, konzentriert es sich auf die internen Strukturen oder Funktionsweisen einer Anwendung im Gegensatz zu deren Funktionalität. Es erfordert detaillierte Programmierkenntnisse.
- **Black-Box-Testen**: Konzentriert sich auf die Funktionalität der Software, ohne die internen Strukturen oder Funktionsweisen zu betrachten. Dieser Ansatz testet die Software aus der Perspektive des Benutzers.

#### Testarten

- **Akzeptanztest**: Bestimmt, ob das System die Benutzer- und Geschäftsanforderungen erfüllt.
- **Systemtest**: Überprüft das vollständig integrierte System, um die Konformität des Systems mit den festgelegten Anforderungen zu bewerten.
- **Integrationstest**: Konzentriert sich auf die Schnittstellen zwischen Einheiten/Komponenten, um sicherzustellen, dass sie korrekt zusammenarbeiten.
- **Unit-Test**: Umfasst das Testen einzelner Komponenten oder Einheiten eines Programms, um zu überprüfen, ob jede Einheit wie vorgesehen funktioniert. Es ist oft die erste Teststufe und bildet die Grundlage für spätere Teststufen.

### Fazit

Das Testen in seinen verschiedenen Formen ist eine wesentliche Praxis in der Softwareentwicklung. Es hilft, Fehler zu identifizieren und zu beheben, bevor das Softwareprodukt bereitgestellt wird, reduziert die Wahrscheinlichkeit von Ausfällen und stellt die Qualität der Software sicher. Während es vielleicht unerreichbar ist, eine vollständig fehlerfreie Anwendung zu erstellen, kann gründliches Testen die Anzahl der Defekte erheblich reduzieren und die Zuverlässigkeit und Leistung des Softwareprodukts verbessern.