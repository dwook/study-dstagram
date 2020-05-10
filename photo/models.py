from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_photos")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default="photos/no_image.png")
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:  # 옵션 클래스
        ordering = ["-updated"]

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self): # 객체의 상세 페이지 주소를 반환
        return reverse('photo:photo_detail', args=[str(self.id)])

