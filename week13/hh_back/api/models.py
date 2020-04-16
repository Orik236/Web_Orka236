from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=200)
    address = models.TextField()

    def short(self):
        return {
            'Name': self.name,
            'City': self.city
        }

    def to_json(self):
        return {
            'Company Name': self.name,
            'Description': self.description,
            'City': self.city,
            'Address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)

    def short(self):
        return {
            'Name': self.name,
            'Salary': self.salary
        }

    def to_json(self):
        return {
            'Name': self.name,
            'Description': self.description,
            'Salary': self.salary,
            'Company': self.company.name
        }