from django.shortcuts import render, redirect
from courses.models import Course, Video, UserCourse
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='login'), name='dispatch')
class MyCoursesList(ListView):
    template_name = 'courses/my_courses.html'
    queryset = UserCourse.objects.all()
    context_object_name = 'user_courses'

    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)



'''
@login_required(login_url="login")
def my_courses(request):
    user = request.user
                
    user_courses = UserCourse.objects.filter(user=user)
    context = {
        'user_courses' : user_courses
    }

    
    return render(request=request, template_name="courses/my_courses.html", context=context)
'''

def coursePage(request,slug):
    course = Course.objects.get(slug = slug)
    # print(type(course))
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    # print(type(videos))
    # courses = Course.objects.all()
    # print(course,serial_number)
    next_lecture = 2
    prev_lecture = None;
    if serial_number is None:
        serial_number = 1
    else:
        next_lecture = int(serial_number)+1
        if len(videos) < next_lecture:
            next_lecture = None


        prev_lecture = int(serial_number)-1
        


    # video = Video.objects.filter(serial_number=serial_number, course=course)
    video = Video.objects.filter(serial_number=serial_number).filter(course=course).first()
    # print(type(video))
    if video==None:
        # print("heyyyyyyyyyyyyyyyyyyyyyy")
        pass
        # print(video1)
        
        # print(type(video)) 
    else:
        # print("Preview Video", video.is_preview)
        # print("course Authentication", request.user.is_authenticated)

        # ***************************
        if(video.is_preview is False):
            if request.user.is_authenticated is False:
                return redirect('login')
                # ******************************
            else:
                user = request.user
                try:
                    user_course = UserCourse.objects.get(user=user, course=course)
                except:
                    return redirect("check-out", slug=course.slug)


    context = {
    "course" : course,
    "video" :video,
    "next_lecture" :next_lecture,
    "prev_lecture" :prev_lecture,
    "videos":videos
    }
    return render(request, template_name="courses/course_page.html", context=context)
        