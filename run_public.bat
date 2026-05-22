@echo off
start cmd /k "python manage.py runserver"
timeout /t 5 /nobreak >nul
start cmd /k "ngrok http 8000"
