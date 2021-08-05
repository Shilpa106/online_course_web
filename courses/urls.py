
from django.urls import path
from courses.views.homepage import HomePageView
# from  .views import home
from courses.views import MyCoursesList, verifyPayment,coursePage, SignupView,LoginView,signout,checkout
from django.conf.urls.static import static
from online_courses.settings import MEDIA_ROOT,MEDIA_URL
from django.conf import settings



urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('logout', signout, name='logout'),
   
    path('my-courses', MyCoursesList.as_view(), name='my-courses'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('course/<str:slug>', coursePage, name='coursepage'),
    path('check-out/<str:slug>', checkout, name='check-out'),
    path('verify_payment', verifyPayment, name='verify_payment'),
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=MEDIA_ROOT)

