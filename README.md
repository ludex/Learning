# Learning

## Python environment

The root dependency snapshot targets Python 3.10. Recreate it locally instead
of committing a virtual environment:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Keep credentials in ignored local `.env` files and commit only placeholder-only
`.env.example` templates.
