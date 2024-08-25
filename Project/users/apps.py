from django.apps import AppConfig

# アプリケーションの設定を行うクラス
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'  # アプリケーション名を指定
    verbose_name = 'ユーザー'  # 管理画面でのアプリケーション名を設定