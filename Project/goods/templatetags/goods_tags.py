from atexit import register
from django import template
from django.utils.http import urlencode
from goods.models import Categories

# テンプレートタグライブラリの登録
register = template.Library()

# 全てのカテゴリを取得するタグ
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

# URLのクエリパラメータを変更するタグ
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()  # 現在のクエリパラメータを取得
    query.update(kwargs)  # 新しいパラメータを追加または更新
    return urlencode(query)  # パラメータをURLエンコードして返す