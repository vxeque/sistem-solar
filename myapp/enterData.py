import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")

django.setup()

from myapp.models import TestSistemSolar

def get_Data(): 
    return TestSistemSolar.objects.all()

