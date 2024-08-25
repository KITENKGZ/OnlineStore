from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.utils import q_search
from goods.models import Products

# カタログを表示する関数
def catalog(request, category_slug=None):
    # ページ番号を取得
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)  # セール中の商品を表示するオプション
    order_by = request.GET.get('order_by', None)  # 並び替えオプション
    query = request.GET.get('q', None)  # 検索クエリ

    # 商品をスラッグ、クエリ、セールの状態でフィルタリングして取得
    if category_slug == 'all':
        goods = Products.objects.all()  # すべての商品を取得

    elif query:
        goods = q_search(query)  # 検索クエリに基づいて商品を検索
        
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))  # 指定されたカテゴリーの商品を取得

    if on_sale:
        goods = goods.filter(discount__gt=0)  # セール中の商品をフィルタリング

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)  # 指定された順序で並び替え

    # ページネーションの設定
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    # コンテキストデータを作成
    context = {
        'title': 'カタログ',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)

# 商品詳細ページを表示する関数
def product(request, product_slug):
    # スラッグで特定の商品を取得
    product = Products.objects.get(slug=product_slug)
    
    # コンテキストデータを作成
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context)