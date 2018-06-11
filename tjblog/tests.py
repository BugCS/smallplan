from django.test import TestCase

# Create your tests here.
import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smallplan.settings")
django.setup()
