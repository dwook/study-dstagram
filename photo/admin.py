from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']  # 모델의 필드를 선택하거나 별도의 함수를 만들어 필드처럼 등록
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created']
    ordering = ['-updated', '-created']


admin.site.register(Photo, PhotoAdmin)
