
from django.urls import path
# from courses.views.homepage import home
# from  .views import home
from courses.views import home,coursePage
from django.conf.urls.static import static
from online_courses.settings import MEDIA_ROOT,MEDIA_URL
from django.conf import settings



urlpatterns = [
    
    path('', home, name='home'),
    path('course/<str:slug>', coursePage, name='coursepage'),
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=MEDIA_ROOT)

