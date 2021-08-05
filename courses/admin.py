from django.contrib import admin

# Register your models here.
from courses.models import Course, Tag, Prequisite, Learning, Video,UserCourse,Payment

class TagAdmin(admin.TabularInline):
    model = Tag

class VideoAdmin(admin.TabularInline):
    model = Video

class PrequisiteAdmin(admin.TabularInline):
    model = Prequisite
class LearningAdmin(admin.TabularInline):
    model = Learning

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, PrequisiteAdmin, LearningAdmin, VideoAdmin]
admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment)
admin.site.register(UserCourse)
