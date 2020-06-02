from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=10)
    subject = models.CharField(max_length=80)
    degree = models.ForeignKey('Degree', on_delete=models.CASCADE)


class Degree(models.Model):
    code =  models.CharField(max_length=10)
    name =  models.CharField(max_length=20)

    def __str__(self):
        return self.name
