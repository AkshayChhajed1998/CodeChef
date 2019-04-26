import os
import django
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE','codechef.settings')
# settings.configure()
django.setup()
from questions.models import Questions
fields=['question']
for row in csv.reader(open('complete_round_1.csv'),delimiter='\n'):
	Questions.objects.create(**dict(zip(fields,row)))
