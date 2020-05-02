from django import forms 

class RegisterLender(forms.Form):
    First_Name = forms.CharField(max_length=50)
    Last_Name = forms.CharField(max_length=50)
    Email = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=15)
    Money = forms.IntegerField(min_value=0, max_value=9999999)

class RegisterBorrow(forms.Form):
    First_Name = forms.CharField(max_length=50)
    Last_Name = forms.CharField(max_length=50)
    Email = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=15)
    Subject = forms.CharField(max_length=50)
    Description = forms.CharField(widget=forms.Textarea)
    Money_Need = forms.IntegerField(min_value=0, max_value=9999999)
