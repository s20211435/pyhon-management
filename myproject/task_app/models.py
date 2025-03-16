from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('L', '低'),
        ('M', '中'),
        ('H', '高'),
    )

    STATUS＿CHOICES = (
        ('TODO', '未着手'),
        ('DOING', '進行中'),
        ('DONE', '完了'),
    )

    title = models.CharField('タイトル', max_length=100)
    description = models.TextField('説明', blank=True)
    status = models.CharField('ステータス', max_length=5, choices=STATUS＿CHOICES, default='TODO')
    priority = models.CharField('優先度', max_length=1, choices=PRIORITY_CHOICES, default='M')
    due_date = models.DateTimeField('期限', blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_task_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ('-due_date', 'priority', 'title')
        verbose_name = 'タスク'
        verbose_name_plural = 'タスク'
