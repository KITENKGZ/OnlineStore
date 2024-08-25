from carts.models import Cart

# 認証済みのユーザーのカートを取得する関数
def get_user_carts(request):
    if request.user.is_authenticated:  # ユーザーが認証されているか確認
        return Cart.objects.filter(user=request.user)  # ユーザーに関連するカートを返す