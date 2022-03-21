from unicodedata import name
from django.db import models

# Create your models here.
from django.db import models

from os import path
from datetime import date

from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

class ClassTypeList(models.TextChoices):
    CLASS = 'CL', '精英班'
    TRAINING = 'TR', '中国集训队'


ROLE_CHOICES = [
    ("Coach", "教练"),
    ("Competitor", "选手"),
    ("Student", "学生"),
]

MODULE_LIST = [
    ("ModuleA", "A模块: ServerClient"),
    ("ModuleB", "B模块: Network"),
    ("ModuleC", "C模块: Python"),
    ("ModuleD", "D模块: TroubleShooting"),
    ("ModuleE", "E模块: English"),
    ("Other", "Other"),
]

# Define user directory path
def user_dierctory_path(instance, filename):
    # 文件扩展名
    ext = filename.split('.')[-1]
    # 作者的角色名字
    for i in ROLE_CHOICES:
        if i[0] == instance.author_role:
            author_role = i[1]
    # 作者的姓名
    author_name = instance.author_name
    # 班级类型的名字
    class_type = ClassTypeList(instance.class_type).label
    class_type_log = f'第46届世界技能大赛网络系统管理项目{class_type}训练日志'
    # 日志的写作日期
    log_date = instance.log_date.strftime("%Y.%m.%d")
    # 模块的名字
    module_list = instance.module_list
    # 文件名重命名的组合方式
    filename_parts = [author_role, class_type_log,
                      module_list, author_name, log_date]
    filename = '-'.join(filename_parts) + '.' + ext
    # filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return path.join(
                        "tlogs",
                        log_date.split('.')[0], 
                        log_date.split('.')[1], 
                        log_date.split('.')[2], 
                        filename
                        )



# remove log_file if exists when it upload.
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            self.delete(name)
        return name


class LogUploadModel(models.Model):
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
     )
    author_name = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name="作者"
    )
    # author_name = models.OneToOneField(
    #     'accounts.User',
    #     on_delete=models.CASCADE,
    #     verbose_name="作者"
    # )

    # name = models.CharField(
    #     max_length=10,
    #     # default=get_username,
    #     verbose_name="作者"
    # )

    author_role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="Competitor",
        blank=False,
        verbose_name="角色"
    )
    log_date = models.DateField(
        default=date.today,
        verbose_name="日期"
    )
    class_type = models.CharField(
        max_length=100,
        choices=ClassTypeList.choices,
        default=ClassTypeList.TRAINING,
        verbose_name="班级"
    )
    log_file = models.FileField(
        upload_to=user_dierctory_path,
        storage=OverwriteStorage(),
        null=False,
        # unique=True,
        help_text="只能上传pdf格式的文件。",
        verbose_name="文件"
    )
    module_list = models.CharField(
        max_length=100,
        choices=MODULE_LIST,
        default="ModuleA",
        verbose_name="模块"
    )
    uploaded_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="上传时间"
    )

    class Meta:
        ordering = ('-log_date', '-uploaded_date',)

    def log_file_name(self):
        return path.basename(self.log_file.name)

    def class_type_name(self):
        return ClassTypeList(self.class_type).label



    # def __str__(self):
    #     return self.author_name

class TlogEvaluate(models.Model):
    tlog = models.ForeignKey(LogUploadModel, on_delete=models.CASCADE)
    evaluate_score = models.IntegerField(
        default=0,
        verbose_name="评分"
    )
    evaluate_content = models.CharField(
        max_length=100,
        default="",
        verbose_name="评论"
    )
    evaluate_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="评价时间"
    )
    evaluate_coach = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name="评价教练"
    )



