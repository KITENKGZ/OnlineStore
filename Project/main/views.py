from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    context = {
        'title':  'メインページ',
        'content': 'イタリア家具のショップ',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title':  '会社概要',
        'content': '会社概要',
        'text_on_page': 'SOME TEXT'
    }

    return render(request, 'main/about.html', context)