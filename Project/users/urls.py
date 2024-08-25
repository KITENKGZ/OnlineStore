from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),  # ログインページへのルート
    path('registration/', views.registration, name='registration'),  # 新規登録ページへのルート
    path('profile/', views.profile, name='profile'),  # プロファイル管理ページへのルート
    path('users-cart/', views.users_cart, name='users_cart'),  # ユーザーのカートページへのルート
    path('logout/', views.logout, name='logout'),  # ログアウト機能へのルート
]