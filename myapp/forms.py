
from django import forms


class Customersignup(forms.Form):
    uname = forms.CharField(max_length=100)  # Matches name="uname" in HTML
    email = forms.EmailField()  # Matches name="email"
    psw = forms.CharField(widget=forms.PasswordInput())  # Matches name="psw"
    pswrepeat = forms.CharField(widget=forms.PasswordInput())  # Matches name="pswrepeat"




class Contactus(forms.Form):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)


class Loginform(forms.Form):
    uname = forms.CharField(max_length=150, label="Username")
    psw = forms.CharField(widget=forms.PasswordInput, label="Password")