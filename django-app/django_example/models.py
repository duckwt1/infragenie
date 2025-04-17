from django.db import models
from django_example.views.business import get_business_name

class Business(models.Models):
    pass
    def __str__(self):
        return get_business_name()



