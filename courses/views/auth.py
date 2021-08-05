from django.shortcuts import render, redirect
from courses.models import Course, Video
from django.shortcuts import HttpResponse
from courses.forms import RegistrationForm, LoginForm
from django.views import View
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView

class SignupView(FormView):
    template_name="courses/signup.html"
    form_class = RegistrationForm
    success_url ='/login'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name="courses/login.html"
    form_class = LoginForm
    success_url ='/'
    def form_valid(self, form):
        print("Form is valid--------",form.cleaned_data)
        login(self.request, form.cleaned_data)
        return super().form_valid(form)


'''
class SignupView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, template_name="courses/signup.html", context= {'form':form})
   
        
    def post(self, request):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
        # print(user.first_name)
        # print(user.last_name)
        # print(user.email)
            if (user is not None):
                return redirect('login')
        return render(request, template_name="courses/signup.html", context= {'form':form})
   
'''        

   
'''  
class LoginView(View):
   
    def get(self, request):
        # print("************")

        form = LoginForm()
        
        return render(request, template_name="courses/login.html", context= {'form':form})
       
    def post(self, request):
        form = LoginForm(request = request, data = request.POST)
        # print(form.is_valid())
        if(form.is_valid()):
            return redirect('home')
        return render(request, template_name="courses/login.html", context= {'form':form})
        # return redirect('home')




'''
def signout(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect("home")