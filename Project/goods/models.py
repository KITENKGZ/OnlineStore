from tabnanny import verbose
from unicodedata import category
from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='カテゴリー名')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='商品名')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='商品説明')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='商品画像')
    price = models.DecimalField(default=0, max_digits=7, decimal_places=0, verbose_name='商品価格')
    discount = models.DecimalField(default=0, max_digits=7, decimal_places=0, verbose_name='割引％')
    quantity = models.PositiveIntegerField(default=0, verbose_name='在庫量')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='カテゴリー')

    class Meta:
        db_table = 'product'
        verbose_name = '商品'
        verbose_name_plural = '商品'
    
    def __str__(self):
        return f'{self.name} 在庫は{self.quantity}'
    
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)  
        return self.price