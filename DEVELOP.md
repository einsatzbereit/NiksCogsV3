# Development

## Windows

[Documentation](https://docs.discord.red/en/stable/install_windows.html)

```bash
python -m venv "%userprofile%\redenv"
"%userprofile%\redenv\Scripts\activate.bat"
"%userprofile%\redenv\Scripts\deactivate.bat"

redbot-setup

redbot olaf --dev --owner 258262622976212993  #--disable-intent presences
```

## Locales

```bash
pip install regettext
python -m redgettext -D <file>
```

* Open messages.pot with [Poedit](https://poedit.net/)

## Refactor

```bash
#black
python -m black . --line-length=120
#pep8
python -m pyflakes .
```
