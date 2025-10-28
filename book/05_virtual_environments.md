# Einführung: Python-Umgebungen für Data-Science-Projekte (venv, Miniconda/Mamba, Anaconda)

Eine **virtuelle Umgebung** kapselt eine Python-Version und alle installierten Pakete vom Rest des Systems. Das macht Projekte **reproduzierbar**, verhindert **Versionskonflikte** (z. B. „Projekt A braucht NumPy 2.x, Projekt B 1.x“) und ermöglicht **saubere Deployments** (z. B. auf Servern/CI).

---

## Warum brauchen wir virtuelle Umgebungen?

* **Isolation:** Jede Umgebung hat ihre eigene Python-Version und Bibliotheken.
* **Reproduzierbarkeit:** Anforderungen lassen sich als `requirements.txt` oder `environment.yml` festhalten und exakt wiederherstellen.
* **Stabilität:** Updates oder Tests gefährden nicht andere Projekte oder das System-Python.
* **Portabilität:** Ein Team kann identische Stände nutzen (wichtig für Lehre, Hausarbeiten, CI).

---

## Häufige Optionen im Überblick

| Option                                                                            | Kurzbeschreibung                                         | Stärken                                            | Mögliche Nachteile                                | Typische Nutzung                                                              |
| --------------------------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------- |
| **`venv`** (Standardbibliothek)                                                   | Eingebaute, schlanke Virtualisierung                     | Minimal, überall vorhanden, schnell                | Kein eigener Paket-Solver, reine `pip`-Welt       | Kleine bis mittlere Projekte, wenn nur PyPI nötig ist                         |
| **Miniconda / Mambaforge / MicroMamba** (im Folgenden „**Mamba/Conda (leicht)**“) | Leichte Conda-Distributionen; mit **mamba** sehr schnell | Starker Solver, **conda-forge** + `pip`            | Etwas Setup-Aufwand                               | Data-Science, gemischte Stacks (C/Fortran-Deps), schnelle Environment-Wechsel |
| **Anaconda**                                                                      | Große Distribution mit vielen Paketen vorinstalliert     | „Out of the box“ viel dabei, GUI-Tools (Navigator) | Schwergewichtig, längere Downloads, mehr Speicher | Einsteiger:innen, Offline-/Workshop-Setups                                    |

> **Faustregel:**
>
> * **Leicht & schnell:** `venv` oder **Miniconda/Mamba**
> * **Komfort/„alles dabei“:** **Anaconda**
> * Bei vielen nativen Abhängigkeiten (NumPy/SciPy/Geo/ML) sind **Conda-Kanäle** oft stressärmer als reines `pip`.

---

## Installation & Nutzung

### 1) `venv` – ist bei Python schon dabei

**Voraussetzung:** funktionierende Python-Installation (3.11/3.12/3.13).

Venv ist sofort bei Python "mit dabei", d.h. es muss nichts extra installiert werden.

**Neue Umgebung anlegen & nutzen:**

```bash
# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1

# Grundpakete aktualisieren
python -m pip install --upgrade pip setuptools wheel

# Pakete installieren
pip install numpy pandas matplotlib

# Abhängigkeiten einfrieren / wiederherstellen
pip freeze > requirements.txt
pip install -r requirements.txt

# Deaktivieren
deactivate
```

**Tipp:** Umgebung im Projektordner `.venv/` ablegen und nicht committen.

---

### 2) Miniconda / Mambaforge / MicroMamba – flexibel & schnell

> Empfehlung für Data-Science: **Mambaforge** (Conda + mamba + Standardkanal `conda-forge`) **oder** **MicroMamba** (sehr "leichtgewichtig", also keine umfangreiche eigene Software nötig).

#### Option A: **Mambaforge / Miniconda**

* **Download & Installation:**

  * **Windows/macOS:** Installer von den Projektseiten laden und durchklicken.
  * **Linux/macOS (Shell-Installer):**

    ```bash
    # Beispiel Mambaforge (aktuelle URL der Projektseite entnehmen)
    curl -LO https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
    bash Mambaforge-*.sh    # Lizenz akzeptieren, Install-Pfad bestätigen
    exec $SHELL             # neue Shell mit init-Skripten starten
    ```
* **Shell-Initialisierung (falls nötig):**

  ```bash
  conda init bash   # oder zsh/fish/pwsh je nach Shell
  exec $SHELL
  ```
* **mamba nachrüsten (falls nur conda vorhanden):**

  ```bash
  conda install -n base -c conda-forge mamba
  ```

#### Option B: **MicroMamba** (ultraleicht)

* **Einzeiler-Setup (Linux/macOS):**

  ```bash
  curl -L micro.mamba.pm/install.sh | bash
  # Danach Shell initialisieren:
  micromamba shell init -s bash -p ~/micromamba   # ggf. zsh/fish/pwsh
  exec $SHELL
  ```
* **Windows (PowerShell, Scoop):**

  ```powershell
  scoop install micromamba
  micromamba shell init -s powershell -p $env:USERPROFILE\micromamba
  ```
* **Hinweis:** `micromamba`-Befehle sind nahezu identisch zu `mamba`.

#### Nutzung (mamba/conda/micromamba – Syntax ähnlich)

```bash
# Neue Umgebung mit spezifischer Python-Version
mamba create -n ds310 python=3.12

# Aktivieren
mamba activate ds310

# Pakete aus conda-forge (empfohlen) installieren
mamba install -c conda-forge numpy pandas matplotlib scikit-learn

# PyPI-Pakete (nur falls benötigt) anschließend:
pip install package_only_on_pypi

# Umgebung als YAML exportieren (reproduzierbar!)
mamba env export --from-history > environment.yml

# Aus YAML neu erstellen
mamba env create -n ds310 -f environment.yml

# Aufräumen
mamba env list
mamba env remove -n ds310
```

**Kanäle:** Für moderne DS-Stacks ist `-c conda-forge` meist die beste Wahl (aktuelle Builds, viele Plattformen).

---

### 3) Anaconda – „alles dabei“

* **Download:** grafischer Installer für Windows/macOS, `.sh` für Linux.
* **Installation:** durchklicken; optional **Anaconda Navigator** (GUI) verwenden.
* **Erstkonfiguration (Terminal):**

  ```bash
  conda init bash   # oder zsh/fish/pwsh
  exec $SHELL
  ```
* **Umgebungen & Pakete:**

  ```bash
  conda create -n ds310 python=3.12
  conda activate ds310
  conda install -c conda-forge numpy pandas jupyterlab seaborn
  conda env export --from-history > environment.yml
  conda env create -n ds310 -f environment.yml
  ```
* **Navigator (GUI):** Umgebungen anlegen, Pakete suchen, Jupyter starten – alles per Klick.

---

## Prüfen, Aktualisieren, Deinstallieren

```bash
# Versionen prüfen
python --version
pip --version
conda --version     # bzw. mamba --version / micromamba --version

# Basissystem aktualisieren (Conda/Mamba)
mamba update -n base -c conda-forge conda mamba

# Pakete in aktiver Env aktualisieren
mamba update --all

# (Teil-)Deinstallation:
mamba remove paketname
mamba env remove -n envname
```

---

## Best Practices

* **Ein Projekt ⇒ eine Umgebung.**
* **Versionsnummern festhalten** (z. B. `python=3.12`, `numpy=2.*`).
* **Wiederholbarkeit testen:** frische Umgebung aufsetzen und Projekt starten lassen.
* **`conda-forge` bevorzugen**, dann erst `pip` für fehlende Pakete.
* **Keine globalen Installationen** (`sudo pip install` vermeiden).
* **`.venv/` und `envs/` nicht committen**; nur `requirements.txt`/`environment.yml`.

---

## Kurze Entscheidungshilfe

* **Minimaler Overhead, reine PyPI-Pakete:** `venv`
* **Viele native/NumPy/SciPy/ML-Pakete, schneller Solver:** Miniconda/Mamba (oder MicroMamba)
* **Komplettlösung mit GUI & vielen Paketen ab Werk:** Anaconda
