import xadmin
from .models import User
class UserAdmin():
    list_display = ['uid','name']
    search_fields =['uid']

xadmin.site.register(User,UserAdmin)

