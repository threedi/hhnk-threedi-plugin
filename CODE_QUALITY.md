# Code Quality Improvements

Dit document beschrijft de code kwaliteitsverbeteringen die zijn geïmplementeerd voor het HHNK 3Di Plugin project.

## Inhoudsopgave

- [Geconstateerde Bevindingen](#geconstateerde-bevindingen)
- [Geïmplementeerde Oplossingen](#geïmplementeerde-oplossingen)
- [Gebruik van de Tools](#gebruik-van-de-tools)
- [CI/CD Pipeline](#cicd-pipeline)
- [Volgende Stappen](#volgende-stappen)

## Geconstateerde Bevindingen

Tijdens de code analyse zijn de volgende punten geïdentificeerd:

### 1. Branch Management
- **Probleem**: Branches zonder ticketnummer
- **Impact**: Moeilijk om wijzigingen te traceren naar requirements
- **Status**: ✅ Opgelost

### 2. Pre-commit Hooks
- **Probleem**: Ontbrekende of niet-geïntegreerde pre-commit hooks en type checks
- **Impact**: Inconsistente code kwaliteit, late detectie van problemen
- **Status**: ✅ Opgelost

### 3. Test Coverage
- **Probleem**: Coverage < 70% of onbekend op kritische modules
- **Impact**: Verhoogd risico op onopgemerkte bugs
- **Status**: ⚠️ Framework opgezet, tests moeten nog worden toegevoegd

### 4. Logging
- **Probleem**: Logging inconsistent of niet aanwezig
- **Impact**: Moeilijk debuggen in productie
- **Status**: ✅ Framework opgezet

### 5. Hardcoded Waarden
- **Probleem**: Hardcoded waarden/paden/locaties
- **Impact**: Moeilijk te onderhouden, niet flexibel
- **Status**: ⚠️ Moet handmatig worden geïdentificeerd en opgelost

### 6. Release Management
- **Probleem**: Weinig releases met te grote changes
- **Impact**: Moeilijk rollback, grote risico's per release
- **Status**: 📋 Workflow opgezet voor betere releases

### 7. Python Versie
- **Probleem**: Python versie erg laag
- **Impact**: Missen van moderne features en security updates
- **Status**: ✅ Minimale versie nu Python 3.11

### 8. Build Systeem
- **Probleem**: Inconsistentie in build systeem (hatchling, wheels)
- **Impact**: Moeilijk reproduceerbare builds
- **Status**: ✅ Gestandaardiseerd op hatchling

### 9. Configuration Files
- **Probleem**: pyproject.toml en pixi.toml niet consistent
- **Impact**: Verwarring over dependencies
- **Status**: ✅ pyproject.toml gestandaardiseerd

### 10. Documentatie
- **Probleem**: Doc strings niet consistent of ontbreken
- **Impact**: Moeilijk te begrijpen code
- **Status**: ⚠️ Style guide opgezet, moet handmatig worden toegepast

## Geïmplementeerde Oplossingen

### 1. Pre-commit Hooks (`.pre-commit-config.yaml`)

Automatische checks bij elke commit:

```yaml
- Ruff: Linting en formatting
- MyPy: Type checking
- Flake8: Style guide enforcement
- Bandit: Security scanning
- General checks: Trailing whitespace, YAML validation, etc.
```

**Voordelen:**
- Problemen worden direct bij commit ontdekt
- Consistente code style
- Security issues worden vroeg gedetecteerd

### 2. PyProject.toml Configuratie

Volledig geconfigureerd met:

```toml
[build-system]
- Hatchling als build backend
- Python 3.11+ als minimum versie

[tool.ruff]
- Line length: 119
- NumPy docstring convention
- Extended rule set voor betere code kwaliteit

[tool.mypy]
- Type checking configuratie
- Ignore voor test bestanden

[tool.pytest]
- Coverage target: 80%
- HTML en XML reports
- Test paths geconfigureerd

[tool.coverage]
- Source directory: hhnk_threedi_plugin
- Exclusions voor tests en patches

[tool.bandit]
- Security scanning configuratie
- Test directory exclusions
```

### 3. GitHub Actions Workflows

#### Code Quality Workflow (`.github/workflows/code-quality.yml`)

Automatische checks op elke PR en push naar main:

1. **Linting Job**: Ruff checks voor code kwaliteit
2. **Type Checking Job**: MyPy voor type safety
3. **Style Check Job**: Flake8 voor style enforcement
4. **Security Job**: Bandit voor security issues
5. **Test Coverage Job**: Pytest met coverage reporting
6. **Pre-commit Job**: Alle pre-commit hooks

**Features:**
- Parallel execution voor snelle feedback
- Coverage reports naar Codecov
- Coverage badge generatie
- Gedetailleerde error reporting

#### Branch Naming Workflow (`.github/workflows/branch-naming.yml`)

Automatische validatie van branch names en PR titles:

**Toegestane branch patterns:**
```
feature/<TICKET>-beschrijving
hotfix/<TICKET>-beschrijving
bugfix/<TICKET>-beschrijving
release/X.Y.Z
```

**Vereisten:**
- Ticket nummer moet aanwezig zijn
- Lowercase beschrijving met hyphens
- PR titel moet ticket nummer bevatten

### 4. Logging Standaard (`hhnk_threedi_plugin/logging_config.py`)

Gestandaardiseerde logging configuratie:

```python
from hhnk_threedi_plugin.logging_config import get_logger

logger = get_logger(__name__)
logger.info("Processing started")
logger.debug("Debug info", extra={"user_id": 123})
```

**Features:**
- Centralized configuratie
- Consistent format
- Structured logging support
- File en console output
- Configureerbare log levels

### 5. Contributing Guidelines (`CONTRIBUTING.md`)

Uitgebreide documentatie voor developers:

- Development setup instructies
- Branch naming policy
- Code quality standards
- Testing requirements
- Commit message guidelines
- PR process
- Logging best practices

### 6. Improved .gitignore

Uitgebreide .gitignore voor:
- Python artifacts
- Virtual environments
- IDE bestanden
- Test coverage reports
- Logs
- Secrets en credentials
- Build artifacts

## Gebruik van de Tools

### Initial Setup

1. **Installeer development dependencies:**
```bash
pip install -e .[dev]
```

2. **Installeer pre-commit hooks:**
```bash
pre-commit install
```

3. **Test de setup:**
```bash
pre-commit run --all-files
```

### Dagelijks Gebruik

#### Voor het maken van een nieuwe branch:

```bash
# Correct formaat
git checkout -b feature/HHNK-123-add-new-feature

# Incorrect (zal worden afgewezen door CI)
git checkout -b add-new-feature
```

#### Voor het maken van een commit:

```bash
git add .
git commit -m "feat(auth): add user authentication"
# Pre-commit hooks worden automatisch uitgevoerd
```

Als pre-commit hooks falen:
- Bekijk de errors
- Fix de problemen (vaak automatisch gefixed door de hooks)
- Stage de changes opnieuw
- Commit opnieuw

#### Voor het maken van een Pull Request:

1. Zorg dat alle pre-commit hooks slagen
2. Zorg dat tests lokaal slagen:
```bash
pytest --cov=hhnk_threedi_plugin
```
3. Push naar GitHub
4. Maak PR met titel die ticket nummer bevat
5. Wacht op CI checks
6. Fix eventuele issues

### Running Tests

```bash
# Alle tests
pytest

# Met coverage
pytest --cov=hhnk_threedi_plugin --cov-report=html

# Specifieke test
pytest tests_htp/test_project.py

# Watch mode tijdens development
pytest-watch
```

### Running Linters Manually

```bash
# Ruff check en fix
ruff check . --fix
ruff format .

# MyPy type checking
mypy hhnk_threedi_plugin

# Flake8 style check
flake8 hhnk_threedi_plugin

# Bandit security check
bandit -r hhnk_threedi_plugin -c pyproject.toml

# Alle pre-commit hooks
pre-commit run --all-files
```

## CI/CD Pipeline

### Workflow Triggers

| Workflow | Trigger | Doel |
|----------|---------|------|
| Code Quality | Push to main, PR to main | Quality checks |
| Branch Naming | PR opened/updated | Policy enforcement |
| Build Docs | Push to main | Documentation |
| Release | Release created | Package creation |

### Quality Gates

Voor een PR om gemerged te worden:

1. ✅ Branch naam moet geldig zijn
2. ✅ PR titel moet ticket nummer bevatten
3. ✅ Alle linting checks moeten slagen
4. ⚠️ Type checking mag warnings hebben (continue-on-error)
5. ⚠️ Style checks mogen warnings hebben (continue-on-error)
6. ✅ Security checks moeten slagen
7. ⚠️ Tests moeten minimaal 70% coverage hebben
8. ✅ Minimaal 1 approving review

### Coverage Reporting

Coverage wordt gerapporteerd naar:
- PR comments (via Codecov)
- HTML report in `htmlcov/`
- XML report voor externe tools
- Badge in README (op main branch)

## Volgende Stappen

### Onmiddellijk

1. **Tests toevoegen**: Verhoog coverage naar minimaal 70%
   ```bash
   pytest --cov=hhnk_threedi_plugin --cov-report=html
   # Bekijk htmlcov/index.html voor uncovered code
   ```

2. **Type hints toevoegen**: Voeg geleidelijk type hints toe aan bestaande code
   ```python
   def calculate(value: float, factor: int) -> float:
       return value * factor
   ```

3. **Logging implementeren**: Vervang print statements door proper logging
   ```python
   from hhnk_threedi_plugin.logging_config import get_logger
   logger = get_logger(__name__)
   logger.info("Processing started")
   ```

4. **Docstrings toevoegen**: Gebruik NumPy style docstrings
   ```python
   def process_data(data: list[float]) -> float:
       """
       Process data and return average.

       Parameters
       ----------
       data : list[float]
           Input data to process

       Returns
       -------
       float
           Average of input data
       """
       return sum(data) / len(data)
   ```

### Korte Termijn (1-2 sprints)

1. **Hardcoded waarden refactoren**:
   - Identificeer hardcoded paden, URLs, configuratie
   - Verplaats naar configuratie bestand of environment variabelen
   - Gebruik pathlib voor paden

2. **Coverage verhogen naar 80%**:
   - Focus eerst op kritieke modules
   - Voeg integration tests toe
   - Gebruik fixtures voor herbruikbare test data

3. **SIG Code Quality Meting**:
   - Baseline meting uitvoeren
   - Verbeterpunten identificeren
   - Target score bepalen

### Middellange Termijn (3-6 maanden)

1. **Pixi.toml synchroniseren**:
   - Dependencies in sync brengen met pyproject.toml
   - Documenteren welke tool waarvoor gebruikt wordt

2. **Release strategie**:
   - Implementeer semantic versioning
   - Kleinere, frequentere releases
   - Automated release notes

3. **Documentation**:
   - API documentatie genereren met Sphinx
   - Docstring coverage verhogen naar 100%
   - Architecture documentation

4. **Performance monitoring**:
   - Profiling van kritieke functies
   - Performance benchmarks
   - Optimization waar nodig

## Metrics & KPIs

### Code Quality Metrics

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Test Coverage | Unknown | 80% | ⚠️ Setup |
| Type Coverage | ~0% | 60% | ⚠️ Config ready |
| Docstring Coverage | ~30% | 100% | ⚠️ Style set |
| Security Issues | Unknown | 0 | ✅ Scanner active |
| Python Version | Various | 3.11+ | ✅ Required |
| Branch Naming Compliance | ~50% | 100% | ✅ Enforced |

### Process Metrics

| Metric | Current | Target |
|--------|---------|--------|
| Release Frequency | Quarterly | Monthly |
| PR Size | Large | Small (<500 lines) |
| PR Review Time | Unknown | <2 days |
| CI Build Time | N/A | <10 min |

## Resources

### Documentation
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pre-commit Documentation](https://pre-commit.com/)

### Internal
- [CONTRIBUTING.md](CONTRIBUTING.md) - Development guidelines
- [pyproject.toml](pyproject.toml) - Project configuration
- [.pre-commit-config.yaml](.pre-commit-config.yaml) - Hook configuration

## Vragen & Support

Voor vragen over code quality improvements:
1. Check eerst [CONTRIBUTING.md](CONTRIBUTING.md)
2. Check de GitHub Actions logs voor specifieke errors
3. Open een issue met het label `code-quality`
4. Contact het development team

## Change Log

| Datum | Wijziging | Door |
|-------|-----------|------|
| 2025-10-29 | Initial code quality setup | Claude |
| | Pre-commit hooks toegevoegd | |
| | GitHub Actions workflows gemaakt | |
| | Documentatie toegevoegd | |
