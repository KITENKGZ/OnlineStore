from django.urls import path

from main import views

app_name = 'main'  # アプリケーション名を指定することで、URL名の衝突を防ぐ

urlpatterns = [
    path('', views.index, name='index'),  # メインページへのルート
    path('about/', views.about, name='about'),  # 会社概要ページへのルート
]