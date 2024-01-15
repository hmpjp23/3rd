from django.db import models

# Create your models here.


class Fcuser(models.Model):  # 객체
    username = models.CharField(max_length=32, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True,  verbose_name='등록시간')  # 현재 시간 자동 등록
    

    def __str__(self): #class를 문자열로 변환할때 내장 함수인 __str__를 호출한다. 이를 이용해서 return을 정의해줌
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'
