from django.db import models

'''
models.py (goods)

goodsアプリのデータベースモデルを定義しています。
商品モデルは、カテゴリー、在庫、価格、割引、画像などのプロパティを管理します。

DjangoのORM機能を使用して、商品とカテゴリーの管理、表示、および処理を効率的に行うことを目的としています。
'''

# カテゴリーのモデルを定義
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='カテゴリー名') # カテゴリー名のフィールド
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL') # URL用のスラッグフィールド

    class Meta:
        db_table = 'category' # データベースのテーブル名を指定
        verbose_name = 'カテゴリー' # 管理画面での単数形の名前
        verbose_name_plural = 'カテゴリー' # 管理画面での複数形の名前

    def __str__(self):
        return self.name # 管理画面やシェルでの表示用にカテゴリー名を返す


# 商品のモデルを定義
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='商品名') # 商品名のフィールド
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL') # URL用のスラッグフィールド
    description = models.TextField(blank=True, null=True, verbose_name='商品説明')  # 商品説明のフィールド
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='商品画像') # 商品画像のフィールド
    price = models.DecimalField(default=0, max_digits=7, decimal_places=0, verbose_name='商品価格') # 商品価格のフィールド
    discount = models.DecimalField(default=0, max_digits=7, decimal_places=0, verbose_name='割引％') # 割引率のフィールド
    quantity = models.PositiveIntegerField(default=0, verbose_name='在庫量') # 在庫量のフィールド
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='カテゴリー') # カテゴリーとの外部キー

    class Meta:
        db_table = 'product' # データベースのテーブル名を指定
        verbose_name = '商品' # 管理画面での単数形の名前
        verbose_name_plural = '商品' # 管理画面での複数形の名前
        ordering = ("id",) # デフォールト並び順をIDで設定
    
    # 管理画面の表示用に商品名と在庫数を返すメソッド
    def __str__(self):
        return f'{self.name} 在庫は{self.quantity}' 
    
    # 商品IDを5桁で表示するメソッド
    def display_id(self):
        return f'{self.id:05}'
    
    # 割引がある場合、割引後の価格を計算して返す、ない場合、そのままの価格を返すメソッド
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        return self.price