"""samsung URL Configurationmyapp/urls.py

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






from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Authentication Views
    path('index/', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.loginforms, name='loginforms'),
    path('logout/', views.logout_view, name='logout'),

    # Functional Views
    path('gallery/', views.gallery, name='gallery'),
    path('contact1/', views.contact1, name='contact1'),
    path('loggedin/', views.loggedin, name='loggedin'),
    path('register/', views.signin, name='signin'),
    path('login/', views.loginforms, name='login'),
    
    path('logout/', views.logout_view, name='logout'),  # Rename the second to 'logout' instead of 'loggedin'
   # myapp/urls.py

    
     path('hotdeals/', views.hot_deals_view, name='hot_deals'), 
      path('contact/', views.contact_us_view, name='contact_us'), 
     
      


    


    # Static Pages Using TemplateView
    # path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('varanasi/', TemplateView.as_view(template_name='varanasi.html'), name='varanasi'),
    path('manali/', TemplateView.as_view(template_name='manali.html'), name='manali'),
    path('kashmir/', TemplateView.as_view(template_name='kashmir.html'), name='kashmir'),
    path('rajasthan/', TemplateView.as_view(template_name='rajasthan.html'), name='rajasthan'),
    path('hotdeals/', TemplateView.as_view(template_name='hotdeals.html'), name='hotdeals'),
    path('payment/', TemplateView.as_view(template_name='payment.html'), name='payment'),
    path('package/', TemplateView.as_view(template_name='package.html'), name='package'),


    # Region-Specific Pages (URL-Friendly Names)
    # path('south-india/', TemplateView.as_view(template_name='south.html'), name='south_india'),
    path('north/', TemplateView.as_view(template_name='north.html'), name='north'),
    path('north-east/', TemplateView.as_view(template_name='northeast.html'), name='north_east'),
    path('goa/', TemplateView.as_view(template_name='goa.html'), name='goa'),

    # Destination Pages
    path('rajasthan_lo/', TemplateView.as_view(template_name='rajasthan_lo.html'), name='rajasthan_lo'),
    path('varanasi_lo/', TemplateView.as_view(template_name='varanasi_lo.html'), name='varanasi_lo'),
    path('manali_lo/', TemplateView.as_view(template_name='manali_lo.html'), name='manali_lo'),
    path('kashmir_lo/', TemplateView.as_view(template_name='kashmir_lo.html'), name='kashmir_lo'),

    # Contact for Logged-Out Users
    path('contact_lo/', TemplateView.as_view(template_name='contact.html'), name='contact_lo'),

    # Base Template
    path('base/', TemplateView.as_view(template_name='base.html'), name='base'),
     path('<str:location>/', views.location_view, name='location_view'),
]
