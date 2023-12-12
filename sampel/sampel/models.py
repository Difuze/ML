# recommendation/models.py

from django.db import models

class UserInput(models.Model):
    online_order = models.CharField(max_length=10)
    book_table = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    type1 = models.CharField(max_length=100)
    votes = models.IntegerField()
    cost = models.IntegerField()
    rest_type_count = models.IntegerField()
