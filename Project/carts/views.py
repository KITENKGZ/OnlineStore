from math import prod
from urllib import response
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from carts.utils import get_user_carts
from carts.models import Cart
from goods.models import Products

# カートに商品を追加する関数
def cart_add(request):
    product_id = request.POST.get("product_id")  # リクエストから商品IDを取得
    product = Products.objects.get(id=product_id)  # 商品IDで商品をDBから取得

    if request.user.is_authenticated:  # ユーザーが認証済みか確認
        carts = Cart.objects.filter(user=request.user, product=product)  # ユーザーのカートを取得

        if carts.exists():  # すでにカートに商品が存在する場合
            cart = carts.first()  # 最初のカートアイテムを取得
            if cart:
                cart.quantity += 1  # 商品の数量を増加
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)  # 新しいカートアイテムを作成

    user_cart = get_user_carts(request)  # ユーザーのカートを取得

    # カートのHTMLをレンダリング
    cart_items_html = render_to_string(
        "cart.html", {"carts": user_cart}, request=request)
    
    response_data = {
        "message": "カートに追加されました",  # メッセージ
        "cart_items_html": cart_items_html,  # レンダリングされたカートのHTML
    }

    return JsonResponse(response_data)  # JSONレスポンスを返す

# カート内の商品数量を変更する関数
def cart_change(request):
    cart_id = request.POST.get("cart_id")  # リクエストからカートIDを取得
    quantity = request.POST.get("quantity")  # リクエストから新しい数量を取得

    cart = Cart.objects.get(id=cart_id)  # カートアイテムを取得

    cart.quantity = quantity  # 数量を更新
    cart.save()
    updated_quantity = cart.quantity  # 更新後の数量を取得

    cart = get_user_carts(request)  # ユーザーのカートを取得
    cart_items_html = render_to_string(
        "cart.html", {"carts": cart}, request=request)
    
    response_data = {
        "message": "数量が変更されました",  # メッセージ
        "cart_items_html": cart_items_html,  # レンダリングされたカートのHTML
        "quantity": updated_quantity,  # 更新された数量
    }

    return JsonResponse(response_data)  # JSONレスポンスを返す

# カートから商品を削除する関数
def cart_remove(request):
    cart_id = request.POST.get("cart_id")  # リクエストからカートIDを取得

    cart = Cart.objects.get(id=cart_id)  # カートアイテムを取得
    quantity = cart.quantity  # 削除する前の数量を取得
    cart.delete()  # カートアイテムを削除

    user_cart = get_user_carts(request)  # ユーザーのカートを取得
    cart_items_html = render_to_string(
        "cart.html", {"carts": user_cart}, request=request)
    
    response_data = {
        "message": "商品は削除されました",  # メッセージ
        "cart_items_html": cart_items_html,  # レンダリングされたカートのHTML
        "quantity_deleted": quantity,  # 削除された数量
    }

    return JsonResponse(response_data)  # JSONレスポンスを返す