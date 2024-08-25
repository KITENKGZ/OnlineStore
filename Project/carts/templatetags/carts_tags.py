from django import template

from carts.utils import get_user_carts
from carts.models import Cart

# テンプレートタグライブラリの登録
register = template.Library()

# ユーザーのカートを取得するカスタムテンプレートタグ
@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)  # 現在のユーザーのカートを取得して返す