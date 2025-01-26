"""prot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""





# from django.contrib.auth.views import LoginView
# from .views import package_detail_view

    # url(r'^$', views.index_redirect, name='index_redirect'),

    

    # url(r'^packages/$', package_detail_view.as_view(template_name='package.html'),name="login"),
    # url(r'^logout/$', auth_views.logout, name='logout'),

    

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Example home page route
    path('admin/', admin.site.urls),    # Correct admin import and URL
    path('myapp/', include('myapp.urls')),
]
