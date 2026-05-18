import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Control_Calidad_Industria.settings')
django.setup()

from django.core.management import call_command
with open('backup_datos.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', '--natural-foreign', '--natural-primary',
                 '--exclude=contenttypes', '--exclude=auth.permission',
                 stdout=f)
print("Exportación completada")