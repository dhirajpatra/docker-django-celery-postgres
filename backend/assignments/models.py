from django.db import models


# Create your models here.
class Assignment(models.Model):
    # first_term and second_term should be decimal numbers with max 5 digits and 2 decimal places
    # null and blank are set to False because they are required
    # sum should be equal to first_term + second_term
    first_term = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    second_term = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    
    # sum should be equal to first_term + second_term
    sum = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
