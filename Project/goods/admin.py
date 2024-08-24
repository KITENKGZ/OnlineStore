from django.contrib import admin
from goods.models import Categories, Products

# カテゴリーモデルの管理クラス
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # 名前に基づいてスラッグフィールドを自動生成
    # 日本語対応していないから手入力必要
    prepopulated_fields = {'slug': ('name',)}

# 商品モデルの管理クラス
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    # 名前に基づいてスラッグフィールドを自動生成
    # 日本語対応していないから手入力必要
    prepopulated_fields = {'slug': ('name',)}