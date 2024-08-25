from django.db import models
from goods.models import Products
from users.models import User

# カート用のカスタムクエリセット
class CartQuerySet(models.QuerySet):
    
    # カート内の商品の合計金額を計算するメソッド
    def total_price(self):
        return int(sum(cart.products_price() for cart in self))
    
    # カート内の商品の合計数量を計算するメソッド
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

# カートモデルの定義
class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ユーザー')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='注文品')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='数量')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='追加した日付')

    class Meta:
        db_table = 'cart'  # データベースのテーブル名
        verbose_name = 'カート'  # 管理画面での単数形の名前
        verbose_name_plural = 'カート'  # 管理画面での複数形の名前

    # カスタムクエリセットをオブジェクトマネージャーとして使用
    objects = CartQuerySet().as_manager()

    # カート内の商品の総価格を計算するメソッド
    def products_price(self):
        return int(round(self.product.sell_price() * self.quantity, 2))

    # オブジェクトの文字列表現を定義
    def __str__(self):
        return f'{self.user.username}のカート | 商品 - {self.product.name} | 数量 - {self.quantity}'