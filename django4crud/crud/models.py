from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.BigAutoField(primary_key=True)
    name= models.CharField(max_length=25, blank=False, null=False)
    age=models.IntegerField()
    major= models.CharField(max_length=25, blank=False, null=False)
    gender=models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.name
        