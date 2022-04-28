from django.core.validators import MinValueValidator
from django.db import models

from category.models import Category
from user.models import UserDetails


class Ledger(models.Model):
    EXPENSE_TYPE = (
        ('Expense', 'Expense'),
        ('Income', 'Income')
    )
    name = models.CharField(max_length=100)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])
    category = models.ForeignKey(Category, related_name='ledger',
                                 on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=EXPENSE_TYPE,
                            default='Expense')
    created_by = models.IntegerField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField(default=None, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    #user = models.ForeignKey(
    #    UserDetails, related_name='ledger', on_delete=models.CASCADE)
    is_shared = models.BooleanField(default=False)
    total_amount = models.FloatField(default=0,
                                     validators=[MinValueValidator(0.0)])
    users = models.ManyToManyField(UserDetails,
                                   related_name='ledger')


def __str__(self):
    return 'Name: {} Amount: {}'.format(self.name, self.amount)
