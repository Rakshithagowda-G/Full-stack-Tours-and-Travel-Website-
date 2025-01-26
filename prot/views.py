# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Assuming you have a 'home.html' template


# Create your views here.
