from django import forms
from django.contrib.auth.models import User, Permission
from django.forms import fields, ModelForm
from .models import UserProfile, Tutors, GeeksModel, Student


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutors
        fields = "__all__"

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password1 = forms.CharField(label = 'Repeat password', widget = forms.PasswordInput)


    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password1']:
                raise forms.ValidationError('password don`t match')
            return cd['password1']
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('disciple', 'level')
        
class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    
    
class GeeksForms(ModelForm):
    class Meta:
        model = GeeksModel
        fields = "__all__"

class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  
        
        
class NameForm(forms.Form):
    your_name = forms.CharField(label = 'Your name', max_length=100)
    age = forms.IntegerField(label = 'age')
        
        

        
