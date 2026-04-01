# Lore Data Platform

An interactive Python-based data platform for exploring character, region, and vanguard data from JSON and database sources. This project demonstrates modular design, scalable backend architecture, and clean code practices suitable for a hireable-level SWE portfolio.

---

## Project Overview

**Lore Data Platform** allows users to:

- Search and filter characters, regions, and vanguards
- Query data via modular Python functions or API endpoints
- Work with both JSON and SQL-based data sources
- Easily extend functionality with new modules or datasets

The goal of this project is to demonstrate proficiency in:

- Python programming and file I/O
- Data structures and modular design
- Backend architecture with RESTful API support
- Data validation, error handling, and logging
- Building maintainable and scalable systems

---

## Folder Structure

```text
LoreDataPlatform/
├─ data/                # Example datasets (JSON/CSV)
├─ modules/             # Core project modules
│  ├─ data_model.py     # Data ingestion, validation, storage
│  ├─ services.py       # Query logic and business rules
│  ├─ api.py            # REST API endpoints
│  └─ utils.py          # Helper functions (formatting, logging)
├─ tests/               # Unit and integration tests
├─ .gitignore           # Excludes venv/, __pycache__, etc.
├─ README.md
└─ requirements.txt     # Project dependencies
