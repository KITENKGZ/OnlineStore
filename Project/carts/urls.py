from django.urls import path

from carts import views

app_name = 'carts'  # アプリケーション名を指定してURL名の衝突を防ぐ

urlpatterns = [
    path('cart_add/', views.cart_add, name='cart_add'),  # カートに商品を追加するルート
    path('cart_change/', views.cart_change, name='cart_change'),  # カート内の商品数量を変更するルート
    path('cart_remove/', views.cart_remove, name='cart_remove'),  # カートから商品を削除するルート
]
