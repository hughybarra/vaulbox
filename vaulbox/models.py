from django.db import models

#Vaulbox Members
class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length =30)
    user_email = models.CharField(max_length= 100)
    user_password = models.CharField(max_length=100, unique=True)
    
