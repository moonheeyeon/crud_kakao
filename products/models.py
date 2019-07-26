from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True) #빈 값도 참으로 인식함
    price = models.IntegerField()
    view_count = models.IntegerField(default=0) #default값을 설정해야함
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", null=True) #pip install pillow

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    #title을 제목으로 받게 해주는 함수