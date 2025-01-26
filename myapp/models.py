# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.db import models

# # Create your models here.

# class webpage(models.Model):
#     name = models.CharField(max_length=20)
#     Email = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     repassword = models.CharField(max_length=20)

#     class Meta:
#         db_table = 'Web'
# class contact(models.Model):
#     fullname = models.CharField(max_length=20)
#     Email = models.CharField(max_length=20)
#     msg = models.CharField(max_length=20)


#     class Meta:
#         db_table = 'contact'



# class package(models.Model):
#          title=models.CharField(max_length=100)
#          description=models.CharField(max_length=500)
#          price=models.CharField(max_length=50)
#          summary=models.TextField(blank=True,null=True)

# from django.db import models

# # Webpage Model - User Registration (Consider using Django's User model for authentication)
# class Webpage(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)  # Use EmailField for validation
#     password = models.CharField(max_length=128)  # Password should be hashed (use Django's built-in password system)
#     repassword = models.CharField(max_length=128)  # This should match 'password' field, used for validation

#     class Meta:
#         db_table = 'web'

#     def __str__(self):
#         return self.name

# # Contact Model - Stores contact form submissions
# class Contact(models.Model):
#     fullname = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     msg = models.TextField()  # Use TextField for longer messages

#     class Meta:
#         db_table = 'contact'

#     def __str__(self):
#         return self.fullname

# # Package Model - Travel Packages
# class Package(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()  # Use TextField for detailed descriptions
#     price = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for accurate price storage
#     summary = models.TextField(blank=True, null=True)  # Optional field for additional summary

#     class Meta:
#         db_table = 'package'

#     def __str__(self):
#         return self.title
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from decimal import Decimal



class Webpage(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Username field
    email = models.EmailField(unique=True)  # Email field
    password = models.CharField(max_length=255)  # Password field (hashed password stored)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.password:
            self.password = make_password(self.password)
        super(Webpage, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(default='default@example.com') 
    msg = models.TextField()

    def __str__(self):
        return self.fullname
# In models.py




