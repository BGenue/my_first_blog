from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)#관리자 페이지에서 Post모델을 보기 위해 등록함
