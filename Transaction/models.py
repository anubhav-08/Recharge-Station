from django.db import models
from django.contrib.auth import get_user_model

from Plan.models import Plan
User = get_user_model()
# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    plan = models.ForeignKey(to=Plan, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    mobile_no = models.CharField(max_length=13)

    def __str__(self):
        return self.mobile_no + " for amount of " + str(self.amount)