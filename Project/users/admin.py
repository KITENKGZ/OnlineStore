from django.contrib import admin
from users.models import User

# 簡単に管理画面に追加
admin.site.register(User)