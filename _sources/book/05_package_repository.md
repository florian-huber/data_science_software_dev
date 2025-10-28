# Python Package / Repository: Von `import` bis eigenes installierbares Paket

Dieses Kapitel zeigt, wie **Imports** in Python funktionieren, warum **Dependencies** sauber definiert werden müssen, und wie du ein **installierbares Python-Package** in einem Git-Repository aufbaust (inkl. `pyproject.toml` mit Poetry), sodass man es mit `pip install git+https://...` installieren kann.

---

## 1) Wie funktionieren `import`s in Python?

### 1.1 Import-Suche (vereinfacht)

Wenn du `import numpy as np` oder `from mypkg.utils import foo` schreibst, sucht Python Module/Packages in folgender Reihenfolge:

1. **Aktuelles Projekt / Arbeitsverzeichnis** (der Ordner, von dem aus das Skript/Notebook gestartet wurde)
2. **Installierte Pakete** in der **aktiven Umgebung** (venv/Conda/Mamba)
3. **Standardbibliothek**

Die Suchpfade liegen in `sys.path`. Welche Pakete „sichtbar“ sind, hängt **direkt von der aktiven Umgebung** ab – daher die enge Verbindung zu virtuellen Environments.

> **Merke:** Wenn etwas „nicht importierbar“ ist, ist oft die **falsche Umgebung aktiv** oder das Paket **nicht installiert**.

### 1.2 Module vs. Packages

* **Modul**: einzelne Datei `foo.py` → importierbar als `import foo`
* **Package**: Ordner mit `__init__.py`, z. B.:

  ```
  mypkg/
    __init__.py
    utils.py
    data/
      __init__.py
      loader.py
  ```

  → `from mypkg.utils import func`

> Für Einsteiger:innen: Lege **eine `__init__.py`** in jeden Package-Ordner, dann verhält es sich zuverlässig als Paket.

### 1.3 Absolute vs. relative Imports

* **Absolut** (empfohlen): `from mypkg.utils import foo`
* **Relativ** (innerhalb des Pakets): `from .utils import foo` oder `from ..data.loader import load`

Absolute Imports sind robuster, v. a. wenn das Paket installiert (nicht nur als „loser“ Ordner) benutzt wird.

---

## 2) Reproduzierbare Projekte: Dependencies festhalten

### 2.1 Pip/venv („requirements.txt“)

* **Erstellen:**

  ```bash
  pip freeze > requirements.txt
  ```
* **Verwenden:**

  ```bash
  pip install -r requirements.txt
  ```

Pins sind hier meist **exakt** (`pkg==1.2.3`). Für längerfristige Reproduzierbarkeit ist das gut, kann aber bei Updates unflexibel sein.

### 2.2 Conda/Mamba („environment.yml“)

* **Export (nur explizite Pakete):**

  ```bash
  mamba env export --from-history > environment.yml
  ```
* **Erstellen:**

  ```bash
  mamba env create -n myenv -f environment.yml
  ```

YAML erlaubt Python-Version, Kanäle (`conda-forge`) und optionale `pip`-Sektion.

### 2.3 Poetry (lockfile)

Poetry verwaltet Dependencies in `pyproject.toml` und erstellt **`poetry.lock`**:

* **Installation gemäß Lockfile**: exakt reproduzierbar
* **`poetry add numpy`** schreibt semantische Versionsbereiche (z. B. `^2.1`)

> **Tipp:** Für Lehr-/Team-Setups ist ein **Lockfile** (Poetry) oder ein **strikt gepinnter** `requirements.txt` sinnvoll.

---

## 3) Nächstes Level: Ein **installierbares** Python-Package im Repository

Ziel:

* Lokale Entwicklung mit sauberem Imports.
* Installation direkt aus GitHub:

  ```bash
  pip install git+https://github.com/<user>/<repo>.git
  ```

  (Optional: `#subdirectory=src` oder `#egg=mypkg` in Spezialfällen.)

### 3.1 Empfohlene Ordnerstruktur („src layout“)

```
myproject/
├─ src/
│  └─ mypkg/
│     ├─ __init__.py
│     ├─ core.py
│     └─ utils.py
├─ tests/
│  └─ test_core.py
├─ pyproject.toml
├─ README.md
├─ LICENSE
├─ .gitignore
└─ (optional) .pre-commit-config.yaml, ruff.toml, environment.yml
```

Warum `src/`?

* Verhindert, dass „zufällig“ lokale Imports funktionieren, wenn das Paket **nicht installiert** ist.
* Testet realistische Import-Pfade (wie bei Installation).

### 3.2 `pyproject.toml` (mit Poetry)

Minimalbeispiel (Poetry-Variante):

```toml
[tool.poetry]
name = "mypkg"
version = "0.1.0"
description = "Beispielpaket für DS-Kurs"
authors = ["Dein Name <you@example.com>"]
readme = "README.md"
license = "MIT"
packages = [{ include = "mypkg", from = "src" }]

[tool.poetry.dependencies]
python = ">=3.11,<3.14"
numpy = "^2.0"
pandas = "^2.2"

[tool.poetry.group.dev.dependencies]
pytest = "^8.0"
ruff = "^0.6"

[tool.poetry.scripts]
mypkg-cli = "mypkg.core:main"   # CLI-Einstiegspunkt (optional)

[build-system]
requires = ["poetry-core>=1.7.0"]
build-backend = "poetry.core.masonry.api"
```

**Wichtigste Felder:**

* **`name`**: Paketname (so heißt es auf PyPI / bei `pip install`).
* **`version`**: Semantische Versionierung (z. B. `0.1.0`).
* **`packages`**: Wo der Code liegt (src-Layout!).
* **`dependencies`**: Laufzeit-Abhängigkeiten.
* **`group.dev.dependencies`**: Dev-Tools (Tests, Linter).
* **`scripts`**: CLI-Entry-Points → `mypkg-cli` wird ein aufrufbares Kommando.
* **`build-system`**: `poetry-core` als Build-Backend.

> Alternativ (PEP 621) kann man `[project]`-Felder nutzen; mit Poetry ist die gezeigte `[tool.poetry]`-Variante weiterhin verbreitet und unkompliziert.

### 3.3 Poetry: typische Befehle

```bash
# Projekt initialisieren (im Repo-Root)
poetry init        # interaktives Setup der pyproject.toml
# oder neues Grundgerüst:
poetry new --src myproject
# -> erzeugt src/myproject, tests/, pyproject.toml, README.md

# Abhängigkeiten hinzufügen
poetry add numpy pandas
poetry add --group dev pytest ruff

# Umgebung / Installation
poetry install     # erstellt venv + installiert Paket (editable) + deps
poetry shell       # aktiviert die Poetry-venv

# Lint/Tests (Beispiel)
ruff check src
pytest -q

# Bauen (sdist + wheel)
poetry build
# -> dist/mypkg-0.1.0.tar.gz und .whl

# (Optional) Veröffentlichen auf PyPI
poetry publish --build
```

### 3.4 `pip install` direkt aus Git (VCS-URL)

Sobald das Repo eine gültige `pyproject.toml` hat (mit `build-system`) und dein Paket unter `src/` liegt, kannst du es ohne PyPI installieren:

```bash
pip install git+https://github.com/<user>/<repo>.git
# Einen Branch/Tag/Commit angeben:
pip install git+https://github.com/<user>/<repo>.git@v0.1.0
# Falls das Package nicht im Repo-Root liegt:
pip install "git+https://github.com/<user>/<repo>.git#subdirectory=subdir_path"
```

> Für Entwicklungs-Workflows lokal: `pip install -e .` (editable install) – mit Poetry erledigt `poetry install` das automatisch in der Poetry-venv.

### 3.5 Tests, Qualität, CI (Kurz)

* **Tests**: `pytest` in `tests/`
* **Linter/Format**: `ruff`, `black` (oder nur `ruff format`)
* **Pre-commit**: Hooks für Autoformat/Lint vor jedem Commit
* **CI**: GitHub Actions, z. B. Matrix über Python-Versionen, `poetry install`, `pytest`, ggf. Build

---

## 4) Typisches Repo-Setup (Checkliste)

* `pyproject.toml` (Poetry + Build-Infos)
* `src/<paketname>/` mit `__init__.py` und Modulen
* `tests/` mit ersten Unit-Tests
* `README.md` (Install, Usage, Beispiele)
* `LICENSE` (z. B. MIT)
* `.gitignore` (z. B. Python, Poetry, venv)
* *(optional)* `ruff.toml`, `.pre-commit-config.yaml`, `environment.yml` oder `requirements.txt` für Lehr-/CI-Use-Cases

Beispiel für `.gitignore`-Ausschnitt:

```
# Environments / Build
.venv/
dist/
build/
*.egg-info/
__pycache__/

# Editor / OS
.DS_Store
.idea/
.vscode/
```

---

## 5) Häufige Stolpersteine & Tipps

* **„Module not found“**: Ist die **richtige Umgebung aktiv**? Wurde das Paket **installiert** (`poetry install` / `pip install -e .`)?
* **Mischen von conda & pip**: Erst möglichst viel über `conda-forge`, dann fehlende Pakete per `pip`. Bei Poetry bleib konsistent innerhalb der Poetry-venv.
* **Versionsstrategie**: Für Anwendungen/Lehre **fixe Versionen** (Lockfile / Pins). Für Libraries **kompatible Bereiche** (z. B. `^2.0`).
* **CLI-Tools**: Über `[tool.poetry.scripts]` elegant abbilden.
* **`__init__.py` nicht vergessen**: Sonst erkennt Python Ordner evtl. nicht als reguläres Paket (außer bei Namespace-Packages – für den Anfang eher weglassen).

---

### Mini-Startvorlage

```bash
# Neues Repo anlegen
mkdir myproject && cd myproject
git init

# Poetry & Paket
poetry init -n --name "mypkg" --description "DS-Beispiel" --license MIT
poetry add numpy pandas
poetry add --group dev pytest ruff

# Ordner anlegen
mkdir -p src/mypkg tests
touch src/mypkg/__init__.py
printf "def main():\n    print('hello from mypkg')\n" > src/mypkg/core.py

# CLI-Eintrag in pyproject.toml ergänzen:
# [tool.poetry.scripts]
# mypkg-cli = "mypkg.core:main"

# Install & Test
poetry install
poetry run mypkg-cli
poetry run pytest -q
```

Mit diesem Setup sind Imports stabil, Abhängigkeiten reproduzierbar festgehalten, und dein Projekt ist als **richtiges Python-Package** nutzbar – lokal, in CI, und direkt aus GitHub installierbar.
