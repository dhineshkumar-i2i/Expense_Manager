from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    created_by = models.IntegerField(default=None, null=True)
    created_at = models.DateTimeField(format('%d-%m-%Y %H:%M:%S'),
                                      auto_now_add=True,)
    updated_by = models.IntegerField(default=None, null=True)
    updated_at = models.DateTimeField(format('%d-%m-%Y %H:%M:%S'),
                                      auto_now=True)
