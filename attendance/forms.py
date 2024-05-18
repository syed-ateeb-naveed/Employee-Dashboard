from django import forms

class LoginForm(forms.Form):
    emp_dig_id = forms.CharField(label="Employee Digital ID", max_length=25)
    emp_password = forms.CharField(label="Password", max_length=128, widget=forms.PasswordInput)