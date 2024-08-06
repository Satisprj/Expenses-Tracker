from django.db import models

# Create your models here.
class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
    