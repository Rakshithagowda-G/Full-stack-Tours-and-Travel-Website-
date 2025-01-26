# from __future__ import unicode_literals

# from django.shortcuts import render,redirect
# from myapp.forms import *
# from django.http import HttpResponse, HttpResponseRedirect
# from myapp.models import *
# import sqlite3

# def signin(request):
#     data=Customersignup(request.GET)
#     if data.is_valid():
#         username = data.cleaned_data['uname']
#         emailid = data.cleaned_data['email']
#         password = data.cleaned_data['psw']
#         repassword = data.cleaned_data['pswrepeat']
#         e=Webpage(name=username,Email=emailid,password=password,repassword=repassword)
#         # request.session["name"]=e.name
#         # request.session["password"]=e.password
#         e.save()
#         # def logout():
#         #     try:
#         #         del request.session.name
#         #         del request.session.password
#         #     except:
#         #         pass
#         # logout()
#     # return render(request,'travelworld/userinterface.html',{})
#     # return HttpResponseRedirect("login.html")

#     return render(request,'register.html',{})
# def contact1(request):
#     data=contactus(request.GET)
#     if data.is_valid():
#         fullname = data.cleaned_data['fullname']
#         Email = data.cleaned_data['Email']
#         msg = data.cleaned_data['msg']

#         e=Contact(fullname=fullname,Email=Email,msg=msg)
#         # request.session["name"]=e.name
#         # request.session["password"]=e.password
#         e.save()
#     return render(request, 'contact.html', {})
# def loginforms(request):
#     if request.method=="GET":
#         data = Loginform(request.GET)
#     try:
#         if data.is_valid():
#             u = data.cleaned_data['uname']
#             p = data.cleaned_data['psw']
#             user = Webpage.objects.get(name=u, password=p)

#             if u == user.name and p == user.password:
#                 request.session["name"] = user.name
#                 request.session["password"] = user.password
#                 # return  HttpResponse("suucess..")
#                 # return HttpResponse("")
#             # return HttpResponseRedirect("loggedin.html")
#             # return HttpResponseRedirect('/prot/loggedin')

#             return redirect(request, "/prot/loggedin.html/", {})

#     except:
#         return render(request, "loggedin.html", {})
# #
# # def loginforms(request):
# #         if request.method == "GET":
# #             data = Loginform(request.GET)
# #
# #             if data.is_valid():
# #                 u = data.cleaned_data['uname']
# #                 p = data.cleaned_data['psw']
# #                 user = webpage.objects.get(name=u, password=p)
# #
# #                 if u == user.name and p == user.password:
# #                     request.session["name"] = user.name
# #                     request.session["password"] = user.password
# #                     # return  HttpResponse("suucess..")
# #                     # return HttpResponse("")
# #                 return HttpResponseRedirect("loggedin.html")
# #                 # return HttpResponseRedirect('/prot/loggedin')
# #
# #                 # return redirect(request, "loggedin.html", {})
# #
# #         else:
# #             return HttpResponseRedirect("loggedin.html")
# #
# #             # return render(request, "loggedin.html", {})


# # def loginforms(request):
# #     if request.method == "GET":
# #         form = Loginform(request.GET)
# #         if form.is_valid():
# #             try:
# #                 return redirect('loggedin.html')
# #             except:
# #                 pass
# #         else:
# #             form = Loginform()
# #     return render(request, 'index.html', {'form': form})

#         # return render(request,"travelagency/loginform.html",{})
#             # else:

#             #     request.session["error"] = "error"
#             #     e = 'error'
#             #     return render(request, "travelagency/loginform.html")
#             # if u == 'Admin' and p == 'admin123':
#             #     request.session["name"]='Admin'
#             #     request.session["password"]='admin123'
#             #     details = webpage.objects.all()
#             #     userdetails = Userdetais.objects.all()
#             #     return render(request,"travelworld/Admin.html",{'detail':details,'userdetail':userdetails})


#                 # return render(request,"travelagency/loginform.html")
# # def pacakgeview(request):
# #     pckg=addpackages.objects.all()
# #     context={'pckg':pckg}
# #     return render(request, 'travelagency/packages.html',context)
# def logout(request):
#     try:
#       del request.session["name"]


#     except:
#         pass
#     # return HttpResponse("<strong>You are logged out.</strong>")
#     return redirect('/myapp/login/')
#     # return render(request,'travelagency/index.html',{})


# # Create your views here.



# #
# # # -*- coding: utf-8 -*-
# # from __future__ import unicode_literals
# #
# # from myapp.forms import *
# # from django.http import HttpResponse, HttpResponseRedirect
# # from myapp.models import *
# # import sqlite3
# #
# #
# #
# # from django.shortcuts import render,redirect
# # from myapp.models import package
# #
# #
# #
# # def package_detail_view(request):
# #    obj=package.objects.get(id=1)
# #    context={
# #       'title':obj.title,
# #       'description':obj.description
# #    }
# #    return render(request,"package.html",context)
# #
# #
# #
# #
# # #
# # # def indexo (request):
# # #
# # #    members = Member.objects.all()
# # #    context={"members" :members}
# # #    return render (request,'contact.html',context)
# # #
# # #
# # # def contact (request):
# # #    member=Member(Name=request.POST['Name'],Email=request.POST['Email'],Message=request.POST['Message'])
# # #    member.save()
# # #    return redirect('/')
# #
# #
# # def contact1(request):
# #     data=contactus(request.GET)
# #     if data.is_valid():
# #         fullname = data.cleaned_data['fullname']
# #         Email = data.cleaned_data['Email']
# #         msg = data.cleaned_data['msg']
# #
# #         e=contact(fullname=fullname,Email=Email,msg=msg)
# #         # request.session["name"]=e.name
# #         # request.session["password"]=e.password
# #         e.save()
# #
# # # # def index(request):
# # # #    con=contactForm()
# # # #    return render(request,{'form':con})
# # # #
# # #
# # #
# # #
# # # def signin(request):
# # #    members=signups.objects.all()
# # #    context={"members" :members}
# # #    return render (request,'register.html',context)
# # #
# # # def register(request):
# # #    member=signups(username=request.POST['username'],Name=request.POST['Name'],Email=request.POST['Email'],Password=request.POST['Password'])
# # #    member.save()
# # #    return redirect('/')
# #
# #
# #
# # # from myapp.forms import LoginForm
# # #
# # # def login(request):
# # #    username="not logged in"
# # #
# # #    if request.method=="POST":
# # #       MyLoginForm=LoginForm(request.POST)
# # #
# # #       if MyLoginForm.is_valid():
# # #          username=MyLoginForm.cleaned_data['username']
# # #
# # #       else:
# # #          MyLoginForm=LoginForm()
# # #       return render (request,'loggedin.html',{"username":username})
# # #
# # #
# # #
# # #
# # #
# # #
# #
# from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password, check_password
# from .forms import Customersignup, Loginform, Contactus  # Assuming you have these forms
# from .models import Webpage, Contact
# from django.contrib.auth import logout

# def index(request):
#     return render(request, 'index.html') 
# # User Registration (Signin)

# def signin(request):
#     if request.method == 'POST':
#         data = Customersignup(request.POST)
#         if data.is_valid():
#             username = data.cleaned_data['uname']
#             emailid = data.cleaned_data['email']
#             password = data.cleaned_data['psw']
#             repassword = data.cleaned_data['pswrepeat']

#             # Check if passwords match
#             if password != repassword:
#                 return render(request, 'register.html', {'error': 'Passwords do not match'})

#             # Hash the password before saving
#             hashed_password = make_password(password)

#             # Save the new user data
#             e = Webpage(name=username, email=emailid, password=hashed_password)
#             e.save()

#             # Redirect to the login page after successful registration
#             return redirect('loginforms')  # Assuming you have a 'login' view set up

#     return render(request, 'register.html')


# # User Login
# def loginforms(request):
#     if request.method == "POST":
#         data = Loginform(request.POST)
#         if data.is_valid():
#             u = data.cleaned_data['uname']
#             p = data.cleaned_data['psw']

#             try:
#                 # Fetch user by name (or username)
#                 user = Webpage.objects.get(name=u)

#                 # Compare the entered password with the stored hashed password
#                 if check_password(p, user.password):
#                     # Set session variables on successful login
#                     request.session["name"] = user.name
#                     request.session["password"] = user.password
#                     return redirect('loggedin')  # Assuming you have a 'loggedin' view

#                 else:
#                     return render(request, 'login.html', {'error': 'Invalid username or password'})

#             except Webpage.DoesNotExist:
#                 return render(request, 'login.html', {'error': 'Invalid username or password'})

#     return render(request, 'login.html')


# # User Logout
# def logout_view(request):
#     logout(request)  # Django's built-in logout method
#     return redirect('loginforms')  # Updated to match the URL pattern name
# # Redirect to the login page after logout


# # Contact Form Submission
# def contact1(request):
#     if request.method == 'POST':
#         data = Contactus(request.POST)
#         if data.is_valid():
#             fullname = data.cleaned_data['fullname']
#             email = data.cleaned_data['Email']
#             msg = data.cleaned_data['msg']

#             # Save the contact form submission
#             e = Contact(fullname=fullname, email=email, msg=msg)
#             e.save()

#             return render(request, 'contact.html', {'message': 'Thank you for contacting us!'})

#     else:
#         data = Contactus()  # Render the empty form on GET request

#     return render(request, 'contact.html', {'form': data})
# def gallery(request):
#     return render(request, 'gallery.html') 
# def loggedin(request):
#     return render(request, 'loggedin.html') 

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout
from .forms import Customersignup, Loginform, Contactus
from .models import Webpage, Contact

def index(request):
    return render(request, 'index.html')

# def signin(request):
#     if request.method == 'POST':
#         data = Customersignup(request.POST)
#         if data.is_valid():
#             if data.cleaned_data['psw'] != data.cleaned_data['pswrepeat']:
#                 return render(request, 'register.html', {'error': 'Passwords do not match'})

#             Webpage.objects.create(
#                 name=data.cleaned_data['uname'],
#                 email=data.cleaned_data['email'],
#                 password=make_password(data.cleaned_data['psw'])
#             )
#             return redirect('loginforms')
#     return render(request, 'register.html')



def signin(request):
    if request.method == 'POST':
        print(request.POST)  # Debug: Print form data to verify it's being submitted
        data = Customersignup(request.POST)
        if data.is_valid():
            print("Form is valid")  # Debug: Check if form validation passes
            if data.cleaned_data['psw'] != data.cleaned_data['pswrepeat']:
                return render(request, 'register.html', {'error': 'Passwords do not match'})

            Webpage.objects.create(
                name=data.cleaned_data['uname'],
                email=data.cleaned_data['email'],
                password=make_password(data.cleaned_data['psw'])
            )
            print("Data saved successfully")  # Debug: Confirm save
            return redirect('loginforms')
        else:
            print("Form errors:", data.errors)  # Debug: Check validation errors
    return render(request, 'register.html')


# def loginforms(request):
#     if request.method == 'POST':
#         data = Loginform(request.POST)
#         if data.is_valid():
#             try:
#                 user = Webpage.objects.get(name=data.cleaned_data['uname'])
#                 if check_password(data.cleaned_data['psw'], user.password):
#                     request.session['name'] = user.name
#                     return redirect('loggedin')
#                 else:
#                     return render(request, 'login.html', {'error': 'Invalid credentials'})
#             except Webpage.DoesNotExist:
#                 return render(request, 'login.html', {'error': 'Invalid credentials'})
#     return render(request, 'login.html')
def loginforms(request):
    if request.method == 'POST':
        print("POST data:", request.POST)  # Print form data to check it's correct
        data = Loginform(request.POST)
        if data.is_valid():
            print("Cleaned data:", data.cleaned_data)  # Check cleaned data
            try:
                user = Webpage.objects.get(name=data.cleaned_data['uname'])
                if check_password(data.cleaned_data['psw'], user.password):
                    request.session['name'] = user.name
                    return redirect('loggedin')
                else:
                    return render(request, 'login.html', {'error': 'Invalid credentials'})
            except Webpage.DoesNotExist:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('loginforms')

def contact1(request):
    if request.method == 'POST':
        form = Contactus(request.POST)
        if form.is_valid():
            Contact.objects.create(
                fullname=form.cleaned_data['fullname'],
                email=form.cleaned_data['email'],
                msg=form.cleaned_data['msg']
            )
            return render(request, 'contact.html', {'message': 'Thank you for contacting us!'})
        else:
            print(form.errors)  # Debugging: print form errors
            return render(request, 'contact.html', {'form': form, 'error': 'Form validation failed'})
    else:
        form = Contactus()
    return render(request, 'contact.html', {'form': form})

def gallery(request):
    return render(request, 'gallery.html')

def loggedin(request):
    return render(request, 'loggedin.html')
from django.shortcuts import render

def contact_lo(request):
    return render(request, 'contact_lo.html')



def hot_deals_view(request):
    # Logic for displaying hot deals
    return render(request, 'hotdeals.html')
def contact_us_view(request):
    # Your logic for the contact us page
    return render(request, 'contact.html')
from django.shortcuts import render
from django.http import Http404

def location_view(request, location):
    locations = ['kashmir', 'manali', 'rajasthan', 'varanasi','south-india', 'north-east', 'rajasthan', 'goa','north','contact_lo']  # List of valid locations
    location = location.lower()  # Normalize to lowercase

    if location not in locations:
        raise Http404("Location not found")

    # Render a location-specific template or handle data dynamically
    return render(request, f'{location}.html', {'location': location})





