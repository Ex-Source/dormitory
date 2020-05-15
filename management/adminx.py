import xadmin
from .models import Student, Room,Building,Mistake
from xadmin import views


# Register your models here.
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "宿舍后台管理系统"  # 设置头标题
    site_footer = "source "  # 设置脚标题 (设置底部关于版权信息)
    # 设置菜单缩放
    menu_style = "accordion"  # 设置菜单样式


class StudentAdmin(object):
    is_execute = True
    list_display = ('student_name', 'student_id', 'student_sex', 'student_building', 'student_room')
    search_fields = ['student_id']


class RoomAdmin(object):
    is_execute = True
    list_display = ('room_id', 'room_building','room_water','room_electricity')
    search_fields = ['room_id']

class MistakeAdmin(object):
    is_execute = True
    list_display = ('mistake_id','case','date')
    search_fields = ['mistake_id']

class BuildingAdmin(object):
    is_execute = True
    search_fields = ['building_name']


xadmin.site.register(Mistake,MistakeAdmin)
xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Room, RoomAdmin)
xadmin.site.register(Building,BuildingAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
