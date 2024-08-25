from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# メインページを表示するビュー
def index(request):
    context = {
        'title':  'メインページ',  # ページのタイトル
        'content': 'イタリア家具のショップ',  # ページのコンテンツ
    }

    # テンプレートをレンダリングしてレスポンスを返す
    return render(request, 'main/index.html', context)

# 会社概要ページを表示するビュー
def about(request):
    context = {
        'title':  '会社概要',  # ページのタイトル
        'content': '会社概要',  # ページのコンテンツ
        'text_on_page': 'SOME TEXT'  # 追加のテキスト
    }

    # テンプレートをレンダリングしてレスポンスを返す
    return render(request, 'main/about.html', context)