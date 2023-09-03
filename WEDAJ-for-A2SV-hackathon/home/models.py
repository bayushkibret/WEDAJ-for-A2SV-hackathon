from django.db import models

# Create your models here.
class advice_history(models.Model):
    user = models.CharField(max_length = 255)
    postive_cash_flow = models.IntegerField()
    total_savings = models.IntegerField()
    total_return = models.IntegerField()
    total_income = models.IntegerField()
    total_expenditure = models.IntegerField()
    simple_interest_earned = models.IntegerField()
    advice = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{} ({})'.format(self.user, self.created_date)