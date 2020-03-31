from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    descritpion = models.TextField()
    city = models.CharField(max_length=200)
    address = models.TextField()

class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company)