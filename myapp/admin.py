# -*- coding: utf-8 -*-
# 
from django.contrib import admin
from .models import Webpage, Contact
# Register the models with the admin site
admin.site.register(Webpage)
admin.site.register(Contact)

