from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10, unique=True)
    age = models.IntegerField(default=18)
    gender = models.BooleanField(default=1)
    # auto_now_add: 创建数据时，默认create_time字段为当前时间
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    # auto_now: 修改时间，每次update学生信息时，修改该字段的时间为当前时间
    operate_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        # 指定Student模型映射到数据库中时，对应的表名。
        db_table = 'student'






