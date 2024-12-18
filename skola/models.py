from django.db import models

class Student(models.Model):
    meno = models.CharField(max_length=20) # textove pole 
    priezvisko = models.CharField(max_length=20)
    trieda = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.meno} {self.priezvisko}, {self.trieda}"
