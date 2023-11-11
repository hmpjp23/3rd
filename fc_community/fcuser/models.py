from django.db import models

# Create your models here.


class Fcuser(models.Model):  # 객체
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True,  verbose_name='등록시간')  # 현재 시간 자동 등록

    class Meta:
        db_table = 'fastcampus_fcuser'
