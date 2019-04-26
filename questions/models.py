from django.db import models

# Create your models here.
class Questions(models.Model):
    question_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=500)
    question_is_active=models.BooleanField(default=True)
    language_option=models.BooleanField(default=True)
    
    
    def __str__(self):
        return '{} {}'.format(self.question_id,self.question)
        