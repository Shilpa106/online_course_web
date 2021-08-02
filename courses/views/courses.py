from django.shortcuts import render
from courses.models import Course, Video
from django.shortcuts import HttpResponse

def coursePage(request,slug):
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    
    # courses = Course.objects.all()
    # print(course,serial_number)
    if serial_number is None:
        serial_number = 1

    # video = Video.objects.filter(serial_number=serial_number, course=course)
    video1 = Video.objects.filter(serial_number=serial_number).filter(course=course)

    # print(video1)
    vid_d = None
    video = None
    for vid in video1:
        vid_d=vid

    video=vid_d
    # print(video)


        # pass
        # print(video)
    context = {
    "course" : course,
    "video" :video,
    "videos":videos
    }
    return render(request, template_name="courses/course_page.html", context=context)
        # print(context)

        # v.append(video)
        # print(type(v))
        # print(v)
        # print(video)
    
    
    # a=v
    # print(a)
    # print(a[0])
    # v.append(video)
    # print(v)
    
    
    # for vid in video:
    #     # video1 = vid
        
    #     # print(vid)
    #     v.append[vid]
    #     print(v)
       
        # print(video1)

    # if serial_number is None:
    #     serial_number = 1


    # try:
    #     if serial_number is None:
    #         serial_number = 1

    # # user = UniversityDetails.objects.get(email=email)
    # except Exception as e:
    #     video = Video.objects.get(serial_number=serial_number, course=course)
    #     print(video)
    # video1 = Video.objects.get(course=course)
    # print(video)
    # context = {
    #     "course" : course,
    #     # "video1" :video
    # }
    # return render(request, template_name="courses/course_page.html", context=context)


    
    # return HttpResponse("Home Page")

