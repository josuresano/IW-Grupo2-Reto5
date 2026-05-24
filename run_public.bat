@echo off
start cmd /k "python manage.py runserver"
rem Aumentamos el tiempo de 3 a 5 segundos ya que hay ocasiones en las que ngrok tarda mas que django en ejecutarse y si intentas acceder en ese momento a la web dara error
timeout /t 5 /nobreak >nul
start cmd /k "ngrok http 8000"
