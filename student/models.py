from django.db import models
# from management.models import Room
# Create your models here.

# class Resources(models.Model):
#     water = models.CharField(max_length=10,verbose_name='水费')
#     electricity = models.CharField(max_length=20,verbose_name ='电费')
#     room = models.ForeignKey(to=Room,verbose_name='宿舍号',on_delete=models.CASCADE)
#     def __str__(self):
#         return self.room
#     class Meta:
#         verbose_name = '水电'
#         verbose_name_plural = '水电'
