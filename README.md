# sunlight
Visualise the sun's positioning over the day or year.

## Developer Information

### Install requirements
```
python3 -m venv var/venv
source var/venv/bin/activate     # Activate it (Linux/macOS)
var\venv\Scripts\activate        # On Windows

pip install -r requirements.txt
```

#### Update
```
pip install new_package
pip freeze > requirements.txt
```


### Folder Structure
```
sunlight/
├── bin/              # Startup scripts, CLI entry points (e.g., `start.sh`, `manage.py`)
├── etc/              # Configuration files
│   ├── default/      # Default config (e.g., `app.conf`, `logging.conf`)
│   └── local/        # Local/overrides not in repository (e.g., for dev or prod secrets)
├── src/              # Actual server code
│   └── your_app/     # App logic, routes, models, services, etc.
├── lib/              # Optional: custom libraries or extensions
├── var/              # Runtime files (e.g., cache, temporary uploads)
├── logs/             # Runtime logs (if stored locally)
├── static/           # Static files if needed (CSS, JS, etc.)
├── tests/            # Unit/integration tests
├── docs/             # Documentation
└── requirements.txt  # Or `pyproject.toml` if using Poetry
```

Put it in bin/: for example bin/run_server.py or bin/start.sh
This makes the intention clear: bin/ = things you can run

Example:

```
# bin/start.sh
#!/bin/bash
python3 -m src.your_app
```
