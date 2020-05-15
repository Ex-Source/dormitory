from django.contrib import admin
from .models import Student
from .models import Room
from .models import Building,Mistake


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_id', 'student_sex', 'student_building', 'student_room')
    search_fields = ['student_id']

class RoomInline(admin.TabularInline):
    model = Room
class BuildingAdmin(admin.ModelAdmin):
    inlines = [RoomInline]

admin.site.register(Mistake)
admin.site.register(Room)
admin.site.register(Student, StudentAdmin)
admin.site.register(Building,BuildingAdmin)
admin.site.site_header = '学生宿舍管理'
