from django.db import models
from django.contrib.auth.models import AbstractUser

# カスタムユーザーモデルを定義
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='プロファイル画像')  # プロファイル画像用のフィールド

    class Meta:
        db_table = 'user'  # データベースのテーブル名を指定
        verbose_name = 'ユーザー'  # 管理画面での単数形の名前
        verbose_name_plural = 'ユーザー'  # 管理画面での複数形の名前
    
    # ユーザー名を返すメソッド、管理画面やシェルでの表示に使用
    def __str__(self):
        return self.username