from django.db import models
from django.db import models
from django.contrib.auth.models import User




class CustomUser(User):
    phone_number = models.CharField(max_length=13,
                                     verbose_name='укажите номер телефона', 
                                    default='+996')
    GENDER = (
        ('M', "M"),
        ('F', "F"),
        ('Unknown',  'Unknown')
    )
    gender = models.CharField(max_length=100, choices=GENDER, default='Unknown')
    city = models.CharField(max_length=100, default='Bishkek')

    def __str__(self):
        return self.username
