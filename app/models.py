from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female')))
    edu_level = models.IntegerField()
    class Meta:
        db_table = 'person'
