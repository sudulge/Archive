from django.db import models

# Create your models here.

#영화/애니, 책 모델 따로 만들어야 할듯? 그래야 그 라인 구분이 됨


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='archive', null=True, blank=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
