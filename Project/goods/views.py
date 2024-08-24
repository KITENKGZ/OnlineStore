from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products

# カタログを表示関数
def catalog(request, category_slug):
    # ページ番号を取得
    page = request.GET.get('page', 1)

    # スラッグで商品をDBから取得、フィルタリング
    if category_slug == "all":
        goods = Products.objects.all()  # すべての商品を取得
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))  # 指定されたカテゴリーの商品を取得

    # ページネーション設定
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    # コンテキストデータ
    context = {
        'title': 'カタログ',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)

# 商品詳細ページを表示関数
def product(request, product_slug):
    # スラッグで特定の商品をDBから取得
    product = Products.objects.get(slug=product_slug)
    
    # コンテキストデータ
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context)