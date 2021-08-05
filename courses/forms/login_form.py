from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError

class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=95, required = True, label='Email Address')
    # print("*********4555*************")
    # print(username)
    class Meta:
        model = User
        fields =['email','password']

    

    def clean(self):
        # print("1111111111222222222222222222")
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None

        try:
            user = User.objects.get(email=email)
            result = authenticate(username = user.username, password=password)
            if(result is not None):
                # login(self.request, result)
                return result
            else:
                raise ValidationError("Email or Password invalid")
        except:
            raise ValidationError("Email or Password invalid")







    