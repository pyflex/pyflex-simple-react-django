from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    user_email = models.EmailField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'Employee'
