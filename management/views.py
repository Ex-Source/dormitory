from django.views.generic.base import View
from .models import Room
from django.core import serializers
from django.http import JsonResponse


# 二级联动View函数
class SelectView(View):
    def get(self, request):
        # 通过get得到父级选择项
        typeparent_id = request.GET.get('module', '')
        # 筛选出符合父级要求的所有子级，因为输出的是一个集合，需要将数据序列化 serializers.serialize（）
        typesons = serializers.serialize("json", Room.objects.filter(room_building=int(typeparent_id)))
        # 判断是否存在，输出
        if typesons:
            return JsonResponse({'typeson': typesons})
