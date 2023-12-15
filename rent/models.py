from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    item_id = models.TextField(primary_key=True)
    item_description = models.TextField()
    item_state = models.IntegerField()

class Loan(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_loan = models.DateField()
    loan_due_date = models.DateField()
    loan_is_finished = models.BooleanField()
