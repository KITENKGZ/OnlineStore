from django.urls import path

from goods import views

app_name = 'goods'  # アプリケーション名を指定してURL名の衝突を防ぐ

urlpatterns = [
    path('search/', views.catalog, name='search'),  # 検索結果を表示するルート
    path('<slug:category_slug>/', views.catalog, name='index'),  # カテゴリー別のカタログページを表示するルート
    path('product/<slug:product_slug>/', views.product, name='product'),  # 商品詳細ページを表示するルート
]
