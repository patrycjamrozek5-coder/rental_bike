# Bike Rental

A simple Django app that reads bike data from `bikes/bikes.json` and shows how many bikes are available and what their names are. If no bikes are available, the page displays a message.

## Run locally on Windows

Open PowerShell in the project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "Django~=5.2.0"
python manage.py runserver
```

Open [http://127.0.0.1:8000/bikes/](http://127.0.0.1:8000/bikes/) in your browser.
