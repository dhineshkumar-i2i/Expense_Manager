from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class UserDetails(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(18)
    ])
    phone_number = models.BigIntegerField(validators=[
        RegexValidator(
            regex='^[789]\d{9}$',
            message='Phone number must be 10 digits',
            code='invalid_number'
        ),
    ])
    salary = models.FloatField(validators=[MinValueValidator(0.0)])
    email = models.EmailField()
    created_by = models.IntegerField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_by = models.IntegerField(default=None, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Name : {} Id: {}'.format(self.name, self.pk)
